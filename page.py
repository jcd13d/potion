import requests
import json

from potion import auth
from potion.errors import DuplicateNoteError
from potion.properties import Property


class Page:
    def __init__(self, headers=auth.headers, id=None) -> None:
        self.headers = headers
        self.id = id
        self.contents = {}
        self.create_note()
        if id is not None:
            self.contents = self.get_note(id)

    def __str__(self) -> str:
        if self.contents is None:
            return None
        else:
            return json.dumps(self.contents, indent=4)

    def get_note(self, note_id) -> dict:
        return NotImplementedError("Not yet implemented")

    def get_id(self):
        return self.contents.get("id", None)

    def get_note_by_title(self, value, db, property="title") -> None:
        base_url = "https://api.notion.com/v1/databases"
        url = f"{base_url}/{db}/query"
        data = {
            "filter": {
                "or": [{
                    "property": property,
                    "rich_text": {
                        "equals": value
                    }
                }]
            }
        }
        result = requests.post(url, headers=self.headers,
                               json=data).json().get("results")
        if not result:
            return self
        if len(result) > 1:
            raise DuplicateNoteError("This note is duplicated!")
        else:
            self.contents = result[0]

        return self

    def exists(self) -> bool:
        results = self.contents.get("id", None)
        if results:
            return True
        else:
            return False

    def create_note(self):
        self.contents["parent"] = {}
        self.contents["properties"] = {}

    def add_parent(self, db):
        self.contents["parent"]['database_id'] = db

    def add_property(self, field_name: str, property: Property):
        self.contents["properties"][field_name] = property.get_dict()

    def upload_note(self):
        url = "https://api.notion.com/v1/pages"
        response = requests.post(
            url, headers=self.headers, json=self.contents)
        self.contents = response.json()
        print(json.dumps(response.json(), indent=4))