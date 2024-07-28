from fastapi import APIRouter
from .schemes import Note, CreateNoteRequest

router = APIRouter(prefix='/notes', tags=['notes'])


@router.get('/')
def find_all_notes() -> list[Note]:
    return []


@router.post('/')
def save_note(request: CreateNoteRequest) -> Note:
    note = Note()
    return note
