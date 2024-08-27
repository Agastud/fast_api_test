from http import HTTPStatus

from fastapi import APIRouter

from src.notes.schemes import CreateNoteRequest, NoteScheme
from src.notes.service import NoteService

router = APIRouter(prefix='/notes', tags=['notes'])


@router.get('/')
def find_all_notes() -> list[NoteScheme]:
    return NoteService.find_all_notes()


@router.post('/', status_code=HTTPStatus.CREATED)
def save_note(request: CreateNoteRequest) -> NoteScheme:
    return NoteService.save_note(request)
