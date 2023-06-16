import grpc
from concurrent import futures
import text_generation_pb2
import text_generation_pb2_grpc
from sample import generate_text

class TextGenerationServicer(text_generation_pb2_grpc.TextGenerationServiceServicer):
    def GenerateText(self, request, context):
        output_text = generate_text(request.start)
        return text_generation_pb2.GenerationResponse(output_text="".join(output_text))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_generation_pb2_grpc.add_TextGenerationServiceServicer_to_server(TextGenerationServicer(), server)
    server.add_insecure_port('[::]:8000')  # Specify the port to listen on
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
