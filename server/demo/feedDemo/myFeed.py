# myFeed.py
# upload, delete, change it.
# new comment, like inform
# get comment, like list of my feed.


# TODO: those variable will become data menber of BaseHandler.
config = ConfigParser.ConfigParser()
config.readfp(open('../../common/conf/key.ini'))
aes_key=config.get('app','secret')
appkey=config.get('app','appkey')
prefix=config.get('url','prefix')

class UploadHandler(object):
    def upload(self,access_token,json):
        
