from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_session
from src.notes.service import NoteService

from .schemes import NoteScheme, CreateNoteRequest

router = APIRouter(prefix='/notes', tags=['notes'])


@router.get('/')
def find_all_notes(session: Session = Depends(get_session)) -> list[NoteScheme]:
    return NoteService.find_all_notes(session)


@router.post('/')
def save_note(request: CreateNoteRequest,
              session: Session = Depends(get_session)) -> HTTPStatus:
    NoteService.save_note(session, request)
    return HTTPStatus.CREATED
