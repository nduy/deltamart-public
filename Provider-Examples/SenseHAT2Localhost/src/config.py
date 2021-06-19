
# This is configuration scripts contains constant regulating the data stream Publishing.

# Provider MQTT hostname or IP
DEST_IP="localhost";

#Name of the MQTT topic under which the stream will be published
TOPIC_NAME="interesting0topic1";

#Expected stream rate sample per second
STREAM_RATE=3;

TEST = False;
# SProvider-side data enoding. None by default
#See page 8 of Collectability Cheatsheet
#Value: Natural number (including Zero-0)
ENCODING=0;

# ID of the Provider (you)
PROVIDER_ID="TST"
#Verbal level 1,2,3.
VERBOSE = 3

# LIMITS
