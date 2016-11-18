from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
	return render(request, 'hello/home.html')
def about(request):
	return render(request, 'hello/about.html')
def contact(request):
	return render(request, 'hello/contact.html')
def construction(request):
	return render(request, 'hello/construction.html')

# Here are the hanlders for Erros 404 and 500. I believe they are unused right now.
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
