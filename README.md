# GCT-Rest

A sample repository to support an upcoming New To Tech session

## How to run

Ensuring that you have Poetry available in your terminal, run

```bash
poetry shell
poetry install
```

to drop yourself into this repo's virtual environment. Then, change directory to the `api` folder:

```bash
cd api
```

and run the service using Uvicorn:

```bash
uvicorn main:app --reload
```

Navigate to `http://127.0.0.1:8000/docs` to see the built-in Swagger API documentation.
