ini message list():
// do it after user login.
将消息的更新存储到redis上

create message():
// 根据给定的type和参数列表,来构造message json 数据.
1. switch type
2. set message

deal message to one()
// server deal message
1. 创建消息到 message table.[type,message] ,获取消息的m_id
2. 给指定的uid的用户增加消息队列[uid], 并更新时间戳,消息队列 到 user message table
2. 查看该用户是否在线,如果在线,更新redis上面的时间戳.

check message ()
// every time client send a http resquest, do this.
1. 检查redis 里面的队列更新update message to user 时间.[update time client]
2. 如果发现update time client 比 redis 里面的早. send message()


send message()
1. uid 获取自己在 user message table 的 message queue
2. 把信息发送给用户.他

return message():
// check if client get the message successfully
// I think if the message is circle message, we needn't do this.
result == true--> clear user message table
to one --- > special user.
to many -- > user list
to all. --->circle

deal message to many()
// server deal message to many user.
1. 创建消息到 message table ,获取消息的m_id
2. 给指定的uid list 更新消息队列到 user message table [m id]
3. 查看uid list 的里面的uid 是否在线,如果在线更新到redis上面

// the same to check message to one
check message ()
// every time client send a http resquest, do this.
1. 用户检查redis 里面自己的uid的update message to user 时间.[update time client]
2. 如果发现update time client 比 redis 里面的早. send message()


// the same to send message to one
send message()
1. uid 获取自己在 user message table 的 message queue
2. 把信息发送给用户.

// the same to return message to one
return message():
// check if client get the message successfully
// I think if the message is circle message, we needn't do this.
result == true--> clear user message table

ini message to all()
1. 为每个现有的圈子创建redis缓存

deal message to all()
// server deal mesage to all of user in circle.
1. 创建消息到message table[type table],获取消息的m_id
2. 给消息对应的circle message table 的[todo 使用 umeng id 还是 自己设置circle] message字段增加 m_id 消息,并更新其updatetime
3. 更新redis上面的时间戳. redis 应该重新维护一套给圈子用的字典, 这个字典记录[add  redis: circle_id, message_queue, update time circle]

check message to all()[高并发操作!]
// every time client send a http resquest, do this.
1. 获取用户的 my circle list [my circle list]
2. 检查redis 里面的用的 my circle list 的circle id[todo:使用umeng还是自己的?]
3. 如果发现update time client 比 redis 里面的早. 从 circle message table 提取对应的 message_id.
	1. 加到 send message id list
4. 遍历完成之后,如果 send message id list 不是空的,运行 send message to all ()

send message to all()
1. 获取message list 所有id 的数据,得到一个结果队列,包括type 和 message.[message id list]
2. 将结果反馈给客户端.
----
update:
 将 check message to all 和 send message to all 合并城一个函数. 修改check message,增加 id type 属性.

clear_circle.

需要的数据结构:
1. message table 消息队列列表
2. user message table 用户消息列表
3. circle message table
4. redis: user 实例 需要维护 uid, access token update time to user数据
5. redis: circle 实例,需要维护:circle_id, message_queue, update time circle


消息更新逻辑重新整理:
1. 用户队列和圈子队列统一更新,用户只有一个last_update_time 字段.
2. 查看用户的redis_dict 的update 字段, 比较确定用户是否需要更新用户消息队列.
	- 如果需要更新,则返回更新的消息存储.
3. 通过上传的 my_circle_list 查找所有 circle: 的update time.
	- 如果需要更新,则 返回对应的消息队列存储.
	- 寻找下一个队列.
4. 拼接所有获取的消息队列, 通过访问send message 的方法. 获得 message content 的 list
5. 返回给客户端.