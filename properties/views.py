from django.shortcuts import render
from .forms import PropertyForm
from .models import Property


# Create your views here.


def PropertyView(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        properties = Property.objects.all()
        context = {
            "properties": properties,
            "form": form
        }
        return render(request,"properties/property_list.html", context=context)
    else:
        form = PropertyForm()
        context = {
            "form": form
        }
        return render(request, "properties/property_form.html",context=context)