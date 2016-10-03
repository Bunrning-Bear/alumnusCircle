#!/usr/bin/env python
# coding=utf-8
#Author ChenXionghui
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


def set_encrypt(aes_key,data):
    data = json.dumps(data)
    data = struct.pack(">I",len(data)) + data
    cryptedData = prpcrypt(aes_key).encrypt(data)
    cryptedData = base64.b64encode( cryptedData )
    return cryptedData
