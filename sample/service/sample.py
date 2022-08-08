from pydantic import BaseModel
from typing import List
from polymath.serving.service import Service
from polymath.decorator.fastapi import routable
from sample.service.library import Book, LibraryService, GetResult

class SampleService(Service):
    @routable(path="/say", tags=["Sample"])
    def say(self, word: str="Hello Polymath.")->str:
        return word

    @routable(path="/add_books", methods=["PUT"], tags=["Sample"])
    def add_books(self) -> GetResult:
        library_service = LibraryService.from_name(name="library")

        books = [
            Book(id="ISBN:9781616120351", title="紅樓夢-平裝書",
                 description="《紅樓夢》，中國古典長篇章回小說，是中國四大小說名著之一。《紅樓夢》書內提及的別名，還有《情僧錄》、《風月寶鑑》、《金陵十二釵》。故事是從女媧補天時所剩下的一塊石頭講起，因此又名《石頭記》。乾隆四十九年甲辰夢覺主人序本題為《紅樓夢》。1791年在第一次活字印刷後，《紅樓夢》便取代《石頭記》成為通行的書名。"),
            Book(id="ISBN:9787534226311", title="水滸傳-平裝書",
                 description="《水滸傳》，是以官話白話文寫成的章回小說，列為中國古典四大文學名著之一，六才子書之一。成書年代極爭議，主流支持「明代嘉靖說」，約1524年。其內容講述北宋山東梁山泊以宋江為首的梁山好漢，由被逼落草，發展壯大，直至受到朝廷招安，東征西討的歷程。"),
            Book(id="ISBN:9787810019774", title="水滸傳-精裝書",
                 description="《水滸傳》，是以官話白話文寫成的章回小說，列為中國古典四大文學名著之一，六才子書之一。成書年代極爭議，主流支持「明代嘉靖說」，約1524年。其內容講述北宋山東梁山泊以宋江為首的梁山好漢，由被逼落草，發展壯大，直至受到朝廷招安，東征西討的歷程。"),
        ]

        for book in books:
            library_service.add(book=book)

        return GetResult(
            succeed=True,
            books=books
        )
