from abc import ABC, abstractmethod
from enum import Enum


# Enum for note type
class NoteType(str, Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    SUBLIST = "SUBLIST"


# Abstract class for note
class Note(ABC):
    @abstractmethod
    def __init__(self, title, date, is_done):
        self.title = title
        self.date = date
        self.is_done = is_done
        self.type = None


# Text note
class TextNote(Note):
    def __init__(self, title, date, is_done, content=""):
        super().__init__(title, date, is_done)
        self.type = NoteType.TEXT
        self.content = content


# Image note
class ImageNote(Note):
    def __init__(self, title, date, is_done, content=""):
        super().__init__(title, date, is_done)
        self.type = NoteType.IMAGE
        self.content = content


# Audio note
class AudioNote(Note):
    def __init__(self, title, date, is_done, content=""):
        super().__init__(title, date, is_done)
        self.type = NoteType.AUDIO
        self.content = content


# Sublist item
class SublistItem:
    def __init__(self, title, is_done):
        self.title = title
        self.is_done = is_done


# Sublist note
class SublistNote(Note):
    def __init__(self, title, date, is_done, content=None):
        super().__init__(title, date, is_done)
        self.type = NoteType.SUBLIST
        if content is None:
            self.content = []
        self.content = content
