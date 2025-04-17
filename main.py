
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from io import BytesIO
import pytesseract
from PIL import Image

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    return {"answer": f"You asked: {data.get('question', '')}"}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    text = pytesseract.image_to_string(image)
    return {"text": text.strip()}

@app.post("/ocr_ai")
async def ocr_ai(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    text = pytesseract.image_to_string(image)
    return {"structured": text.strip()}
