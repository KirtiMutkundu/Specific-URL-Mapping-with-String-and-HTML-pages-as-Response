from django.shortcuts import render

# Create your views here.
def html(request):
    return render(request,'tag.html')
