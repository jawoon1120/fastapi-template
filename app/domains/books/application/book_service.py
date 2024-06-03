class BookService:
    def __init__(self):
        pass
    
    def get_books(self) -> list[dict]:
        book_list: list[dict] = [
            {
                "name": "The book1",
                "author": "sam",
                "description": "it's good book1"
            },
            {
                "name": "The book2",
                "author": "kim",
                "description": "it's good book2"
            },
            {
                "name": "The book3",
                "author": "jeong",
                "description": "it's good book3"
            }
        ]
        return book_list