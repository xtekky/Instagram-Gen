from httpx import Client
from random import choice

import string


class TempEmail:
    def __init__(self, proxy: str = None, timeout: int = 15) -> None:
        self.session = Client(
            headers={"Content-Type": "application/json"}, timeout=timeout, proxies=proxy
        )
        self.base_url = "https://api.mail.tm"

    def get_domains(self) -> list:
        return [
            item["domain"]
            for item in self.session.get(f"{self.base_url}/domains").json()[
                "hydra:member"
            ]
        ]

    def get_mail(
        self,
        name: str = "".join(choice(string.ascii_lowercase) for _ in range(15)),
        password: str = None,
        domain: str = None,
    ) -> str:
        mail: str = f"{name}@{domain if domain != None else self.get_domains()[0]}"
        response: int = self.session.post(
            f"{self.base_url}/accounts", json={"address": mail, "password": mail}
        ).status_code

        try:
            if response == 201:
                token = self.session.post(
                    f"{self.base_url}/token",
                    json={
                        "address": mail,
                        "password": mail if password is None else password,
                    },
                ).json()["token"]

                self.session.headers["Authorization"] = f"Bearer {token}"
                return mail
        except Exception:
            return "Email creation error."

    def fetch_inbox(self):
        return self.session.get(f"{self.base_url}/messages").json()["hydra:member"]

    def get_message(self, message_id: str):
        return self.session.get(f"{self.base_url}/messages/{message_id}").json()

    def get_message_content(self, message_id: str):
        return self.get_message(message_id)["text"]
