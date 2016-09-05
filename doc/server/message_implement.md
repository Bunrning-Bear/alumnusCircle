### 本文解决的问题：

*   圈子的发起人creator申请圈子--->服务器--->后台人工审核--->写入友盟数据库--->告知用户的逻辑实现；
*   圈子发起人--->任命/撤销管理员操作--->服务器--->写入友盟数据库--->告知所有管理员任命和撤销决定 的逻辑实现；
*   圈子管理员/圈子创始人--->踢出群成员---->服务器--->写入友盟数据库--->告知所有管理员和被踢用户；
*   圈子申请人--->从服务器获取题目信息--->提交答案--->服务器--->发送给管理员审核通知--->接受第一个管理员的处理请求-->写入服务器--->反馈给申请人结果

### 名词解释：
1.  圈子的发起人 creator ： 圈子的创建者，提出创建圈子的人，拥有管理圈子的最高权限；
2.  圈子的管理员 administrator：圈子的管理员，由圈子的创建者任命，能够审核群成员，踢出群成员，发布群通知；
3.  圈子的成员 member:圈子普通成员。
4.  圈子的申请人 applier：申请加入圈子的人

### 需要用到的mysql数据库：
manual_review_table：人工审核表。
message_table：消息队列表
user_message_table:用户消息队列表
circle_message_table：圈子消息队列[用于群发消息]
redis：
- 存放用户idumengid uid 
- 消息处理列表：user message queue ，circle message queue
- 更新时间：update time 
- 记录是否处理消息：deal
### 具体分析：
1. 圈子的发起人creator申请圈子--->服务器--->后台人工审核--->写入友盟数据库--->告知用户的逻辑实现；
	1.  首先，圈子的发起人需要填写三方面的信息:
		1.  用于在圈子列表展示的信息，称为show_message: 圈子名称，圈子图片[有默认值]，圈子所属类别；
        2.  发起人填写的用于后台审核的信息，称为create_reason_message: 申请圈子理由；
        3.  [2.0]: 发起人设置的，给申请人填写的问卷信息，称为 quession_list： 问卷列表；
        4.  圈子发起人信息，称之为 creator_uid:发起人的 友盟uid，[mysql uid？]
    2.  4方面的信息经过合法性的检验 validation_check，如果检验失败，返回给客户端，如果成功，传递给后台服务器，写入mysql的manual_review_table里面;
    3.  后台管理员打开审核界面，进行人工审核：
    	1.  如果审核失败：
    		1.  message_table:加入一条type1的消息，这个类型是”申请结果“类型的消息;
    		2.  并把这个消息加入到user_message_table 的 uid == creator_uid 的 message_queue 队列中。这个消息包括：
    			- 申请的圈子的name：circle_name;
    			- 申请的结果 result = false;
    			- 失败的理由 reason;
            2.  进入”消息队列处理逻辑“，下文详解。
        2.  如果审核成功：
        	1.  后台服务器登陆的是”全局管理员账号“，发送创建话题的请求，需要的信息包括：
        		*   name 圈子名称
                *   tags 圈子标签
                *   icon_url 圈子的头像
                *   description 圈子描述
                *   自定义字段：
				 	- 圈子创建人 creator_id
 					- 圈子管理员 administration_id
 					- 问卷列表 question_list
            2.  从Umeng获取反馈的信息，取得里面的如下json：
            	- circle_id:圈子id.
            	- circle_name:圈子的名字.
            3.  接下来要把这条消息存储到用户的消息队列：
				- message_table:加入一条type1的消息，这个消息类型是申请结果类型的消息；
				- 把这个消息加入到user_message_table 的 uid == creator_uid 的message_queue 队列中，这个消息队列包括：
    			- 申请的圈子的name：circle_name;
    			- 申请的结果 result = true;
    			- 圈子的信息的json：
    				- 圈子的id:circle_id
    				- 圈子的名字：circle_name
    		4. 等待用户发送http请求，进入消息队列推送处理程序
