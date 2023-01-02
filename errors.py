

class PotionException(Exception):
    """
    base Potion Exception
    """
    pass


class DuplicateNoteError(PotionException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AuthNotSet(PotionException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

