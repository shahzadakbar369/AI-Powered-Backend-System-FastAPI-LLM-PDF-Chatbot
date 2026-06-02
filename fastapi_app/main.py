# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "FastAPI is working"}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --------------------
# Request Body Model
# --------------------
class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home route working"}

@app.get("/about")
def about():
    return {"message": "This is the about page"}

@app.get("/user")
def user():
    return {"name": "Shahzad", "role": "developer"}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "User fetched successfully"
    }
    
    
@app.get("/search")
def search(name: str = None, age: int = None):
    return {
        "name": name,
        "age": age,
        "message": "Search completed"
    }
    
@app.post("/create-user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
    
class Resume(BaseModel):
    resume_text: str
    
@app.post("/analyze-resume")
def analyze_resume(resume: Resume):
    
    text = resume.resume_text.lower()

    score = 50  # base score

    if "python" in text:
        score += 10
    if "fastapi" in text:
        score += 15
    if "api" in text:
        score += 10

    feedback = "Good profile"

    if score < 60:
        feedback = "Needs improvement"
    elif score < 80:
        feedback = "Good backend foundation"
    else:
        feedback = "Excellent profile"

    return {
        "score": score,
        "feedback": feedback
    }