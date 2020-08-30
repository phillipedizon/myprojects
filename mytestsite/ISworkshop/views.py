from django.shortcuts import render

# Create your views here.
def index(request):
  context = { }


  return render(request, 'ISworkshop/index.html', context=context)

def form(request):
  return render(request, 'ISworkshop/forms.html', {})