from django.db import models

class Item(models.Model):
    # Atribut wajib
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    # Atribut tambahan yang relevan untuk e-commerce
    stock = models.IntegerField(default=0)  # Stok barang
    category = models.CharField(max_length=100)  # Kategori barang
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  # Rating barang
    date_added = models.DateField(auto_now_add=True)  # Tanggal barang ditambahkan
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Diskon barang dalam persentase

    def __str__(self):
        return self.name

    @property
    def is_in_stock(self):
        return self.stock > 0  # Menampilkan apakah barang tersedia

    @property
    def final_price(self):
        return self.price - (self.price * (self.discount / 100))  # Menghitung harga setelah diskon
