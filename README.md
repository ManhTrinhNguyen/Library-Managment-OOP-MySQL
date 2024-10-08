# Library-Managment-OOP-MySQL

# Build a Library Management System
Entities:
  Author: Stores information about authors who write books.
  Book: Stores information about books in the library.
  Member: Represents a library member who can borrow books.
  Borrow: Tracks the borrowing records of library members (with return due dates, etc.).
  BookAuthor: Represents the many-to-many relationship between books and authors (a book can have multiple authors, and an author can write multiple books).

# Relationships:
  ## One-to-Many:
  One Member can borrow multiple Books.
  ## Many-to-Many:
  A Book can be written by multiple Authors, and an Author can write multiple Books.


# Requirements:
  ## Create Classes for Each Entity:
  Author:
  Add, update, view, and delete authors.
  Book:
  Add, update, view, and delete books.
  Handle multiple authors for a book (many-to-many relationship).
  Member:
  Add, update, view, and delete members.
  Allow a member to borrow multiple books.
  Borrow:
  Handle borrowing and returning books.
  Track the borrow date, due date, and return date.
  BookAuthor:
  Manage the many-to-many relationship between books and authors.


CREATE TABLE authors(
    -> author_id INT PRIMARY KEY AUTO_INCREMENT,
    -> name VARCHAR(100),
    -> bio TEXT);

CREATE TABLE books(
    -> book_id INT PRIMARY KEY AUTO_INCREMENT,
    -> title VARCHAR(100),
    -> description TEXT,
    -> stock INT);

CREATE TABLE members(
    -> member_id INT PRIMARY KEY AUTO_INCREMENT, 
    -> name VARCHAR(100),
    -> email VARCHAR(100) UNIQUE;
    -> address VARCHAR(255));

CREATE TABLE borrows( 
    -> borrow_id INT PRIMARY KEY AUTO_INCREMENT, member_id INT, 
    -> book_id INT, borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    -> due_date TIMESTAMP, return_date TIMESTAMP NULL,
    -> FOREIGN KEY (member_id) REFERENCES members(member_id),
    -> FOREIGN KEY (book_id) REFERENCES books(book_id));

CREATE TABLE book_authors(
    -> book_id INT,
    -> author_id INT,
    -> PRIMARY KEY (book_id, author_id),
    -> FOREIGN KEY (book_id) REFERENCES books(book_id),
    -> FOREIGN KEY (author_id) REFERENCES authors(author_id));


