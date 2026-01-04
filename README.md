# Library Management System API

A Django REST Framework (DRF) based Library Management System API.  
This project allows librarians to manage books, authors, categories, and book images, while users can browse books, add reviews, and manage their borrow records.  

---

## Features

### Public/User Features
- Browse books with filtering, searching, and ordering.
- View book details, including author, category, and images.
- View all categories and authors along with book count.
- Add reviews to books.
- Borrow books and manage borrowed books (add/remove/update items in a borrow record).

### Librarian/Admin Features
- Create, update, and delete books, authors, categories.
- Manage book images.
- Restricted endpoints for library staff only (librarian/admin permissions).

### Technical Features
- Pagination for book listings.
- Filtering and search using DjangoFilterBackend and DRF SearchFilter.
- Ordering by fields.
- Prefetching related objects for optimized queries.
- Swagger/OpenAPI documentation for all endpoints.
- JWT or session-based authentication (via DRF `IsAuthenticated` permissions).

---

## Models

- **Category**: Library book categories, annotated with `book_count`.
- **Author**: Book authors, annotated with `book_count`.
- **Book**: Library books with fields like `title`, `description`, `isbn`, `category`, `author`.
- **BookImages**: Multiple images per book.
- **Review**: Users can review books.
- **Borrow**: Records of Students borrowing books.
- **BorrowBook**: Details of books within a borrow record.

---

## API Endpoints

### Categories
- `GET /categories/` – List all categories
- `GET /categories/{id}/` – Retrieve a single category
- `POST /categories/` – Create category (librarian only)
- `PUT /categories/{id}/` – Update category (librarian only)
- `DELETE /categories/{id}/` – Delete category (librarian only)

### Authors
- `GET /authors/` – List all authors
- `GET /authors/{id}/` – Retrieve a single author
- `POST /authors/` – Create author (librarian only)
- `PUT /authors/{id}/` – Update author (librarian only)
- `DELETE /authors/{id}/` – Delete author (librarian only)

### Books
- `GET /books/` – List books (supports filtering, searching, ordering)
- `GET /books/{id}/` – Retrieve a single book
- `POST /books/` – Create book (librarian only)
- `PUT /books/{id}/` – Update book (librarian only)
- `DELETE /books/{id}/` – Delete book (librarian only)

### Book Images
- `GET /books/{book_pk}/images/` – List images of a book
- `POST /books/{book_pk}/images/` – Add an image to a book (admin only)

### Reviews
- `GET /books/{book_pk}/reviews/` – List reviews for a book
- `GET /books/{book_pk}/reviews/{id}/` – Retrieve a review
- `POST /books/{book_pk}/reviews/` – Add a review (authenticated users)
- `PATCH /books/{book_pk}/reviews/{id}/` – Update a review (author only)
- `DELETE /books/{book_pk}/reviews/{id}/` – Delete a review (author only)

### Borrow
- `GET /borrows/` – List all borrow records for current user
- `GET /borrows/{id}/` – Retrieve a single borrow record
- `POST /borrows/` – Create a borrow record (authenticated users)
- `PUT /borrows/{id}/` – Update a borrow record
- `DELETE /borrows/{id}/` – Delete a borrow record

### Borrowed Books
- `GET /borrows/{borrow_pk}/books/` – List all books in a borrow
- `GET /borrows/{borrow_pk}/books/{id}/` – Retrieve a borrowed book
- `POST /borrows/{borrow_pk}/books/` – Add a book to borrow
- `PATCH /borrows/{borrow_pk}/books/{id}/` – Update a borrowed book
- `DELETE /borrows/{borrow_pk}/books/{id}/` – Remove a book from borrow

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/samiul-seam/Library-manage-management-system-with-rest-api.git

cd library-management

```
2. Create a virtual environment
```bash
python -m venv env


Activate the virtual environment:

Windows:

env\Scripts\activate


Linux / Mac:

source env/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt

```
4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

6. Run the development server
```bash
python manage.py runserver
```
7. Access the API
```bash
API Root: http://127.0.0.1:8000/

Swagger UI: http://127.0.0.1:8000/swagger/

Redoc UI: http://127.0.0.1:8000/redoc/