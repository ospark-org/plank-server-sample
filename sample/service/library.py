from typing import List, Optional
from fastapi.responses import JSONResponse, Response
from polymath.serving.service import Service
from polymath.decorator.fastapi import routable
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
    books: Optional[List[Book]]

class LibraryService(Service):
    library_dict = {}

    @routable(path="/add", methods=["PUT"], tags=["Library"])
    def add(self, book: Book)->AddResult:
        if book.id not in self.library_dict:
            self.library_dict[book.id] = book
            return AddResult(succeed=True, message=f"Added {book}.")
        else:
            return AddResult(succeed=False, message=f"The book `{book.id}` exists in library.")

    @routable(path="/get", methods=["GET"], tags=["Library"])
    def get(self, book_id: str) -> GetResult:
        if book_id in self.library_dict:
            return GetResult(succeed=True, books=[self.library_dict[book_id]])
        else:
            return GetResult(succeed=False, books=None)

    @get.response
    def response(self, result: GetResult)->Response:
        status_code = 200
        if not result.succeed:
            status_code = 404
        return JSONResponse(result.dict(), status_code=status_code)

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


