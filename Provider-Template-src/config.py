
# This is configuration scripts contains constant regulating the data stream Publishing.

# Provider MQTT hostname or IP
DEST_IP="52.19.248.189";

#Name of the MQTT topic under which the stream will be published
TOPIC_NAME="interesting0topic1"

#Expected stream rate sample per second
STREAM_RATE=2;

TEST = True;
# SProvider-side data enoding. None by default
#See page 8 of Collectability Cheatsheet
#Value: Natural number (including Zero-0)
ENCODING = 0;
"""
    @ 0:  No Encoding - Plain-text
    @ 1 :    #ASCII
    @ 2 :    #UTF8
    @ 3 :    #UTF16
    @ 4 :    #UTF16
    @ 5 :    #Base 16
    @ 6 :    #Base 32
    @ 7 :    #Base 64
    @ 8 :    #Base 85
      
"""

# ID of the Provider (you)
PROVIDER_ID="TST"
#Verbal level 1,2,3.
VERBOSE = 3

# LIMITS
