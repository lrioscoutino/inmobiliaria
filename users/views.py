from django.shortcuts import render
from properties.models import Property
# Create your views here.


def first_view(request):
    properties = Property.objects.exclude(owner=request.user)
    context = {
        "properties": properties
    }
    return render(request, "base.html", context=context)