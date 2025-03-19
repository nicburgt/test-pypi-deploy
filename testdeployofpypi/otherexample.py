from abc import abstractmethod
from typing import Optional
from src.exampleclass import Example

class NewExample(Example):
    def __init__(
            self,
            name: str,
            description: str,
            count: Optional[int] = None
    ) -> None:
        self.description = description
        super().__init__(name, count)

    @abstractmethod
    def get_description(self) -> str:
        """Fetch description

        Returns:
            str: The description
        """