2. 圈子发起人--->任命/撤销管理员操作/踢出群成员--->服务器--->写入友盟数据库--->告知所有成员任命和撤销决定 的逻辑实现
	1. 圈子发起人在管理成员列表中点击触发http请求，客户端获取任命/撤销的管理员uid，客户端带着umengid和method = set or cancel 给服务器；
	2. 服务器向友盟修改custom字段.
	3. 成功之后生成一个type2 的消息 存在 message_table 里面,需要的数据字段有:
		- circle_id[umeng]
		- umengid[被任免的用户的id].
		- username[被任免的用户的用户名]
		- method[操作名 set or cancel]
	4. 同时,circle_message_table写入操作:
		- time[时间戳]
		- circle_id[圈子id]
		- m_id[message_id]
	5. 用户发送http请求的时候,要请求上次进行http请求时的时间戳,然后从那个时间戳之后开始遍历寻找更新值,需要的数据
		- circle_id_list:自己加入的圈子
		- time
		- user_id
	6. 找到message id 存储到redis里面.
3.  圈子申请人--->从服务器获取题目信息--->提交答案--->服务器--->发送给管理员审核通知--->接受第一个管理员的处理请求-->写入服务器--->反馈给所有人结果
	1. 在点开圈子详情页面的时候,申请人就获取了题目的文本信息, 点击申请的时候,将输入信息上传给服务器,需要接受的信息有:
		- 问卷的题目列表
		- 问卷的答案列表
		- 申请人的umeng id
		- 申请人的name
		- 圈子的topic id
	2. 得到消息接受人：这些信息被传给服务器，服务器做合法性检验，成功之后，访问友盟数据库，通过topic id 找到topic detail信息，得到里面的管理员和创始人的umeng id.
	3. 创建消息：在message table 里面创建这条消息，记录一条m id
	4. 消息处理：
		1. 给每个友盟id的消息队列user message table 的 message queue 增加一条m id, 并更新时间戳
		2. 查看用户是否在线，如果用户在线，更新redis上的时间戳
		3. 用户发送http请求的时候发现时间戳更新，并且未被处理，则从数据库上面获取信息，客户端确定正确收到消息之后，则反馈给redis，消息已经被处理, 清空数据库的消息队列。
		4. 如果用户不在线,则访问user message table 列表的 该uid 的信息,获取其message update time给redis
	7. 发起人审阅消息阶段：客户端接受到消息，选择处理结果[同意，拒绝申请]：将处理结果发送给服务器，包括以下字段：
		- 处理结果 result.
		- 申请人的umeng id.
		- 申请人的name
		- 圈子的 topic id
	8. 创建消息：服务器新建消息，message table，需要把处理结果推送给消息发送者，需要的的字段：
		- 处理结果 result.
		- 申请人的umeng id.
		- 申请人的name
		- 圈子的 topic id
	9. 设置消息的接受者[单人接收]：user message table [如果用户在线还要存在 redis 里面], umengid 的对应条目的消息队列增加 m id，并更新时间戳。
	10. 用户发送http请求的时候，发现消息队列的时间戳更新，并且还没被发送给客户端[未被处理]，客户端获取消息进行处理。
- 消息处理逻辑:
    1. 新的消息出现了.
    2. 给每个友盟id的消息队列user message table 的 message queue 增加一条m id, 并更新时间戳
    2. 查看用户是否在线，如果用户在线，更新redis上的时间戳
    3. 用户发送http请求的时候发现时间戳更新，并且未被处理，则从数据库上面获取信息，客户端确定正确收到消息之后，则反馈给redis，之后消息已经被处理, 清空数据库的消息队列。
    4. 如果用户不在线,则访问user message table 列表的 该uid 的信息,获取其message update time给redis,用户登陆的时候redis获取 user message table 的 updatetime.
### 总结：
思路大体理清楚了，但是实际上肯定还会遇到问题，需要持续补充
