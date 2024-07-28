from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel

@dataclass
class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

@dataclass
class CreateNoteRequest(BaseModel):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
