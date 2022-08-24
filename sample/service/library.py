from typing import List, Optional
from fastapi.responses import JSONResponse, Response
from plank.serving.service import Service
from plank.decorator.fastapi import routable
from pydantic import BaseModel
import re

class Book(BaseModel):
    id: str
    title: str
    description: str

class AddResult(BaseModel):
    succeed: bool
    message: str

class DeleteResult(BaseModel):
    succeed: bool
    message: str

class GetResult(BaseModel):
    succeed: bool
    books: Optional[List[Book]] = None

class LibraryService(Service):
    library_dict = {}

    @routable(path="/add", methods=["PUT"], tags=["Library"])
    def add(self, book: Book)->Optional[Book]:
        if book.id not in self.library_dict:
            self.library_dict[book.id] = book
            return book
        else:
            return None

    @add.response(response_model=AddResult)
    def add(self, value: Optional[Book]):
        if value is not None:
            return AddResult(succeed=True, message=f"Added {value}.")
        else:
            return AddResult(succeed=False, message=f"The book exists in library.")

    @routable(path="/get", methods=["GET"], tags=["Library"])
    def get(self, book_id: str)->Optional[Book]:
        book = self.library_dict.get(book_id)
        # print("book:", book)
        if book is None:
            raise ValueError("The id of book is not found.")
        return book

    @get.response(response_model=GetResult)
    def get(self, value: Optional[Book]):
        return JSONResponse(GetResult(succeed=True, books=[value]).dict())

    @get.catch(ValueError)
    def get(self, error: Exception):
        return JSONResponse(str(error), status_code=404)

    @routable(path="/delete", methods=["DELETE"], tags=["Library"])
    def delete(self, book_id: str) -> DeleteResult:
        if book_id not in self.library_dict:
            return DeleteResult(succeed=False, message=f"The book id {book_id} not found in library.")
        else:
            del self.library_dict[book_id]
            return DeleteResult(succeed=True, message=f"The book id {book_id} was deleted in library.")

    @routable(path="/find", methods=["GET"], tags=["Library"])
    def find(self, keyword: str) -> GetResult:
        rx = f".*{keyword}.*"
        filtered_books = filter(lambda book: re.search(rx, book.title) is not None or re.search(rx, book.description) is not None, self.library_dict.values())
        return GetResult(succeed=True, books=list(filtered_books))


