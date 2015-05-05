from django.http import HttpResponse
from django.template import RequestContext, loader
from rest_framework import viewsets

# Create your views here.
def index(request):
    template = loader.get_template('events/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
