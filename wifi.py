#############################################################
# copyright (c) 2015 Mahmoud Elshobaky                      #
# Email :Mahmoud.Elshobaky@Gmail.com                        #
# GitHub : https://github.com/elshobaky                     #
# License : GPL v3                                          #
#############################################################

import subprocess as sp
import os, sys, re

get_c = """
regsvr32 hnetcfg.dll
$m = New-Object -ComObject HNetCfg.HNetShare
$m.EnumEveryConnection |% { $m.NetConnectionProps.Invoke($_) }
"""

def check_support():
	i = sp.Popen('netsh wlan show drivers',shell=True,
		            stdout=sp.PIPE,
		            stderr=sp.PIPE)
	out, err = i.communicate()
	res = re.findall(r'[A-Z]*[a-z]*(?: [a-z]+)* *\: .*',out)
	info = {}
	for i in res :
		key = re.findall(r'[A-Z]*[a-z]*(?: [a-z]+)*',i)[0]
		value = i[i.find(':')+2:]
		info[key] = value
	if info['Hosted network supported'] == 'Yes\r':
		return True
	else :
		return False

def start_wifi():
	output = sp.call("netsh wlan start hostednetwork")
	return output, "WiFi hotspot started"



def stop_wifi():
	output = sp.call("netsh wlan stop hostednetwork")
	return output, "WiFi hotspot stopped"

def create_new(ssid, key):
	if not ssid or ssid=="" :
		ssid="melsho"
	if not key or key=="":
		key ="melsho12345"
	command = "netsh wlan set hostednetwork mode=allow ssid="+ssid+" key="+key
	output = sp.call(command)
	start_wifi()
	return output, "WiFi hotspot created \nname=%s\npassword=%s"%(ssid,key)

def show_wifi():
	info = sp.Popen('netsh wlan show hostednetwork',shell=True,
		            stdout=sp.PIPE,
		            stderr=sp.PIPE)
	out, err = info.communicate()
	errcode = info.returncode
	res = re.findall(r'[A-Z]*[a-z]*(?: [a-z]+)* *\: .*',out)
	info = {}
	for i in res :
		key = re.findall(r'[A-Z]*[a-z]*(?: [a-z]+)*',i)[0]
		value = i[i.find(':')+2:]
		info[key] = value
	return info



#print check_support()
#x = show_wifi()
#print x['Number of clients']

# print sp.call("regsvr32 hnetcfg.dll")
#p = sp.Popen(["powershell.exe", 
#             get_c], 
#            stdout=sys.stdout)
#print p.communicate()
#p =  sp.check_output(["powershell.exe", 
#             get_c],cwd=os.getcwd())
#print p.wait()
#start_wifi()



