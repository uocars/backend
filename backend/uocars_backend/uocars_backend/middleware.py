class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "http://localhost:5500"  # Replace with your frontend origin
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"  # Add other allowed methods as needed
        response["Access-Control-Allow-Headers"] = "Content-Type"  # Add other allowed headers as needed
        return response