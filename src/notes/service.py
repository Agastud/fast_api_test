from sqlalchemy.orm import Session

from src.notes.models import NoteModel
from src.notes.note_not_found_exception import NoteNotFoundException
from src.notes.schemes import NoteScheme, CreateNoteRequest


class NoteService:
    @staticmethod
    def find_all_notes(session: Session) -> list[NoteScheme]:
        note_models = session.query(NoteModel).all()

        return [NoteScheme.from_orm(note) for note in note_models]

    @staticmethod
    def save_note(session: Session, request: CreateNoteRequest) -> NoteScheme:
        note_model = NoteModel(**request.dict())

        session.add(note_model)
        session.commit()
        session.refresh(note_model)

        return NoteScheme.from_orm(note_model)

