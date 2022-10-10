from pystyle import Col
from random import choice, choices, randint
from time import time

import string

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
        return f"#PWD_INSTAGRAM_BROWSER:0:{int(time())}:{password}"
    
    @staticmethod
    def get_userinfo() -> list:
        names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila', 'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail', 'Sofia', 'Avery', 'Scarlett', 'Emily', 'Aria', 'Penelope', 'Chloe', 'Layla', 'Mila', 'Nora', 'Hazel', 'Madison', 'Ellie', 'Lily', 'Nova', 'Isla', 'Grace', 'Violet', 'Aurora', 'Riley', 'Zoey', 'Willow', 'Emilia', 'Stella', 'Zoe', 'Victoria', 'Hannah', 'Addison', 'Leah', 'Lucy', 'Eliana', 'Ivy', 'Everly', 'Lillian', 'Paisley', 'Elena', 'Naomi', 'Maya', 'Natalie', 'Kinsley', 'Delilah', 'Claire', 'Audrey', 'Aaliyah', 'Ruby', 'Brooklyn', 'Alice', 'Aubrey', 'Autumn', 'Leilani', 'Savannah', 'Valentina', 'Kennedy', 'Madelyn', 'Josephine', 'Bella', 'Skylar', 'Genesis', 'Sophie', 'Hailey', 'Sadie', 'Natalia', 'Quinn', 'Caroline', 'Allison', 'Gabriella', 'Anna', 'Serenity', 'Nevaeh', 'Cora', 'Ariana', 'Emery', 'Lydia', 'Jade', 'Sarah', 'Eva', 'Adeline', 'Madeline', 'Piper', 'Rylee', 'Athena', 'Peyton', 'Everleigh', 'Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Theodore', 'Jack', 'Levi', 'Alexander', 'Jackson', 'Mateo', 'Daniel', 'Michael', 'Mason', 'Sebastian', 'Ethan', 'Logan', 'Owen', 'Samuel', 'Jacob', 'Asher', 'Aiden', 'John', 'Joseph', 'Wyatt', 'David', 'Leo', 'Luke', 'Julian', 'Hudson', 'Grayson', 'Matthew', 'Ezra', 'Gabriel', 'Carter', 'Isaac', 'Jayden', 'Luca', 'Anthony', 'Dylan', 'Lincoln', 'Thomas', 'Maverick', 'Elias', 'Josiah', 'Charles', 'Caleb', 'Christopher', 'Ezekiel', 'Miles', 'Jaxon', 'Isaiah', 'Andrew', 'Joshua', 'Nathan', 'Nolan', 'Adrian', 'Cameron', 'Santiago', 'Eli', 'Aaron', 'Ryan', 'Angel', 'Cooper', 'Waylon', 'Easton', 'Kai', 'Christian', 'Landon', 'Colton', 'Roman', 'Axel', 'Brooks', 'Jonathan', 'Robert', 'Jameson', 'Ian', 'Everett', 'Greyson', 'Wesley', 'Jeremiah', 'Hunter', 'Leonardo', 'Jordan', 'Jose', 'Bennett', 'Silas', 'Nicholas', 'Parker', 'Beau', 'Weston', 'Austin', 'Connor', 'Carson', 'Dominic', 'Xavier', 'Kai', 'Zion', 'Jayden', 'Eliana', 'Luca', 'Ezra', 'Maeve', 'Aaliyah', 'Mia', 'Nova', 'Aurora', 'Amara', 'Kayden', 'Ivy', 'Alina', 'Mila', 'Quinn', 'Rowan', 'Elliot', 'Finn', 'Lilibet', 'River', 'Xavier', 'Rachel', 'Amaya', 'Remi', 'Axel', 'Zoey', 'Malachi', 'Alex', 'Blake', 'Lyla', 'Alice', 'Isla', 'Rebecca', 'Rohan', 'Milo', 'Elias', 'Ari', 'Aria', 'Molly', 'Jude', 'Isabella', 'Arthur', 'Millie', 'Andrea', 'Marcus', 'Atlas', 'Ariella', 'Kyle', 'Evan', 'Ira', 'Hayden', 'Bailey', 'Gianna', 'Valerie', 'Brianna', 'Jesse', 'Cecilia', 'Leo', 'Leilani', 'Dante', 'Zoe', 'Khadijah', 'Mya', 'Sharon', 'Sean', 'Brielle', 'Ayla', 'Shia', 'Riley', 'Raya', 'Sloane', 'Alana', 'Charlie', 'Kian', 'Hudson', 'Elise', 'Akira', 'Mika', 'Freya', 'Nia', 'Natasha', 'Myra', 'Mateo', 'Everett', 'Rae', 'Savannah', 'Thea', 'Finley', 'Alaina', 'Mina', 'Yara', 'Emerson', 'Camille', 'Ivan', 'Skyler', 'Skylar', 'Alma', 'Reese', 'Sasha', 'Asa', 'Sage', 'Camila', 'Amira', 'Kieran', 'Monica', 'Everly', 'Evie', 'Maverick', 'Kyra', 'Ian', 'Julia', 'Vivian', 'Theo', 'Ophelia', 'Chelsea', 'Azariah', 'Jade', 'Lara', 'Ava', 'Morgan', 'Lennox', 'Luna', 'Isabelle', 'Amir', 'Rhys', 'Arlo', 'Giovanni', 'Aisha', 'Orion', 'Ahmed', 'Nolan', 'Ezekiel', 'Michelle', 'Lea', 'Silas', 'Elaine', 'Adira', 'Callan', 'Lilith', 'Justin', 'Simon', 'Rhea', 'Marie', 'Lisa', 'Damien', 'Ximena', 'Lilah', 'Elora', 'Sienna', 'Fiona', 'Urban', 'Jean', 'Eden', 'Kayla', 'Avi', 'Octavia', 'Skye', 'Nancy', 'Otis', 'Lila', 'Anya', 'Elena', 'Zayne', 'Gigi', 'Alyssa', 'Amelia', 'Giselle', 'Francis', 'Jacqueline', 'Aiden', 'Kylie', 'Wren', 'Maria', 'Mae', 'Colette', 'Louise', 'Aliyah', 'Chase', 'Tara', 'Lorenzo', 'Sydney', 'Callie', 'Niko', 'Avery', 'Gemma', 'Rafael', 'Hailey', 'Harlow', 'Adeline', 'Margot', 'Rory', 'Nyla', 'Helena', 'Colin', 'Xander', 'Rylee', 'Irene', 'Ashton', 'Marley', 'Arden', 'Kaira', 'Arianna', 'Pia', 'Nola', 'Miles', 'Brooks', 'Annalise', 'Imani', 'Josie', 'Ellis', 'Cali', 'Hadassah', 'Phoenix', 'Piper', 'Emery', 'Aliza', 'Mackenzie', 'Timothy', 'Adrian', 'Sawyer', 'Harvey', 'Enoch', 'Lachlan', 'Kaiden', 'Zuri', 'Shelby', 'Liam', 'Olivia', 'Aubrey', 'Sanjana', 'Rayne', 'Stella', 'Cleo', 'Gracie', 'Oakley', 'Madeline', 'Melissa', 'Lauren', 'Mona', 'Alicia', 'Jasmine', 'Scott', 'Abel', 'Elliott', 'Wesley', 'Aditya', 'Alan', 'Brooke', 'Sunny', 'Sana', 'Blair', 'Leon', 'Emmanuel', 'Lilian', 'Priya', 'Malia', 'Elodie', 'Adriel', 'Amos', 'Trisha', 'Naomi', 'Damian', 'Nevaeh', 'Judah', 'Sloan', 'Joel', 'Nicholas', 'Azriel', 'Lyra', 'Lee', 'Kevin', 'Remy', 'Omar', 'Amelie', 'Caleb', 'Aleena', 'Killian', 'Theodore', 'Asher', 'Mariam', 'Claudia', 'Noelle', 'Juliana', 'Makayla', 'Beau', 'Nikita', 'Beckett', 'Nadia', 'Ana', 'Zane', 'Jayce', 'Brayden', 'Elia', 'Leia', 'Cooper', 'Zain', 'Ronan', 'Liana', 'Kali', 'Serena', 'Davina', 'Zaid', 'Dillon', 'Sylvia', 'Rhiannon', 'Ryder', 'Zara', 'Amina', 'Keanu', 'Amaris', 'Eloise', 'Mara', 'Vera', 'Sonny', 'Keira', 'Ali', 'Sierra', 'Harper', 'Katherine', 'Siobhan', 'Ada', 'Gia', 'Heather', 'Kalani', 'Penny', 'Camilla', 'Cole', 'Amani', 'Emmet', 'Leila', 'Ethan', 'Alani', 'Fallon', 'Joyce', 'Joan', 'Winifred', 'Amyra', 'Mira', 'Quincy', 'Kimberly', 'Faye', 'Colton', 'Cayden', 'Maira', 'Ayana', 'Shiloh', 'Darren', 'Evelyn', 'Lorelei', 'Iva', 'Felix', 'Tessa', 'Jalen', 'Rylan', 'Nellie', 'Masha', 'Amora', 'Alvin', 'Leighton', 'Keziah', 'Mikayla', 'Harley', 'Oliver', 'Huxley', 'Martin', 'Noa', 'Rocco', 'Shane', 'Ines', 'Rai', 'Harry', 'Lily', 'Stanley', 'Darcy', 'Bryce', 'Devin', 'Lucas', 'Jamie', 'Teddy', 'Martha', 'Albert', 'Travis', 'Lucian', 'Emelia', 'Delilah', 'Norah', 'Azalea', 'Valentina', 'Hallie', 'Nora', 'Kara', 'Misha', 'Ishmael', 'Mimi', 'Pamela', 'Genevieve', 'Thalia', 'Collin', 'Grayson', 'June', 'May', 'Kenji', 'Chiara', 'Ravi', 'Rosie', 'Seraphina', 'Juno', 'Sophie', 'Simone', 'Gavin', 'Alayna', 'Miriam', 'Patricia', 'Christine', 'Joaquin', 'Dior', 'Israel', 'Teagan', 'Jocelyn', 'Zaira', 'Tiffany', 'Cedric', 'Reyna', 'Winston', 'Maximus', 'Dennis', 'George', 'Braxton', 'Deborah', 'Lorraine', 'Romy', 'Dakota', 'Reuben', 'Hayley', 'Anisha', 'Saira', 'Veda', 'Tiana', 'Kyler', 'Preston', 'Olive', 'Ellie', 'Rio', 'Yvonne', 'Parker', 'Yana', 'Maia', 'Levi', 'Tyson', 'Graham', 'Cain', 'Kelvin', 'Lynn', 'Lia', 'Kaden', 'Rian', 'Aurelia', 'Spencer', 'Usnavi', 'Elina', 'Ellen', 'Kaya', 'Tamara', 'Mabel', 'Remington', 'Ember', 'Sadie', 'Sahil', 'Azrael', 'Kendall', 'Raine', 'Noah', 'Athena', 'Declan', 'Leigh', 'Helen', 'Rey', 'Janet', 'Ace', 'Alena', 'Lola', 'Karina', 'Grace', 'Jedidiah', 'Alaia', 'Aman', 'Brian', 'Milan', 'Malcolm', 'Javier', 'Emma', 'Marion', 'Adaline', 'Daisy', 'Amal', 'Holly', 'Cillian', 'Kayleigh']
        
        name     = choice(names)
        username = f"{name.lower()}_{''.join(choices('abcdefghijklmnopqrstuvwxyz', k=3))}_{randint(1111, 9999)}"
        password = f"{name.lower()}@{randint(1111, 9999)}"

        return name, username, password