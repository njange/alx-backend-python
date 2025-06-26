#!/usr/bin/python3
seed = __import__('seed')
def stream_user_ages():
    """
    Generator function that yields user ages one by one from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database with a given page size and offset.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    Generator function that lazily fetches pages of users from the database.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

for age in stream_user_ages():
    print(age)