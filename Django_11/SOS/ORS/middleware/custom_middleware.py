from django.conf import settings
from django.http import HttpResponse

class SimpleMiddleware(object):
    def __init__(self, get_resp):
        self.get_response = get_resp

    def __call__(self, request):
        res = self.get_response(request)
        #return HttpResponse("<center><h1>Welcome to Middleware</h1></center>")
        return res

    def process_exception(self, request, exception):
        return HttpResponse("in exception")