#!/usr/bin/env python
# coding=utf-8
# index.py
#!/usr/bin/env python
# coding=utf-8
import json

from base import BaseHandler

class IndexHandler(BaseHandler):
    """
     Client will access IndexHandler when he open his app.
     Server will set a _xsrf as cookie to client.
     All of access after it, client should post _xsrf as a parameter to server,
     tornado will check it automatic.
    """
    def get(self):
        try:
            Data = {"_xsrf":self.xsrf_token}
            Data = json.dumps(Data)
            result = json.dumps({"code": "100","message":"success set cookie","Data":Data})
            self.write(result)
        except Exception, e:
            result = json.dumps({"code": "101","message":"fail set cookie","Data":"{}"})
            self.write(result)
            raise