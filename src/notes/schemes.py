from datetime import datetime

from pydantic import BaseModel


class NoteScheme(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True


class CreateNoteRequest(BaseModel):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
