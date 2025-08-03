# Lab: Flask Pagination

## Introduction

This project demonstrates how to implement **server-side pagination** in a Flask API. Instead of returning all books at once, the `/books` endpoint now supports pagination, allowing clients to request a specific page and number of results per page. This approach is scalable and mirrors the structure used by APIs across the web, from Shopify to Reddit to GitHub.

---

## Features

- Accepts `?page` and `?per_page` query parameters on `/books`
- Returns only the requested subset of records
- Includes metadata: `page`, `per_page`, `total`, `total_pages`
- Returns results in a structured JSON format

---

## Example API Response

```json
{
  "page": 1,
  "per_page": 5,
  "total": 500,
  "total_pages": 100,
  "items": [
    {
      "id": 1,
      "title": "The Curious Cat",
      "author": "Jane Doe",
      "description": "A delightful story about a cat's adventures."
    },
    {
      "id": 2,
      "title": "Learning Flask Fast",
      "author": "John Smith",
      "description": "A quickstart guide to Flask web development."
    }
  ]
}
```

---

## Setup

1. **Install dependencies and activate environment:**

    ```bash
    pipenv install && pipenv shell
    ```

2. **Initialize and migrate the database:**

    ```bash
    cd server
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade head
    ```

3. **Seed the database:**

    ```bash
    python seed.py
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

---

## Usage

- **Default:**  
  `GET /books`  
  Returns page 1 with 5 books per page.

- **Custom page and per_page:**  
  `GET /books?page=2&per_page=10`  
  Returns page 2 with 10 books per page.

- **Edge cases:**  
  - If `page` exceeds the total number of pages, returns an empty list.
  - If no query parameters are provided, defaults to page 1 and 5 books per page.

---

## Running Tests

To run the test suite:

```bash
pytest
```

---
