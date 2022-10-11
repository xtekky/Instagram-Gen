from faker import Faker
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
            digits.append("-")
        digits.reverse()
        return "".join(digits)

    @staticmethod
    def cookie_to_headers(cookies: dict) -> dict:
        cookies_str = ""
        for i in cookies.items():
            cookies_str = cookies_str + i[0] + "=" + i[1] + "; "
        return cookies_str[: len(cookies_str) - 2]

    @staticmethod
    def sprint(x: str, msg: str) -> None:
        return "%s{%s%s%s}%s %s[%s%s%s]%s" % (
            Col.purple,
            Col.reset,
            x,
            Col.purple,
            Col.reset,
            Col.blue,
            Col.reset,
            msg,
            Col.blue,
            Col.reset,
        )

    @staticmethod
    def encrypt_password(password: str) -> str:
        return f"#PWD_INSTAGRAM_BROWSER:0:{int(time())}:{password}"

    @staticmethod
    def get_userinfo(faker_session: Faker) -> tuple[str, str, str]:

        full_name = faker_session.name()
        username = faker_session.user_name()
        password = faker_session.password(len(username) * 2)

        return (full_name, username, password)
