# opt_circle.py
# Author ChenXionghui
import tornado.web
import tornado.gen

from handler.circle.circle import TopicHandler
from handler import request
from common.lib.to_list import custom_list_to_list


class CircleApplyHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(CircleApplyHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/fans'
        self.methodUsed = 'GET'
        self.requestName = 'circle_apply'

    @request.authenticated('circle_apply')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    # @request.throwBaseException
    def post(self):
        circle_id = self.get_argument('circle_id')
        circle_name = self.get_argument('circle_name')
        circle_url = self.get_argument('circle_url')
        circle_id = self.circle_module.get_cid_from_umeng_id(circle_id)
        reason = self.get_argument('reason')
        uid = self.get_secure_cookie('uid')
        creator_id = self.get_argument('creator_id')
        username = self._user_detail_module.get_name_from_uid(uid)
        # create message to all of admin and creators
        mid = self.message.create_message(self.message.TYPE['apply circle'],
                                          circle_id=circle_id, circle_name=circle_name, circle_url=circle_url, reason=reason, uid=uid, username=username)
        # [todo] this message should send to all of admin and creator.
        self.message.deal_message_to_one(mid, creator_id)
        code = self.return_code_process(0)
        message = "set apply successfully!!"
        self.return_to_client(code, message)
        self.finish()


class LeaveCircleHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(LeaveCircleHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/unfocus'
        self.methodUsed = 'DELETE'
        self.requestName = 'leave circle'

    @request.authenticated('circle_apply')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """
            this is umeng cid.: circle_id
        """
        circle_id = self.get_argument('umeng_circle_id')
        Data = {'topic_id': circle_id}
        uid = self.get_secure_cookie('uid')
        cid = self.circle_module.get_cid_from_umeng_id(circle_id)
        my_circle_list = self.user_detail_module.get_my_circle_list(uid)
        my_circle_list = custom_list_to_list(my_circle_list)
        # admin_circle_list =
        create_circle_list = self.user_detail_module.get_create_circle_list(
            uid)
        create_circle_list = custom_list_to_list(create_circle_list)
        def circle_filter(self, list_unit):
            if list_unit != cid:
                return cid
        my_circle_list = filter(circle_filter, my_circle_list)
        create_circle_list = filter(circle_filter, create_circle_list)
        string_my_circle_list = '_'
        string_create_circle_list = '_'
        for value in my_circle_list:
            string_my_circle_list += str(value) + '_'

        for value in create_circle_list:
            string_create_circle_list += str(value) + '_'
        self.user_detail_module.leave_circle(
            string_my_circle_list, string_create_circle_list, uid)
        access_token = self.get_redis_dict_access_token(uid)
        code, message, Data = yield self.Umeng_asyn_request(access_token, Data)
        self.return_to_client(code, message, Data)
        self.finish()


class DetailCircleHadnler(TopicHandler):
    pass
