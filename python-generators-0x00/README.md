# Python Generators - 0x00

This project demonstrates the use of Python to interact with MySQL databases, including creating databases, tables, and inserting data from a CSV file. The project is structured to showcase database operations and data handling using Python.

## Features

- **Database Connection**: Establishes a connection to a MySQL database.
- **Database Creation**: Creates a database named `ALX_prodev` if it does not already exist.
- **Table Creation**: Creates a table named `user_data` with the following fields:
  - `user_id`: A unique identifier for each user (UUID).
  - `name`: The name of the user.
  - `email`: The email address of the user.
  - `age`: The age of the user.
- **Data Insertion**: Reads data from a CSV file and inserts it into the `user_data` table, ensuring no duplicate emails are added.

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library
- A CSV file containing user data with the following columns:
  - `name`
  - `email`
  - `age`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-backend-python.git
   cd alx-backend-python/python-generators-0x00