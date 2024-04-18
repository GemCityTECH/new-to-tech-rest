# GCT-Rest

A sample repository to support an upcoming New To Tech session

## How to run

### Prerequisites

You must have Python 3.12 and [Poetry](https://python-poetry.org/docs/#installation) installed.

### Execution

Ensuring that you have Poetry available in your terminal, run

```bash
poetry shell
```

to use Poetry's virtual environment, and then

```bash
poetry install
```

to install FastAPI and the other dependencies. Then, change directory to the `api` folder:

```bash
cd api
```

and run the service using Uvicorn:

```bash
uvicorn main:app --reload
```

Navigate to `http://127.0.0.1:8000/docs` to see the built-in Swagger API documentation.

## Suggested Exercises

### Starting Out

- Add a 'genre' field to Book. Make sure that you can see this field using `GET /books` and update it using `PUT /books/{id}`.

- Add an endpoint that lets you `GET` a book by author and/or publication year.

- Add a `GET` endpoint that shows the average rating across all books.

- Add support for multiple ratings - and reviewers - per book, and to view both individual reviews and the average review score for a book.

### Moderate

- Share your solutions to one of the above exercises using a GitHub Pull Request.

- Return the summary and ratings for a book using [Goodreads' API](https://www.goodreads.com/api/index).

- Return author biographies using [Wikipedia's API](https://api.wikimedia.org/wiki/Getting_started_with_Wikimedia_APIs).

- Rework this book-based sample app into a different domain: customer tracking, RPG character creator, pizza store, etc.

### Complex

- Add an ORM tool such as SQLAlchemy and use it to persist data between runs.

- Migrate the app's API to GraphQL.

- Dockerize the app.

- Host/deploy the app publicly.

- Build a small JS UI in front of the API.

## Additional Files

If you use Insomnia, `Insomnia REST call collection.json` can be imported to get you started making calls against this API.