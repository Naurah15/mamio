from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse   # Tambahkan import redirect di baris ini
from main.forms import ItemForm
from main.models import Item
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'npm' : '2306245900',
        'name': 'Naurah Iradya Kurniawan',
        'class': 'PBP B',
        'last_login': request.COOKIES.get('last_login'),
        
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request, id):
    # Mendapatkan item berdasarkan id
    get_item = Item.objects.get(pk = id)

    # Set get_item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=get_item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    # Get mood berdasarkan id
    get_menu_item = Item.objects.get(pk = id)
    # Hapus mood
    get_menu_item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    # Mendapatkan data dari POST request dan menggunakan strip_tags untuk membersihkan HTML tags
    name = strip_tags(request.POST.get("name"))  # strip HTML tags dari name
    price = strip_tags(request.POST.get("price"))  # strip HTML tags dari price
    description = strip_tags(request.POST.get("description"))  # strip HTML tags dari description
    stock = strip_tags(request.POST.get("stock", 0))  # strip HTML tags dari stock, set default 0 jika tidak disediakan
    category = strip_tags(request.POST.get("category"))  # strip HTML tags dari category
    rating = strip_tags(request.POST.get("rating", 0))  # strip HTML tags dari rating, set default 0 jika tidak disediakan
    user = request.user  # Mendapatkan user yang sedang login

    # Membuat item baru dengan data yang sudah dibersihkan
    new_item = Item(
        user=user,
        name=name,
        price=int(price),  # Pastikan harga adalah integer
        description=description,
        stock=int(stock),  # Pastikan stok adalah integer
        category=category,
        rating=float(rating),  # Pastikan rating adalah float
    )
    
    # Menyimpan item baru ke database
    new_item.save()

    return HttpResponse(b"CREATED", status=201)