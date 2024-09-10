from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245900',
        'name': 'Naurah Iradya Kurniawan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)