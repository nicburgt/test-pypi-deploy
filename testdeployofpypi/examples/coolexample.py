from src.otherexample import NewExample


class CoolExample(NewExample):
    def get_description(self) -> str:
        return self.description