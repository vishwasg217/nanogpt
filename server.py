import fastapi
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sample import generate_text

class InputText(BaseModel):
    start: str

app = FastAPI()

@app.post("/generate-text")
def output_text(input_text: InputText):
    output_text = generate_text(input_text.start)
    text = "".join(output_text)
    return {"output_text": text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
