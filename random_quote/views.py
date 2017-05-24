from django.shortcuts import render

# Create your views here.

def quote_list(request):
    return render(request, 'random_quote/base.html')
