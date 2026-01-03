import psycopg2

# Connect to Neon
conn = psycopg2.connect(
    host="ep-shy-grass-ahml2tw1-pooler.c-3.us-east-1.aws.neon.tech",
    dbname="neondb",
    user="neondb_owner",
    password="npg_sTKx0AJ9jVZD",
    sslmode="require"
)

cur = conn.cursor()

# SELECT query
cur.execute("SELECT id, title, photo FROM books WHERE id = 1")
row = cur.fetchone()  # fetch one row

book_id = row[0]
title = row[1]
photo_data = row[2]  # this is BYTEA binary data

# Save image to file
with open("output.jpg", "wb") as f:
    f.write(photo_data)

print(f"Book ID: {book_id}, Title: {title}, image saved as output.jpg")

cur.close()
conn.close()
