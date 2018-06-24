"""
This script will create an Organization, a network for the Organization
and add a number of devices for the Network created.
The script will print the response code for the devices added.
"""

import requests
import json
import sys


api_key = sys.argv[1]
headers = {
    "x-cisco-meraki-api-key": api_key,
    "content-type": "application/json"
    }
payload = '{"name":"'+name+'"}'
base_url = "https://dashboard.meraki.com/api/v0/organizations"
name = raw_input("Please enter the name of the Organization: ")
network = raw_input("Please enter the name of the network: ")
devices_list = []
number = int(raw_input("Please enter the number of devices to be added: "))

#Create a list of devices
for i in range(number):
    device = raw_input("Please introduce the serial number "+str(i+1)+": ")
    devices_list.append(device)

#Get the Organization ID
response = requests.request("POST", url=base_url, data=payload, headers=headers)
org_id = response.json()['id']

#Get the network ID
payload_network = '{"name":"'+network+'", "type":"wireless appliance"}'
url = base_url+"/"+str(org_id)+"/networks"
response1 = requests.request("POST", url=url, data=payload_network, headers=headers)
net_id = response1.json()['id']

#Add the devices to the network ID, by using POST method
url = "https://api.meraki.com/api/v0/networks/"+str(net_id)+"/devices/claim"
for i in devices_list:
    payload_device = '{"serial": "'+i+'"}'
    response = requests.request("POST", url=url, data=payload_device, headers=headers)
    print response



