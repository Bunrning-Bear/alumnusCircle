## database:
- 数据库存放原则：
	- mysql 存放账号密码和写死的字段，以及
	- elasticsearch 仅存放和搜索需要筛选的相关信息，以及在列表层次需要展示的信息，以及该信息在Umeng对应的id
	- Umeng 存放所有信息。
	- 操作
		- 增
			- 新增用户
				- 用户信息需要同时写入mysql，elasticsearch，umeng
			- 新增圈子
				- elasticsearch
					- 与搜索相关的信息：简介，标签，名称。
					- 用于筛选的信息：类别
					- 用于展示的信息：名称。
					- 用于排序的信息：匹配度和活跃度综合排序： [一日前的人数，一日前的feed数 [Umeng有现成的接口]][新增人数，日新增公告数，日更新] [2.0]
				- mysql：
					- 无
				- umeng:
					- 所有信息都要的
			- 新增公告---暂时不考虑搜索，直接和umeng交接
		- 查
            - 登陆注册的时候经过mysql，然后再访问Umeng
            - 发送搜索请求的时候，返回结果列表只访问elasticsearch，然后返回结果是列表信息，并且携带了可以到Umeng搜索到唯一feed的feedid
            - 获取某个项目的详情的操作，非搜索的列表获取，直接访问umeng来实现
            - 查找用户：
            	- 精确查找[个人信息，查找特定的校友圈号的用户]---直接访问umeng的搜索功能
            	- 搜索用户：
            		- elasticsearh
            			- 于模糊搜索相关的信息：姓名，职业，公司，专业，标签，个人简历，工作经历。
            			- 用于筛选的信息：常驻城市，入学年份，所在院系
            			- 用于展示的信息：姓名，院系，年级，职业。
            			- 用于排序的信息：仅靠匹配度
            			- 公开度处理的信息：用户是否愿意被公开搜索到的字段。
            		- mysql：
            			- 无
            		- umeng：
            			- elasticsearch字段
            			- umeng自带字段
            			- 自定义字段：
                            - work year publicity [int] 工龄公开度
                            - private telephone publicity [int] 个人电话公开度
                            - public telephone publicity [int] 公共电话公开度
                            - qq publicity [int] QQ公开度
                            - wechat publicity [int] 微信公开度
                            - career publicity [int] 工作经历公开度
                            - if can be find [bool] 记录是否能够被搜索到
                            - 
                            - work year [int] 工龄
                            - private telephone [array] 个人电话
                            - public telephone [array] 公共电话
                            - qq [string] 个人
                            - wechat [string]
                            - career [json]
            - 查找圈子：
            	- 分类别查找： 我们给圈子分类别[友盟里面的话题分类]，调用分类话题的接口，直接返回给用户
            	- 模糊搜索：
            		- elasticsearh
            			- 于模糊搜索相关的信息：圈子介绍，圈子标签，圈子名称
            			- 用于筛选的信息：不尽兴筛选[或者使用分类进行筛选]
            			- 用于展示的信息：展现的是圈子的名字,[考虑展示匹配信息？]
            			- 用于排序的信息：匹配度和活跃度综合排序： [一日前的人数，一日前的feed数 [Umeng有现成的接口]][新增人数，日新增公告数，日更新] [2.0]
            			- 公开度处理的信息：圈子应该也有通过精确搜索才能找到的序号[2.0 暂时不考虑]
            		- mysql:
            			- 无
            		- umeng：
            			- 圈子动态列表
            				- 友盟提供接口：话题的feed流，话题热门的feed流，时事话题热门的feed流
            			- 圈子信息
            				- 标签 tags
            				- 介绍 description
            				- 图片 icon url
            				- 名称 name
            				- 管理员
            			- 圈子成员列表
            				- 友盟提供接口：话题的粉丝列表
            - 查找公告：
            	- 查找用户的公告列表
            	- 查找圈子的公告列表
            	- 详情看team的doc文档
		- 删：
			- 删除话题：[需要经过审核]，提示是否有人愿意接管
			- 删除公告：直接删除
			- 删除名片：取消关注
		- 改：
			- 修改圈子：
				- 管理员修改：访问后台，确认管理员身份之后，执行话题编辑操作。
			- 不能修改公告
-user dict:维护的用户在线信息表.

