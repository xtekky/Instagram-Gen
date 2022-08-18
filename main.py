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
        self.base_url = 'https://api.mail.tm'
    
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
    
    @staticmethod
    def encrypt_password(password: str) -> str:
        # data = requests.get("https://www.instagram.com/data/shared_data/").json()["encryption"]
        
        # public_key = data["public_key"]
        # key_id = data["key_id"]
        # version = data["version"]
        return f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
    
    @staticmethod
    def get_userinfo() -> list:
        names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila', 'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail', 'Sofia', 'Avery', 'Scarlett', 'Emily', 'Aria', 'Penelope', 'Chloe', 'Layla', 'Mila', 'Nora', 'Hazel', 'Madison', 'Ellie', 'Lily', 'Nova', 'Isla', 'Grace', 'Violet', 'Aurora', 'Riley', 'Zoey', 'Willow', 'Emilia', 'Stella', 'Zoe', 'Victoria', 'Hannah', 'Addison', 'Leah', 'Lucy', 'Eliana', 'Ivy', 'Everly', 'Lillian', 'Paisley', 'Elena', 'Naomi', 'Maya', 'Natalie', 'Kinsley', 'Delilah', 'Claire', 'Audrey', 'Aaliyah', 'Ruby', 'Brooklyn', 'Alice', 'Aubrey', 'Autumn', 'Leilani', 'Savannah', 'Valentina', 'Kennedy', 'Madelyn', 'Josephine', 'Bella', 'Skylar', 'Genesis', 'Sophie', 'Hailey', 'Sadie', 'Natalia', 'Quinn', 'Caroline', 'Allison', 'Gabriella', 'Anna', 'Serenity', 'Nevaeh', 'Cora', 'Ariana', 'Emery', 'Lydia', 'Jade', 'Sarah', 'Eva', 'Adeline', 'Madeline', 'Piper', 'Rylee', 'Athena', 'Peyton', 'Everleigh', 'Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Theodore', 'Jack', 'Levi', 'Alexander', 'Jackson', 'Mateo', 'Daniel', 'Michael', 'Mason', 'Sebastian', 'Ethan', 'Logan', 'Owen', 'Samuel', 'Jacob', 'Asher', 'Aiden', 'John', 'Joseph', 'Wyatt', 'David', 'Leo', 'Luke', 'Julian', 'Hudson', 'Grayson', 'Matthew', 'Ezra', 'Gabriel', 'Carter', 'Isaac', 'Jayden', 'Luca', 'Anthony', 'Dylan', 'Lincoln', 'Thomas', 'Maverick', 'Elias', 'Josiah', 'Charles', 'Caleb', 'Christopher', 'Ezekiel', 'Miles', 'Jaxon', 'Isaiah', 'Andrew', 'Joshua', 'Nathan', 'Nolan', 'Adrian', 'Cameron', 'Santiago', 'Eli', 'Aaron', 'Ryan', 'Angel', 'Cooper', 'Waylon', 'Easton', 'Kai', 'Christian', 'Landon', 'Colton', 'Roman', 'Axel', 'Brooks', 'Jonathan', 'Robert', 'Jameson', 'Ian', 'Everett', 'Greyson', 'Wesley', 'Jeremiah', 'Hunter', 'Leonardo', 'Jordan', 'Jose', 'Bennett', 'Silas', 'Nicholas', 'Parker', 'Beau', 'Weston', 'Austin', 'Connor', 'Carson', 'Dominic', 'Xavier', 'Kai', 'Zion', 'Jayden', 'Eliana', 'Luca', 'Ezra', 'Maeve', 'Aaliyah', 'Mia', 'Nova', 'Aurora', 'Amara', 'Kayden', 'Ivy', 'Alina', 'Mila', 'Quinn', 'Rowan', 'Elliot', 'Finn', 'Lilibet', 'River', 'Xavier', 'Rachel', 'Amaya', 'Remi', 'Axel', 'Zoey', 'Malachi', 'Alex', 'Blake', 'Lyla', 'Alice', 'Isla', 'Rebecca', 'Rohan', 'Milo', 'Elias', 'Ari', 'Aria', 'Molly', 'Jude', 'Isabella', 'Arthur', 'Millie', 'Andrea', 'Marcus', 'Atlas', 'Ariella', 'Kyle', 'Evan', 'Ira', 'Hayden', 'Bailey', 'Gianna', 'Valerie', 'Brianna', 'Jesse', 'Cecilia', 'Leo', 'Leilani', 'Dante', 'Zoe', 'Khadijah', 'Mya', 'Sharon', 'Sean', 'Brielle', 'Ayla', 'Shia', 'Riley', 'Raya', 'Sloane', 'Alana', 'Charlie', 'Kian', 'Hudson', 'Elise', 'Akira', 'Mika', 'Freya', 'Nia', 'Natasha', 'Myra', 'Mateo', 'Everett', 'Rae', 'Savannah', 'Thea', 'Finley', 'Alaina', 'Mina', 'Yara', 'Emerson', 'Camille', 'Ivan', 'Skyler', 'Skylar', 'Alma', 'Reese', 'Sasha', 'Asa', 'Sage', 'Camila', 'Amira', 'Kieran', 'Monica', 'Everly', 'Evie', 'Maverick', 'Kyra', 'Ian', 'Julia', 'Vivian', 'Theo', 'Ophelia', 'Chelsea', 'Azariah', 'Jade', 'Lara', 'Ava', 'Morgan', 'Lennox', 'Luna', 'Isabelle', 'Amir', 'Rhys', 'Arlo', 'Giovanni', 'Aisha', 'Orion', 'Ahmed', 'Nolan', 'Ezekiel', 'Michelle', 'Lea', 'Silas', 'Elaine', 'Adira', 'Callan', 'Lilith', 'Justin', 'Simon', 'Rhea', 'Marie', 'Lisa', 'Damien', 'Ximena', 'Lilah', 'Elora', 'Sienna', 'Fiona', 'Urban', 'Jean', 'Eden', 'Kayla', 'Avi', 'Octavia', 'Skye', 'Nancy', 'Otis', 'Lila', 'Anya', 'Elena', 'Zayne', 'Gigi', 'Alyssa', 'Amelia', 'Giselle', 'Francis', 'Jacqueline', 'Aiden', 'Kylie', 'Wren', 'Maria', 'Mae', 'Colette', 'Louise', 'Aliyah', 'Chase', 'Tara', 'Lorenzo', 'Sydney', 'Callie', 'Niko', 'Avery', 'Gemma', 'Rafael', 'Hailey', 'Harlow', 'Adeline', 'Margot', 'Rory', 'Nyla', 'Helena', 'Colin', 'Xander', 'Rylee', 'Irene', 'Ashton', 'Marley', 'Arden', 'Kaira', 'Arianna', 'Pia', 'Nola', 'Miles', 'Brooks', 'Annalise', 'Imani', 'Josie', 'Ellis', 'Cali', 'Hadassah', 'Phoenix', 'Piper', 'Emery', 'Aliza', 'Mackenzie', 'Timothy', 'Adrian', 'Sawyer', 'Harvey', 'Enoch', 'Lachlan', 'Kaiden', 'Zuri', 'Shelby', 'Liam', 'Olivia', 'Aubrey', 'Sanjana', 'Rayne', 'Stella', 'Cleo', 'Gracie', 'Oakley', 'Madeline', 'Melissa', 'Lauren', 'Mona', 'Alicia', 'Jasmine', 'Scott', 'Abel', 'Elliott', 'Wesley', 'Aditya', 'Alan', 'Brooke', 'Sunny', 'Sana', 'Blair', 'Leon', 'Emmanuel', 'Lilian', 'Priya', 'Malia', 'Elodie', 'Adriel', 'Amos', 'Trisha', 'Naomi', 'Damian', 'Nevaeh', 'Judah', 'Sloan', 'Joel', 'Nicholas', 'Azriel', 'Lyra', 'Lee', 'Kevin', 'Remy', 'Omar', 'Amelie', 'Caleb', 'Aleena', 'Killian', 'Theodore', 'Asher', 'Mariam', 'Claudia', 'Noelle', 'Juliana', 'Makayla', 'Beau', 'Nikita', 'Beckett', 'Nadia', 'Ana', 'Zane', 'Jayce', 'Brayden', 'Elia', 'Leia', 'Cooper', 'Zain', 'Ronan', 'Liana', 'Kali', 'Serena', 'Davina', 'Zaid', 'Dillon', 'Sylvia', 'Rhiannon', 'Ryder', 'Zara', 'Amina', 'Keanu', 'Amaris', 'Eloise', 'Mara', 'Vera', 'Sonny', 'Keira', 'Ali', 'Sierra', 'Harper', 'Katherine', 'Siobhan', 'Ada', 'Gia', 'Heather', 'Kalani', 'Penny', 'Camilla', 'Cole', 'Amani', 'Emmet', 'Leila', 'Ethan', 'Alani', 'Fallon', 'Joyce', 'Joan', 'Winifred', 'Amyra', 'Mira', 'Quincy', 'Kimberly', 'Faye', 'Colton', 'Cayden', 'Maira', 'Ayana', 'Shiloh', 'Darren', 'Evelyn', 'Lorelei', 'Iva', 'Felix', 'Tessa', 'Jalen', 'Rylan', 'Nellie', 'Masha', 'Amora', 'Alvin', 'Leighton', 'Keziah', 'Mikayla', 'Harley', 'Oliver', 'Huxley', 'Martin', 'Noa', 'Rocco', 'Shane', 'Ines', 'Rai', 'Harry', 'Lily', 'Stanley', 'Darcy', 'Bryce', 'Devin', 'Lucas', 'Jamie', 'Teddy', 'Martha', 'Albert', 'Travis', 'Lucian', 'Emelia', 'Delilah', 'Norah', 'Azalea', 'Valentina', 'Hallie', 'Nora', 'Kara', 'Misha', 'Ishmael', 'Mimi', 'Pamela', 'Genevieve', 'Thalia', 'Collin', 'Grayson', 'June', 'May', 'Kenji', 'Chiara', 'Ravi', 'Rosie', 'Seraphina', 'Juno', 'Sophie', 'Simone', 'Gavin', 'Alayna', 'Miriam', 'Patricia', 'Christine', 'Joaquin', 'Dior', 'Israel', 'Teagan', 'Jocelyn', 'Zaira', 'Tiffany', 'Cedric', 'Reyna', 'Winston', 'Maximus', 'Dennis', 'George', 'Braxton', 'Deborah', 'Lorraine', 'Romy', 'Dakota', 'Reuben', 'Hayley', 'Anisha', 'Saira', 'Veda', 'Tiana', 'Kyler', 'Preston', 'Olive', 'Ellie', 'Rio', 'Yvonne', 'Parker', 'Yana', 'Maia', 'Levi', 'Tyson', 'Graham', 'Cain', 'Kelvin', 'Lynn', 'Lia', 'Kaden', 'Rian', 'Aurelia', 'Spencer', 'Usnavi', 'Elina', 'Ellen', 'Kaya', 'Tamara', 'Mabel', 'Remington', 'Ember', 'Sadie', 'Sahil', 'Azrael', 'Kendall', 'Raine', 'Noah', 'Athena', 'Declan', 'Leigh', 'Helen', 'Rey', 'Janet', 'Ace', 'Alena', 'Lola', 'Karina', 'Grace', 'Jedidiah', 'Alaia', 'Aman', 'Brian', 'Milan', 'Malcolm', 'Javier', 'Emma', 'Marion', 'Adaline', 'Daisy', 'Amal', 'Holly', 'Cillian', 'Kayleigh']
        
        name     = random.choice(names)
        username = f"{name.lower()}_{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))}_{random.randint(1111, 9999)}"
        password = f"{name.lower()}@{random.randint(1111, 9999)}"

        return name, username, password

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
        __email_client = Email()
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
            
                self.__create_account(
                    session     = session,
                    password    = password,
                    email       = __email,
                    username    = username, 
                    first_name  = first_name,
                    signup_code =__signup_code
                )

if __name__ == '__main__':
    Instagram().main()
    # name, username, password = Utils().get_userinfo()

    # print(name)
    # print(username)
    # print(password)
