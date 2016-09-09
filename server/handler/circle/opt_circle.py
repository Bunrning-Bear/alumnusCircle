# opt_circle.py
import tornado.web
import tornado.gen

from handler.circle.circle import TopicHandler
from handler import request

class CircleApplyHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(CircleApplyHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/fans'
        self.methodUsed = 'GET'    
        self.requestName ='circle_apply'    

    @request.authenticated('circle_apply')        
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        circle_id = self.get_argument('circle_id')
        circle_name = self.get_argument('circle_name')
        circle_url = self.get_argument('circle_url')
        reason = self.get_argument('reason')
        uid = self.get_secure_cookie('uid')
        creator_id =self.get_argument('creator_id')
        # create message to all of admin and creators
        mid = self.message.create_message(type_id=4,
            circle_id=circle_id,circle_name=circle_name,circle_url=circle_url,reason=reason,uid=uid)
        # [todo] this message should send to all of admin and creator.
        self.message.deal_message_to_one(mid,creator_id)
        code = self.return_code_process(0)
        message = "set apply successfully!!"
        self.return_to_client(code,message)
        self.finish()

class LeaveCircleHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(LeaveCircleHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/unfocus'
        self.methodUsed = 'DELETE'    
        self.requestName ='leave circle'   

    @request.authenticated('circle_apply')        
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
            this is umeng cid.: circle_id
        """
        circle_id = self.get_argument('umeng_circle_id')
        Data = {'topic_id':circle_id}
        uid = self.get_secure_cookie('uid')
        access_token = self.get_redis_dict_access_token(uid)
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()
