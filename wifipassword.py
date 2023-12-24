import subprocess
import wifipassword
name = subprocess.getoutput("netsh wlan show profile").replace("profiles on inter Wi_Fi:","").replace \
                           ("Group plicy profiles(read only)", "").replace \
                            ("---------------------------------------------------","").replace \
                           ("<None>","").replace("\n","").replace("user profiles","").replace \
                           ("---------","").replace("All user profile","").replace(":","")
wifilists = name.split()
for i in wifilists:
    a=subprocess.getoutput("wifipassword" +i)
    print(a)