from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_store' : 'mamio',

        'name': 'Naurah Iradya Kurniawan',
        'npm' : '2306245900',
        'class': 'PBP B',

        'category' : 'Main Course',
        'name_menu' : 'Chicken Steak',
        'quantity_ordered' : '3',
        'stock' : '20',
        'rating' : '95',
        'date_added' : '10 September 2024',
        
        
    }

    return render(request, "main.html", context)