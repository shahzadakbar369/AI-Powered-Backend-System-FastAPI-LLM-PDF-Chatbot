from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi import File, UploadFile
from pypdf import PdfReader
import os

api_key = os.getenv("GROQ_API_KEY")

pdf_text_storage = ""

app = FastAPI()

client = Groq(api_key=api_key)

# Request body model
class Question(BaseModel):
    question: str


@app.post("/ask-ai")
def ask_ai(data: Question):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for students and developers."
            },
            {
                "role": "user",
                "content": data.question
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "question": data.question,
        "answer": answer
    }
    
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    global pdf_text_storage

    reader = PdfReader(file.file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    pdf_text_storage = text

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename,
        "length": len(text)
    }
    
class PDFQuestion(BaseModel):
    question: str
    
@app.post("/ask-pdf")
def ask_pdf(data: PDFQuestion):

    global pdf_text_storage

    if not pdf_text_storage:
        return {
            "error": "No PDF uploaded yet"
        }

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You answer questions based ONLY on the given PDF content."
            },
            {
                "role": "user",
                "content": f"""
PDF CONTENT:
{pdf_text_storage[:6000]}

QUESTION:
{data.question}
"""
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "question": data.question,
        "answer": answer
    }