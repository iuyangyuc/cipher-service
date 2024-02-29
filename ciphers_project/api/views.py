from django.http import JsonResponse
from .cipher import encoder

# Create your views here.
def greeting(request):
    message = {"message": "Welcome to the Ciphers Service"}
    return JsonResponse(message)

def encoderendpoint(request, text, shift):
    params = request.GET
    print(params)
    cipher = encoder(text, shift)
    return JsonResponse({"cipher": cipher})