

class Property:
    def __init__(self) -> None:
        self.id = None
        self.type = None
        self.attributes = {}

    def get_dict(self) -> dict:
        return {
            self.type: self.attributes
        }


class Relation(Property):
    def __init__(self, related_id, existing_note=None) -> None:
        super().__init__()
        self.type = "relation"
        self.existing_note = existing_note
        if existing_note:
            self.attributes = self.get_existing_realated()
            self.attributes.append({
                "id": related_id
            })
        else:
            self.attributes = [
                {
                    "id": related_id
                }
            ]

    def get_existing_related(self):
        raise NotImplementedError()


class Date(Property):
    def __init__(self, start=None, end=None, tz=None) -> None:
        super().__init__()
        self.type = "date"
        self.attributes = {
            "start": start,
            "end": end,
            "time_zone": tz
        }


class Title(Property):
    def __init__(self, title) -> None:
        super().__init__()
        self.type = "title"
        self.attributes = [
            {
                "text": {
                    "content": title
                }
            }
        ]