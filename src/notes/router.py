from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_session
from src.notes.service import NoteService

from .schemes import CreateNoteRequest, NoteScheme

router = APIRouter(prefix='/notes', tags=['notes'])


@router.get('/')
def find_all_notes(session: Session = Depends(get_session)) -> list[NoteScheme]:
    return NoteService.find_all_notes(session)


@router.post('/', status_code=HTTPStatus.CREATED)
def save_note(request: CreateNoteRequest, session: Session = Depends(get_session)) -> None:
    NoteService.save_note(session, request)
