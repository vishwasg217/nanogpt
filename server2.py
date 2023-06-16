import grpc
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import text_generation_pb2
import text_generation_pb2_grpc

class InputText(BaseModel):
    start: str

app = FastAPI()

grpc_channel = grpc.insecure_channel("localhost:8000")
stub = text_generation_pb2_grpc.TextGenerationServiceStub(grpc_channel)

@app.post("/generate-text")
def output_text(input_text: InputText):
    request = text_generation_pb2.GenerationRequest(start=input_text.start)
    response = stub.GenerateText(request)
    return {"output_text": response.output_text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
