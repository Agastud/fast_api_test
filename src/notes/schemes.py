from datetime import datetime

from pydantic import BaseModel, Field


class NoteScheme(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateNoteRequest(BaseModel):
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None

    class Config:
        from_attributes = True