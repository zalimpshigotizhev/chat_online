from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class ChatWithThatTitleAlreadyExistsException(Exception):
    title: str

    def message(self) -> str:
        return f"Чат с названием {self.title} уже существует."

