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
import re
import os
import sys
import ast
import requests
from termcolor import colored
import pprint

# Global variables
BuyerID="DDN";  # A dummy user ID of the Buyer
RETRIEVED_TOPIC_NAME="";
RETRIEVED_DEST_IP="";
providID_pattern = re.compile('[A-Z0-9]{3}')

dcaID="";  # A dummy Data Collection Activity ID
dcaID_pattern = re.compile('[a-z0-9]{10}')
INTERVAL =1/STREAM_RATE;
def print_logo():
    # Use a breakpoint in the code line below to debug your script.
    with open('delta-logo-ascii-art.txt', 'r') as f:
        for line in f:
           print(colored(line.rstrip(),'blue'))

    print('====> Starting the publisher.')  # Press Ctrl+F8 to toggle the breakpoint.

    print('Now publishing stream to {0},\n under topic name \" {1}\"\n with expected stream rate {2} smpls/sec\nEcoding_mode: {3}. '.format(DEST_IP,TOPIC_NAME,STREAM_RATE,ENCODING))

    #print(packagemess())

def on_connect(client, userdata, flags, rc):
    print("+++++++++ Connected to {0} with result code {1}".format(DEST_IP,str(rc)))

# Press the green button in the gutter to run the script.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
if __name__ == '__main__':
    # GET USER INFORMATION
    print_logo();
    print(colored("      === DELTAMART DATA STREAM PROVIDER ===", 'red'))
    ProviderID = input("Enter YOUR User ID: ");
    PROVIDER_ID= ProviderID

    # Print out inputted data
    print("===========================")
    print("==You entered the following information")
    print("UserID:{0}".format(ProviderID));
    print("Now looking for establised Data Collection Activity for user {0}".format(ProviderID));

x = requests.get('http://dmart.hopto.org/dcaquery.php?ProviderID=' + ProviderID);
print("Now parse the results");
print(x.text)
dcaresult = ast.literal_eval(x.text);
print('There are ' + str(dcaresult['Count']) + " DCA established for you (as a PROVIDER):");
results = dcaresult['Results'];
for i in range(0, dcaresult['Count']):
    print(colored("((-- Index={0}--))".format(i), 'blue'))
    pprint.pprint(results[i])

    Sellecteddca_index = 0
    Sellecteddca_index = int(input(
        "Enter index of the Data Collection you want to recieve data (number from 0 to {0}:".format(
            dcaresult['Count'] - 1)));

RETRIEVED_TOPIC_NAME = dcaresult["Results"][Sellecteddca_index]["MQTTopic"];
RETRIEVED_DEST_IP = dcaresult["Results"][Sellecteddca_index]["IPAddress"];

#RETRIEVED_DEST_IP="52.19.248.189";
print("Publishing to : \"{0}\" under topic name:\"{1}\"".format(RETRIEVED_DEST_IP,RETRIEVED_TOPIC_NAME))
while (Sellecteddca_index < 0 or Sellecteddca_index > int(dcaresult['Count']) - 1):
    Sellecteddca_index = input(
        "[!]Incorrect input. Reenter index of the Data Collection you want to SEND data (number from 0 to {0}:".format(
            dcaresult['Count'] - 1));
print("\n({0})|{1}".format("Code","Method"))
print("\n({0})|{1}".format(0,"No Encoding"))
print("\n({0})|{1}".format(1," ASCII"))
print("\n({0})|{1}".format(2," UTF8"))
print("\n({0})|{1}".format(3," UTF16"))
print("\n({0})|{1}".format(4," UTF32"))
print("\n({0})|{1}".format(5," Base 16"))
print("\n({0})|{1}".format(6," Base32"))
print("\n({0})|{1}".format(7," Base64"))
print("\n({0})|{1}".format(8," Base85"))
client=mqtt.Client()
ENCODING_METHOD= int(input("How would you like your messages to be encoded?"))
"""
print("\n({0})-{1}".format(0,"No Encoding"))
print("\n({0})-{1}".format(1," ASCII"))
print("\n({0})-{1}".format(2," UTF8"))
print("\n({0})-{1}".format(3," UTF16"))
print("\n({0})-{1}".format(4," UTF32"))
print("\n({0})-{1}".format(5," Base 16"))
print("\n({0})-{1}".format(6," Base32"))
print("\n({0})-{1}".format(7," Base64"))
print("\n({0})-{1}".format(8," Base85"))
"""
client=mqtt.Client()
subclient = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(RETRIEVED_DEST_IP, 1883, 60)
publishedCount=0;
while True: # Continuously get data and publish in an infinte loop

    now = datetime.utcnow()
    current_time = now.strftime('\"%Y-%m-%d %H:%M:%S.%f\"')[:-3];
    # print(current_time)
    header='{ \"ProviderID\":\"'+PROVIDER_ID+ '\",\"utc_time\":'+current_time+ "\" "


    load =header+","+str(packagemess())+"}"
    # Do the encryption here. Set last parameter to 0 to apply NO encryption
    load =encode(load,ENCODING_METHOD)


    client.publish(topic=RETRIEVED_TOPIC_NAME, payload=load);
    publishedCount=publishedCount+1
    if (publishedCount%20==0):
        iprint("Published {0} samples".format(publishedCount),2)
    iprint("=>Published:\n"+str(load),1);
    time.sleep(INTERVAL);# Sleep to ensure the stream rate
