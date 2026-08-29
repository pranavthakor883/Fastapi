import psycopg

# One single connection used by the whole app
conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="api_db",
    user="postgres",
    password="1146"
)

print("Database Connected!")
