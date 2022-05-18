import os
lib = input("""
[1] Download lib & update
[2] pass

[+] Please Choice >> """)

if lib == "1":
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

import requests
import random
import secrets
from time import sleep
from user_agent import generate_user_agent

banner = ("""
[!] Free By : Tekky#9999
    _                             _   __  __       _             
   / \   ___ ___ ___  _   _ _ __ | |_|  \/  | __ _| | _____ _ __ 
  / _ \ / __/ __/ _ \| | | | '_ \| __| |\/| |/ _` | |/ / _ \ '__|
 / ___ \ (_| (_| (_) | |_| | | | | |_| |  | | (_| |   <  __/ |   
/_/   \_\___\___\___/ \__,_|_| |_|\__|_|  |_|\__,_|_|\_\___|_|                       
""")
print(banner)
print('====================================')

def Make():
    while 1:
        idd    = 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
        r      = requests.Session()
        cookie = secrets.token_hex(8)*2
        chars  = 'abcdefghijklmnopqrstuvwxyz123456789'
        myID   = input('[+] Enter Your Telegram ID : ')
        if myID == "":
            print('[!] Error Telegram ID')
            exit()
        else:
            token   = input('[+] Enter token Bot Telegram : ')
            pass
        phone  = input('[+] Enter Your Phone Number : ')
        if phone == "":
            print('[!] Error Phone Number')
            exit()
        else:
            pass
        userr  = ""
        passs  = ""
        for x in range(0,3):
            userr_char = random.choice(chars)
            userr      = userr + userr_char
        for i in range(0,8):
            passs_char = random.choice(chars)
            passs      = passs + passs_char   
        paas   = passs
        user   = (f'zpoc_tools{userr}')
        name   = 'By @old_zpoc'
        url1   = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        url2   = 'https://www.instagram.com/accounts/send_signup_sms_code_ajax/'
        url3   = 'https://www.instagram.com/accounts/web_create_ajax/'
        head   = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : generate_user_agent(),
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
        }

        data1   = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'client_id': idd,
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'fals'
        }
        data2   = {
            'client_id': idd,
            'phone_number': phone,
            'phone_id': '',
            'big_blue_token': ''
        }
        Make_Acc1 = r.post(url1,headers=head,data=data1)
        Make_Acc2 = r.post(url2,headers=head,data=data2)
        if 'Looks like your phone number may be incorrect.' in Make_Acc2.text:
            print('[!] Error Phone Number')
            exit()
        elif 'Please wait a few minutes before you try again.' in Make_Acc2.text:
            print('[!] Please wait a few Minutes')
            exit()
        elif 'true' in Make_Acc2.text:
            print('[-] The SMS has been sent successfully')
            pass
        else:
            print('[!] Error ..')
            exit()
        code = input('[+] Enter The Code : ')
        data3 = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'sms_code': code,
            'client_id': idd,
            'seamless_login_enabled': '1',
            'tos_version': 'row'
        }
        Make_Acc3 = r.post(url3,headers=head,data=data3)
        if "That code isn't valid." in Make_Acc3.text:
            print("[!] That code isn't valid")
            exit()
        elif 'true' in Make_Acc3.text:
            print("[-] Done Created Account")
            pass
        elif "checkpoint_required" in Make_Acc3.text:
            print('[!] Done, checkpoint required')
            pass
        else:
            print(Make_Acc3.text)
            print('[!] Error ..')
            exit()
        Account = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=⌯ Instagram Fake Account  \n⌯ User : {}\n⌯ Pass : {}\n⌯ by : @old_zpoc'.format(token,myID,user,paas)
        r.get(Account)
Make()
