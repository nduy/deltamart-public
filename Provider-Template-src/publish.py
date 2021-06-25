# HIS IS A MAIN PYTHON SCRIPT TEMPLATE FOF DATA STREAM PUBLISHER OF PROVIDER.

# A message to publishmust in formof valid JSON, should look like:
#{ "ProviderID":<Your  Identification>,"utc_time":<Your current time > , "data":{[content of your data msample]}}
#Where:
# *"ProviderID":(3 English uppercased Alphabetical letter  is the unique ideintification that Deltamart allocated to you
# *"utc_time"(yyy-mm-dd hh:mm:ss.ffff) is Your current time stamp in Universal Time Coordinated (UTC) or Greenwich Mean Time (GMT). It is detailed to Microsecond as a decimal number, zero-padded on the left(%ffff.
# * "data" (JSON object): the sensory data item.
#           For instance: (i) "data":2021.5" # Data as a number
#                          (ii) "data":"Welcome to Deltamart" #Data as a string
#                          (iii) "data": {"humidity":30, "temperature":21}
#                          (iv)" "data": {"brand": ["Ford", "BMW", "Fiat"]}"
#
# An example pf a published message is:
#       { "ProviderID":"TST","utc_time":"2021-06-17 07:36:55.4766" , "data":16}
#

#Import libraries, unquote what is applicable to you.
#Mandatory library
from config import * #Configurations
from plugin import packagemess # User-defined code
from lib import *
# Additional libraries
import paho.mqtt.client as mqtt
from datetime import datetime
import random
import string
from datetime import datetime
import time

INTERVAL =1/STREAM_RATE;
def print_hi():
    # Prin welcome words:
    print('====> Starting the publisher.')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Now publishing stream to {0},\n under topic name \" {1}\"\n with expected stream rate {2} smpls/sec\nEcoding_mode: {3}. '.format(DEST_IP,TOPIC_NAME,STREAM_RATE,ENCODING))

    #print(packagemess())

def on_connect(client, userdata, flags, rc):
    print("+++++++++ Connected to {0} with result code {1}".format(DEST_IP,str(rc)))

# Press the green button in the gutter to run the script.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
if __name__ == '__main__':
    print_hi();
#    for i in range(10):
#        print('Ecoding code: {0}  result: {1}'.format(i,encode(u'Nothing',i)))
    client=mqtt.Client()
    subclient = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(DEST_IP, 1883, 60)
    publishedCount=0;
    while True: # Continuously get data and publish in an infinte loop

        now = datetime.utcnow()
        current_time = now.strftime('\"%Y-%m-%d %H:%M:%S.%f\"')[:-3];
        # print(current_time)
        header='{ \"ProviderID\":\"'+PROVIDER_ID+ '\",\"utc_time\":'+current_time+ "\" "


        load =header+","+str(packagemess())+"}"
        # Do the encryption here. Set last parameter to 0 to apply NO encryption
        load =encode(load,ENCODING)


        client.publish(topic=TOPIC_NAME, payload=load);
        publishedCount=publishedCount+1
        if (publishedCount%20==0):
            iprint("Published {0} samples".format(publishedCount),2)
        iprint("=>Published:\n"+str(load),1);
        time.sleep(INTERVAL);# Sleep to ensure the stream rate
