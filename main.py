from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel
from database import conn

app = FastAPI()

#Hi this is parag
class User(BaseModel):
    name: str
    age: int
    email: str


# Opening http://127.0.0.1:8000/ shows the HTML form
@app.get("/")
def home():
    return FileResponse("index.html")


# The HTML form sends its data here (POST /users)
@app.post("/users")
def create_user(user: User = Form()):

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
        (user.name, user.age, user.email)
    )

    conn.commit()
    cursor.close()

    # Send the browser back to the form with a GET request.
    # This way, refreshing the page does NOT insert the user again.
    return RedirectResponse(url="/", status_code=303)


# Returns every row of the users table as JSON
@app.get("/users")
def show_users():

    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, email FROM users ORDER BY id")

    rows = cursor.fetchall()

    cursor.close()

    return rows
