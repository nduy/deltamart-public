"""
Self-modifiedLibrary for clients
"""

import binascii
import base64
from config import  VERBOSE as VERB_LEVEL
def encode(string,scheme_code):
    """

Params:
- string (bytes) input/original string
-scheme_code (integer0+: encoding scheme codes
    """
    if (scheme_code==0): # No Encoding
        return string;
    elif (scheme_code==1):    #ASCII
        return string.encode('ascii')
    elif (scheme_code==2):    #UTF8
        return string.encode("utf-8")
    elif (scheme_code==3):    #UTF16
        return string.encode("utf-16")
    elif (scheme_code==4):    #UTF16
        return binascii.hexlify(bytes(string, 'utf-8'))
    elif (scheme_code==5):    #Base 16
         return base64.b16encode(bytes(string, 'utf-8'))
    elif (scheme_code==6):    #Base 32
        return base64.b32encode(bytes(string, 'utf-8'))
    elif (scheme_code==7):    #Base 64
        return base64.b64encode(bytes(string))

    else:
        return string

def iprint(to_printtext,verb):
    if (verb<=VERB_LEVEL):
        print(to_printtext)
