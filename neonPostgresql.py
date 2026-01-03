import psycopg2

conn = psycopg2.connect(
    host="ep-shy-grass-ahml2tw1-pooler.c-3.us-east-1.aws.neon.tech",
    dbname="neondb",
    user="neondb_owner",
    password="npg_sTKx0AJ9jVZD",
    sslmode="require"
)

cur = conn.cursor()

with open("download.jpg", "rb") as f:
    img = f.read()

cur.execute(
    "INSERT INTO books (title, photo) VALUES (%s, %s)",
    ("Artificial Intelligence", psycopg2.Binary(img))
)

conn.commit()
cur.close()
conn.close()

print("Image stored successfully")
