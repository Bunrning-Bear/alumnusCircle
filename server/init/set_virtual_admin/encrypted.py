# encrypted_data.py
# -*- coding: utf-8 -*-
import json
import struct
import base64
from Crypto.Cipher import AES



class prpcrypt(object):
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
        self.iv = self.key[:16]

    def encrypt(self, text):
            cryptor = AES.new(self.key, self.mode, self.iv)
            length = 32
            count = len(text)           
            amount = length - (count % length)
            if amount == 0:
                amount = length
            pad_chr = chr(amount & 0xFF)
            new_text = text + (pad_chr * amount)
            ciphertext = cryptor.encrypt(new_text)
            return ciphertext


#APPkey：579c674c67e58eebcb00275a
# https://rest.wsq.umeng.com/api1?ak={579c674c67e58eebcb00275a}&access_token={access_token}
#https://rest.wsq.umeng.com/0/get_access_token?ak=579c674c67e58eebcb00275a
#&encrypted_data=eYAA/8twLpOlgJFqC/X0H+u3P5OY1mPJAZB/19vyHDo=
# curl -H 'Content-type: application/x-www-form-urlencoded' -XPOST -d 'encrypted_data=nftaDxqpEZ/BPjNqbEmzKoFelU73C8Kw+oZJrx73qUUfB9VEzseI8QBSjUMj2/B4rG/Pbg5T5w/hFVjmHlrAs9Ffh6SIwdJiorBc7Reb/oOXE0GHC8uzEcR3MpTzepRk0h3R49j8TaXbp9cFU8dT7+zH5SetxBFJou0yB/E8sXA=' https://rest.wsq.umeng.com/0/get_access_token?ak=579c674c67e58eebcb00275a
"""
if __name__ == '__main__':
    #data = '{"source_uid": "123312", "source": "qq", "source_name": "hello"}';
   # data = json.dumps({}) # JSON 格式字符串
    data = json.dumps({"user_info": {"name": "test1","icon_url": "http://umeng.com/1.jpg"},"source_uid": "4124","source": "self_account"}) # JSON 格式字符串
    print data
    data = struct.pack(">I",len(data)) + data
    aes_key = '2f5c5f18353cdd1b56e077c19bd3ebc5'
    data = prpcrypt(aes_key).encrypt(data)
    data = base64.b64encode( data )
    print data
"""
"""
https://rest.wsq.umeng.com/0/get_access_token?ak=579c674c67e58eebcb00275a

Host: rest.wsq.umeng.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/css,*/*;q=0.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Referer: https://rest.wsq.umeng.com/0/get_access_token?ak=579c674c67e58eebcb00275a&encrypted_data=nftaDxqpEZ/BPjNqbEmzKoFelU73C8Kw+oZJrx73qUUfB9VEzseI8QBSjUMj2/B4rG/Pbg5T5w/hFVjmHlrAs9Ffh6SIwdJiorBc7Reb/oOXE0GHC8uzEcR3MpTzepRk0h3R49j8TaXbp9cFU8dT7+zH5SetxBFJou0yB/E8sXA=
Content-Length: 187
Cookie: l=AoWF88n4iByj8ILEb79mcLPAtcq-OTnM; isg=AkhIJzeyi_e2S-dzpWKw09UMGr99D6z7AckYWgL470Ou3epHqgB2inffMw9X; Hm_lvt_4f8b18c5911db1a4c1cd2d91b83b0aa5=1469847446,1469867638,1469867764,1469876239; cna=tedwDwYYBzUCAWuyw9FHgXP0; umengplus_name=zpcxh95%40outlook.com; umplusuuid=4648e17a75fb884fc4aa52738ae3f819; umplusappid=umeng_wsq; __ufrom=https://wsq.umeng.com/communities/pro/home/; Hm_lpvt_4f8b18c5911db1a4c1cd2d91b83b0aa5=1469876248; pgv_pvi=5047878656; pgv_si=s4353898496; _ga=GA1.2.1382108315.1469868626; csrftoken=8VwJrqLZlDqwa3PFIeB3InDsi7ncOFJx; cn_a61627694930aa9c80cf_dplus=%7B%22distinct_id%22%3A%20%2215639bbf20442-03ea8e84477e8f-72226750-100200-15639bbf205bd%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201469876228%2C%22initial_view_time%22%3A%20%221469846722%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPa4zFHPR0vo-CVWqIV6qecx-qm5kBcor7BPqWy7mSu7%26wd%3D%26eqid%3Dbeeff1120022a36500000005579c1787%22%2C%22initial_referrer_domain%22%3A%20%22www.baidu.com%22%2C%22%24recent_outside_referrer%22%3A%20%22www.baidu.com%22%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201469876228%2C%22%E7%94%A8%E6%88%B7%E5%90%8D%22%3A%20%22zpcxh95%40outlook.com%22%7D; cn_f7169cbd4377cl2a77d3_dplus=%7B%22distinct_id%22%3A%20%2215639bc0624449-0d6806bc24d994-72226750-100200-15639bc06256e%22%2C%22%24_sessionid%22%3A%201%2C%22%24_sessionTime%22%3A%201469876247%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201469876247%2C%22initial_view_time%22%3A%20%221469842625%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fwww.umeng.com%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.umeng.com%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D; _gat=1
Connection: keep-alive

encrypted_data=3rE0y8Ir0aINUBwGnacHfAbBh+F4GMjAA6i3BTTmIGmD7SNJ7sc5hQzSlG02TYPQww2GCEbqrf7nhoLxY/qjpxHFt3wR6UEOq2/yEMnbGjOd/murkGiGuDAhXLWTCFDsAjYiNyCenfJ0OIV7mzVk03N0D6uPUB4KK7cRw8ViVsY=
access_token_app = 91ecfda554562b067956f6a8ae927d288dd96616acf8f6427bf95cb267bb069d52000b21b8ddf5142771f3bb3ab689eeab87d99dc23889add8551ea4731efa6a

when:data = json.dumps({})
access_token_app:"a83b30a4979ed930a590b9ea08a1e484441e0af2820dc9aa9d56412cc651a7e085957e702f559fdda307492c09ef26f02b84a51310c2225e4c47383ea1f8254a"

"""