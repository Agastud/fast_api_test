from src.db import get_session
from src.notes.models import NoteModel
from src.notes.schemes import CreateNoteRequest, NoteScheme


class NoteService:
    @staticmethod
    def find_all_notes() -> list[NoteScheme]:
        with get_session() as session:
            note_models = session.query(NoteModel).all()
            return [NoteScheme.from_orm(note) for note in note_models]

    @staticmethod
    def save_note(request: CreateNoteRequest) -> NoteScheme:
        with get_session() as session:
            note_model = NoteModel(**request.dict())
            session.add(note_model)
            session.commit()
            session.refresh(note_model)

            return NoteScheme.from_orm(note_model)