- mysql
	- user info
        - uid [int]：用户id
        - telephone[string]:注册手机号
        - password[string]:密码
        - stu id[int]:从数据库获取的学号
        - uni id[int]:学校id，目前只有东南大学，设置为1
        - access token[string] umeng的access token
    - user show:
        - show id：详情信息表的id
        - uid：作为user info 的uid的约束的外键
        - admission year[int]:入学年份，
        - faculty id [int] 用户的院系id
        - major id：[int] 某个major对应的id
        - name[string]： 用户的真实姓名
        - gender[string]：性别
        - my circle list[field of circle id] 我加入的圈子列表
    - major id table：专业和id的对应表[这个表放在客户端，不然每次多访问一次数据库不合适]
    	- major id[int]:user info 表格的id
    	- major name[string]:对应的专业名
    - [如果话题不支持管理员功能，管理员存储在mysql里面]
    - circle ：[记录圈子的基本信息，防止圈子重名]
    	- cid
    	- umengcid
    	- name
- elasticsearch and umeng
	- user[用户的自定义字段比较多，所以只存放uid，uid能够找到具体信息，所以查看用户详情的时候，直接访问mysql。]
		- 列表级别的信息：
			- 姓名，入学年份，院系，专业，头像，现在的职业
		- source uid = source id 是 mysql 里面的 phone.
		- username = telephone：
		- icon url
		- umeng id[string] 友盟 用户id
		- custom
            - stu id[int]:从数据库获取的学号
            - admission year[int]:入学年份
            - faculty id [int]:院系id
            - major id：[int] 专业的id
            - gender[string]：性别
	- feed
		- id[string] feed id
		- content[string] 内容
		- creator [field] 创建者相关信息？
		- topics [string] 只有一个话题，也就是只隶属于一个圈子
		- status[int] 状态---见友盟状态码
		- create time[datetime] 创建时间
		- stats [field] 各项计数值[liked comments forwards[转发不需要的]]
		- image urls[field] :url链接列表
		- title [string]：feed标题
		- main img url [string] 封面图片的url
	- circle
	- comment
	- like



message table:
m_id
type:
time：
message:
type:1 发给圈子发起人的消息，宣布其创建圈子的处理结果：
{
	"topic name"
	“agree”: true of false,
    [if "agree" == true]
    [if "agree" == false]
    "reason":手工填写的拒绝理由
    icon_url:
}	
type：2 全体成员都能接受到的消息，由圈子的管理员或者创始人发送：
{
	”topic“：{
    	”id“：
        ”name“：
    }，
    ”message“:{
        "umeng id ":[被任免的用户的id].
        "username":[被任免的用户的用户名]
        "method":[操作名 set or cancel]
    }
}
type:3 申请人发给管理员的消息[加入圈子的审核消息]
	{
    	"topic"：{
        	“id”:topic id 当用户需要获取该圈子的详情的时候，可以通过这个topic id 来找到这个话题的详细信息。
            “name”:话题的文本名称，用于直接在前端显示,
            [todo]"topic_url"
        },
        "applyer":{
        	“id”:申请人id，方便用户需要获取这个申请人的详细信息的时候，通过这个id可以直接向服务器发送请求
            “name”：申请人的文本名称，用于直接在前端显示
            [todo]"topic_url"
        },
        “question”:{
        	//这是一个可变长度的json数组
           {
           	"questionname":问题的题目，
            “answer“：申请人的答案
            }，
            {
            ”questionname“：问题的题目，
            ”answer“：申请人的答案
            }
            ……
        }
    }
type:4  申请人接受到的消息，他发出的消息的处理结果
    {
    	"topic":{
        	“id”:topic id 当用户需要获取该圈子的详情的时候，可以通过这个topic id 来找到这个话题的详细信息。
            “name”:话题的文本名称，用于直接在前端显示
        },
        "method": "set or cancel"
        "member":{
        	"name":用于显示的名字,
            "umengid":用于查找详细信息的umengid
        }
    }


manual_review table
review_id:
name:
icon_url:
creator_uid:[umeng uid]:创建者的id
circle_name：圈子的名字
circle_icon_url:圈子的图标
circle_type:圈子类别
create_reason_message:创建者填写的创建理由
deal[int] 0 not deal yet. 1 agree	.2 disagree

user_message_table:
id:
uid:
message_queue[array]


circle_message_table:
cm_id:
time:
circle_id:
m_id:[message_id 的id,记录的这条消息]

redis:里面需要有专门的字段用来记录用户是否已经成功接受到消息了：
deal:[bool]
这几个message表的特点:记录数据库，只有读写操作，没有修改操作的数据操作。试试可否进行高效的处理