from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class NoteType(str, Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    SUBLIST = "SUBLIST"


class Note(ABC):
    @abstractmethod
    def __init__(self, title, date, is_done):
        self.title = title
        self.date = date
        self.is_done = is_done
        self.type = None


class TextNote(Note):
    def __init__(self, title, date, is_done, content=""):
        super().__init__(title, date, is_done)
        self.type = NoteType.TEXT
        self.content = content


class ImageNote(Note):
    def __init__(self, title, date, is_done, content=""):
        super().__init__(title, date, is_done)
        self.type = NoteType.IMAGE
        self.content = content


class AudioNote(Note):
    def __init__(self, title, date, is_done, content=""):
        super().__init__(title, date, is_done)
        self.type = NoteType.AUDIO
        self.content = content


class SublistItem:
    def __init__(self, title, is_done):
        self.title = title
        self.is_done = is_done


class SublistNote(Note):
    def __init__(self, title, date, is_done, content=None):
        super().__init__(title, date, is_done)
        self.type = NoteType.SUBLIST
        if content:
            self.content = content
        else:
            self.content = []
