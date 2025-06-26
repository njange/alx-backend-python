import sqlite3

def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the user_data database.
    Each batch is a list of user dictionaries.
    """
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_data")  # Corrected table name
    while True:
        rows = cur.fetchmany(batch_size)
        if not rows:
            break
        yield [dict(row) for row in rows]
    conn.close()

def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25 and prints them.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get('age', 0) > 25:
                print(user)

    return "Batch processing complete."