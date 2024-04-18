from fastapi import FastAPI, HTTPException, status
from schema.book import Book, BookCreate

app = FastAPI()

books: list[Book] = []

book_id_counter = 0
def get_next_book_id() -> int:
    global book_id_counter
    next_id = book_id_counter
    book_id_counter += 1
    return next_id

@app.get("/")
async def root():
    return "The root endpoint of a service (/) is often used as a health check to determine whether the service is working or not."

@app.get(
    "/books",
    response_model=list[Book],
)
async def get_books():
    return books

@app.get(
    "/books/{book_id}",
)
async def get_book(book_id: int) -> Book:
    ret = next((book for book in books if book.id == book_id), None)
    if not ret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Book with ID {book_id} does not exist"
        )
    return ret

# TODO Add endpoint(s) for GET-ing books by author/publication year here
# What should the endpoint(s) be named? 
# Will it/they return one or potentially several books?
# Can you safely handle the case where no books are returned? What HTTP status code would that be?

@app.post(
    "/books",
    status_code=status.HTTP_201_CREATED,
)
async def create_book(book: BookCreate) -> Book:
    new_book = Book.from_base(book, get_next_book_id())
    books.append(new_book)
    return new_book

@app.put(
    "/books/{book_id}",
)
async def update_book(book: BookCreate, book_id: int) -> Book:
    book_to_update = next((book for book in books if book.id == book_id), None)
    if book_to_update:
        book_to_update.title = book.title
        book_to_update.author = book.author
        book_to_update.publication_year = book.publication_year
        book_to_update.rating = book.rating
    else:
        book_to_update = Book.from_base(book, book_id)
        books.append(book_to_update)
    return book_to_update

@app.delete(
    "/books/{book_id}",
)
async def delete_book(book_id: int) -> Book | None:
    book_to_delete = next((book for book in books if book.id == book_id), None)
    if book_to_delete:
        books.remove(book_to_delete)
    return book_to_delete

@app.get("/coffee")
async def brew():
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="Cannot brew coffee with a teapot!"
    )

@app.get("/search/author/")
async def search_by_author(author: str):
    return (book for book in books if author in book.author)

@app.get("/search/pub_year/")
async def search_by_pub_year(year: int):
    return (book for book in books if book.publication_year == year)

@app.get('/info/average_rating')
async def get_average_rating():
    ratings = [book.rating for book in books]
    return sum(ratings) / len(ratings)
