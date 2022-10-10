from pystyle import Col
from temp_mail import TempEmail
from utils import Utils

import json
import random
import re
import requests
import time


class Instagram:
    def __init__(self, proxy = None) -> None:
        self.mid          = None
        self.crsf         = None
        self.asbd_id      = None
        self.fbapp_id     = None
        self.device_id    = None
        self.rollout_hash = None
        self.proxies      = {'http': f'http://{proxy}', 'https': f'http://{proxy}'} if proxy != None else None

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
    
    def __init_session(self, session: requests.Session)-> dict:
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
            headers = headers,
            proxies=self.proxies
        ).text

        self.device_id    = re.findall(r'(?<="device_id":")[A-Z0-9\-]{35,36}', data)[0]
        self.crsf         = re.findall(r'(?<="csrf_token":")[a-zA-Z0-9]{31,32}', data)[0]
        self.rollout_hash = re.findall(r'(?<="rollout_hash":")[a-z0-9]{11,12}', data)[0]
        self.mid          = Instagram.__x_mid()
        
        session.cookies["csrftoken"] = self.crsf
        session.cookies["mid"]       = self.mid
        session.cookies["ig_did"]    = self.rollout_hash
        
        return session.cookies.get_dict()
    
    
    def __init_create(self, session: requests.Session, password: str, username: str, first_name: str) -> bool:

        payload = {
            "enc_password": Utils.encrypt_password(password),
            "email": "eggrrrrferg@gmail.com",
            "username": username,
            "first_name": first_name,
            "client_id": self.mid,
            "seamless_login_enabled": "1",
            "opt_into_one_tap": "false"
        }
        response = session.post(
            url  = "https://www.instagram.com/accounts/web_create_ajax/attempt/", 
            data = payload, 
            headers = self.__base_headers(session),
            proxies = self.proxies
        )
        print(response.text)

        if 'Try Again Later' in response.text:
            return False
            
        elif response.json()["dryrun_passed"] is True or response.json()["dryrun_passed"] == 'true':
            return True
        
        elif "username isn't" in response.text:
            return False
            
        else:
            True
            
    def __create_account(self, session: requests.Session, password: str, email: str, username: str, first_name: str, signup_code: str) -> bool:
        payload = {
            "enc_password": Utils.encrypt_password(password),
            "email": email,
            "username": username,
            "first_name": first_name,
            "month": str(random.randint(1, 12)),
            "day": str(random.randint(1, 27)),
            "year": str(random.randint(1970, 2000)),
            "client_id": self.mid,
            "seamless_login_enabled": "1",
            "tos_version": "eu",
            "force_sign_up_code": signup_code
        }
        
        return session.post(
            url  = "https://www.instagram.com/accounts/web_create_ajax/", 
            data = payload, 
            headers = self.__base_headers(session),
            proxies = self.proxies
        )
    
    def __verify_code(self, session: requests.Session, email: str, code: str) -> str:

        payload = {
            "code": code,
            "device_id": self.mid,
            "email": email
        }
        
        response = session.post(
            url  = "https://i.instagram.com/api/v1/accounts/check_confirmation_code/", 
            data = payload, 
            headers = self.__base_headers(session),
            proxies = self.proxies
        )

        print(response.text)
        __signup_code = response.json()["signup_code"]
        
        return __signup_code
    
    def __verify_mail(self, session: requests.Session) -> (dict and json):
        __email_client = TempEmail()
        __email = __email_client.get_mail()
        
        print(__email)
        
        payload = {
            "device_id": self.mid,
            "email": __email
        }
        
        response = session.post(
            url  = "https://i.instagram.com/api/v1/accounts/send_verify_email/", 
            data = payload, 
            headers = self.__base_headers(session),
            proxies = self.proxies
        )
        print(response.json())
        if response.json()['email_sent'] != True:
            print(response.json())
            return False
        
        __veri_code = None
        while True:
            time.sleep(1)
            for mail in __email_client.fetch_inbox():
                content = __email_client.get_message_content(mail['id'])
                __veri_code = re.findall(r'(\d{6,6})', content)[0]
                if __veri_code:
                    print(Utils.sprint("*", f"Code: {Col.blue}{__veri_code}"))
                    break
            if __veri_code:
                break
        
        __signup_code = self.__verify_code(session, __email, __veri_code)
        return __email, __signup_code
        

    def main(self) -> None:
        with requests.Session() as session:
            self.__init_session(session)
            
            first_name, username, password = Utils().get_userinfo()
            
            __init_create = self.__init_create(
                session    = session, 
                password   = password,
                username   = username,
                first_name = first_name
            )
            print(Utils.sprint("*", __init_create))
            
            if __init_create is True:
                __email, __signup_code = self.__verify_mail(session)
                print(__email)
                print(__signup_code)
            
                response: requests.Response = self.__create_account(
                    session     = session,
                    password    = password,
                    email       = __email,
                    username    = username, 
                    first_name  = first_name,
                    signup_code =__signup_code
                )
                
                print(response.text)

if __name__ == '__main__':
    Instagram().main()
