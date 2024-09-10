from django.db import models

class Item(models.Model):
    # Atribut wajib
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    # Atribut tambahan yang relevan untuk e-commerce
    category = models.CharField(max_length=100)  # Kategori barang
    name_menu = models.DateField(auto_now_add=True)  # nama menu
    quantity_ordered = models.IntegerField(default=0)  # Default jumlah pesanan adalah 0
    stock = models.IntegerField(default=0)  # Stok barang
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  # Rating barang
    date_added = models.DateField(auto_now_add=True)  # Tanggal barang ditambahkan

    def __str__(self):
        return self.name

    @property
    def is_in_stock(self):
        return self.stock > 0  # Menampilkan apakah barang tersedia
