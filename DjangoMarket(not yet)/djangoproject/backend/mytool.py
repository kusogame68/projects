# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:53:01 2023

@author: Johnson
"""

import hashlib
import requests

class Password_Encryption:
    def __str__(self):
        string='這是一個sha256加密function'
        return string
    
    def encryption(self,password=None):
        password=password
        password_bytes=password.encode('utf-8')
        ascii_password=hashlib.sha256(password_bytes).hexdigest()
        return password,ascii_password

