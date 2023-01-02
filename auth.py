import os
from potion.errors import AuthNotSet


class Constants:
    # TODO change key to inherit from env or explicitly set
    def __init__(self, api_key=None) -> None:
        self.api_key = os.environ.get("NOTION_KEY", api_key)
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-08-16"
        }

        if not self.api_key:
            raise AuthNotSet("NOTION_KEY environment variable must be set to integration key.")



