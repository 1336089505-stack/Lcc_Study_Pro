from core.converters import BookConverter
from db.model import Book
from db.session import get_session
from repositories.book_repositories import BookRepository
from schema.schema_module import BookModel

class BookService:
    def __init__(self):
        pass

    def save(self, book: BookModel):
        with get_session() as session:
            dao = BookRepository(session)
            entity = BookConverter.model_to_book(book) #model to orm
            dao.save(entity)
            return book

    def update(self, book: BookModel):
        with get_session() as session:
            dao = BookRepository(session)
            entity = BookConverter.model_to_book(book)
            dao.update(entity)


    def get(self, id: int) -> BookModel:
        with get_session() as session:
            repository = BookRepository(session)
            book_entity: Book = repository.find_by_id(id)
            book_model = BookConverter.book_to_model(book_entity)  # orm to model
            return book_model

    def get_all(self) -> list[BookModel]:
        with get_session() as session:
            repository = BookRepository(session)
            books = repository.find_all()
            return [BookConverter.book_to_model(book) for book in books]

    def delete(self, id: int):
        with get_session() as session:
            dao = BookRepository(session)
            dao.delete_by_id(id)
            return {}




