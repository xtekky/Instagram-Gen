import requests
import random
import json
import time
import re
import string
import curlify
import httpx
from pystyle import Col


class Email:
    def __init__(self, proxy: str= None, timeout: int=15) -> None:
        self.session = httpx.Client(headers={'content-type': 'application/json'}, timeout=timeout, proxies=proxy)
        self.base_url = 'https://api.mail.gw'
    
    def get_domains(self) -> list:
        domains: list = []
        
        for item in self.session.get(f'{self.base_url}/domains').json()['hydra:member']:
            domains.append(item['domain'])

        return domains

    def get_mail(self, name: str = ''.join(random.choice(string.ascii_lowercase) for _ in range(15)), password: str= None, domain: str = None) -> str:
        mail: str =  f'{name}@{domain if domain != None else self.get_domains()[0]}'
        response: int = self.session.post(f'{self.base_url}/accounts', json={'address': mail, 'password': mail}).status_code
        
        try:
            if response == 201:
                token = self.session.post(f'{self.base_url}/token', json={'address': mail, 'password': mail if password == None else password}).json()['token']
                self.session.headers['authorization'] = f'Bearer {token}'
                return mail
        except:
            return 'Email creation error.'
    
    def fetch_inbox(self):
        response = self.session.get(f'{self.base_url}/messages').json()['hydra:member']
        return response
    
    def get_message(self, message_id: str):
        response = self.session.get(f'{self.base_url}/messages/{message_id}').json()
        return response
    
    def get_message_content(self, message_id: str):
        response = self.get_message(message_id)['text']
        return response

class Utils:
    @staticmethod
    def base36(x: int, base: int) -> str:
        base_36 = string.digits + string.ascii_letters
        
        if x < 0:
            sign = -1
        elif x == 0:
            return base_36[0]
        else:
            sign = 1
        x *= sign
        digits = []
        while x:
            digits.append(base_36[x % base])
            x = x // base
        if sign < 0:
            digits.append('-')
        digits.reverse()
        return "".join(digits)
    
    @staticmethod
    def cookie_to_headers(cookies: dict) -> dict:
        cookies_str = ""
        for i in cookies.items():
            cookies_str = cookies_str + i[0] + "=" + i[1] + "; "
        return cookies_str[:len(cookies_str) - 2]
    
    @staticmethod
    def sprint(x: str, msg: str) -> None:
        return '%s{%s%s%s}%s %s[%s%s%s]%s' % (
            Col.purple, Col.reset,
            x, 
            Col.purple, Col.reset,
            Col.blue, Col.reset,
            msg,
            Col.blue, Col.reset
        )

class Instagram:
    def __init__(self) -> None:
        self.mid          = None
        self.crsf         = None
        self.asbd_id      = None
        self.fbapp_id     = None
        self.device_id    = None
        self.rollout_hash = None

    @staticmethod
    def __x_mid() -> str:
        return "".join(
            [
                Utils.base36(
                        random.randint(2**29, 2**32), 36
                    ) for _ in range(8)
                ]
        )
    
    def __base_headers(self, session: requests.Session, addon = {}) -> dict:
        __base_headers =  {
            'authority': 'www.instagram.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            "x-ig-www-claim": "0",
            
            "x-mid": self.mid,
            "x-instagram-ajax": self.rollout_hash,
            "x-asbd-id": self.asbd_id,
            "x-csrftoken": self.crsf,
            "x-ig-app-id": self.fbapp_id,
            "cookie": Utils.cookie_to_headers(session.cookies.get_dict())
        }
        
        __base_headers.update(addon)
        
        return __base_headers
    
    def __get_headers(self, session: requests.Session)-> None:
        headers = {'authority':'www.instagram.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'en','cache-control':'no-cache','pragma':'no-cache','sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'document','sec-fetch-mode':'navigate','sec-fetch-site':'none','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',"x-ig-www-claim":"0"}

        libcommons_hash = re.findall(
            r'(?<=ConsumerLibCommons\.js\/)[a-z0-9]{12}', 
            session.get(
                url = 'https://www.instagram.com/', 
                headers=headers
            ).text
        )[0]

        res = session.get(
            url = f'https://www.instagram.com/static/bundles/es6/ConsumerLibCommons.js/{libcommons_hash}.js', 
            headers=headers
        ).text

        self.asbd_id  = re.findall(r"ASBD_ID='(\d+)'", res)[0]
        self.fbapp_id = re.findall(r"AppId='(\d+)'", res)[0]

        data =  session.get(
            url = (
                "https://"
                + "www.instagram.com"
            ),
            headers = headers
        ).text

        self.device_id    = re.findall(r'(?<="device_id":")[A-Z0-9\-]{35,36}', data)[0]
        self.crsf         = re.findall(r'(?<="csrf_token":")[a-zA-Z0-9]{31,32}', data)[0]
        self.rollout_hash = re.findall(r'(?<="rollout_hash":")[a-z0-9]{11,12}', data)[0]
        self.mid          = Instagram.__x_mid()
        
        session.cookies["csrftoken"] = self.crsf
        session.cookies["mid"]       = self.mid
        session.cookies["ig_did"]    = self.rollout_hash
        
        return session.cookies.get_dict()
    
    
    def __init_create(self, session: requests.Session, password: str, email: str, username: str, first_name: str) -> None:

        payload = {
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
            "email": email,
            "username": username,
            "first_name": first_name,
            "client_id": self.mid,
            "seamless_login_enabled": "1",
            "opt_into_one_tap": "false"
        }

        response = session.post(
            url  = "https://www.instagram.com/accounts/web_create_ajax/attempt/", 
            data = payload, 
            headers = self.__base_headers(session)
        )
        
        if 'Try Again Later' in response.text:
            return False
            
        elif response.json()["dryrun_passed"] is True or response.json()["dryrun_passed"] == 'true':
            return True
        
        elif "username isn't" in response.text:
            return False
            
        else:
            True
        
    def main(self) -> None:
        with requests.Session() as session:
            headers = self.__get_headers(session)
            print(Utils.sprint("*", headers))
            x = self.__init_create(session, "erfeferf", "zfzoeignzgz@gmail.com", "roinerfe3", "erfefe")
            print(Utils.sprint("*", x))
            

if __name__ == '__main__':
    Instagram().main()
    # api = Email()

    # email = api.get_mail()
    # print(f'Your temp-mail: {email}')
    # code = None
    # while True:
    #     time.sleep(3)
    #     for mail in api.fetch_inbox():
    #         content = api.get_message_content(mail['id'])
    #         code = re.findall(r'(\d{6,6})', content)[0]
            
    #         if code:
    #             print(f"code: {code}")
    #             break
    #     if code:
    #         break
