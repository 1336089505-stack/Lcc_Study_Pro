from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from db.model import Book

class BookRepository:
    def __init__(self, session: Session):
        self.session = session
        pass

    def save(self, book: Book):
        self.session.add(book)

    def find_by_id(self, id: int) -> Book:
        return self.session.get(Book, id)

    def find_all(self) -> list[Book]:
        statement = select(Book)
        result = self.session.scalars(statement)
        books = result.all()
        return books

    def delete_by_id(self, id: int):
        book = self.find_by_id(id)
        self.session.delete(book)
        return book

    def update(self ,book: Book):
        book_tmp = self.find_by_id(book.id)
        if not book_tmp:
            return None
        book_tmp.name = book.name
        book_tmp.category = book.category
        book_tmp.binding = book.binding
        book_tmp.tags = book.tags
        book_tmp.price = book.price
        book_tmp.is_sale = book.is_sale

        return book_tmp





