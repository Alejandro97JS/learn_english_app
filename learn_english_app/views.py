from django.http import HttpResponse

def test(request):
    response_text = "The app is up and running!"
    return HttpResponse(response_text)