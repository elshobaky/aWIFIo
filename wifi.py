

import subprocess as sp
import os, sys

get_c = """
regsvr32 hnetcfg.dll
$m = New-Object -ComObject HNetCfg.HNetShare
$m.EnumEveryConnection |% { $m.NetConnectionProps.Invoke($_) }
"""


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
	return output, "WiFi hotspot created name=%s password=%s"%(ssid,key)
# print sp.call("regsvr32 hnetcfg.dll")
#p = sp.Popen(["powershell.exe", 
#             get_c], 
#            stdout=sys.stdout)
#print p.communicate()
#p =  sp.check_output(["powershell.exe", 
#             get_c],cwd=os.getcwd())
#print p.wait()
#start_wifi()

def get_current():
	info = sp.call("netsh wlan show hostednetwork")
	print info

