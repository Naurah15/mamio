from django.forms import ModelForm
from main.models import Item
from django.utils.html import strip_tags

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "description", "stock", "category", "rating"]

    # Clean method for 'name'
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    # Clean method for 'price'
    def clean_price(self):
        price = self.cleaned_data["price"]
        return int(strip_tags(str(price)))  # Ensure price is cleaned and converted to integer

    # Clean method for 'description'
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    # Clean method for 'stock'
    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        return int(strip_tags(str(stock)))  # Ensure stock is cleaned and converted to integer

    # Clean method for 'category'
    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)

    # Clean method for 'rating'
    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        return float(strip_tags(str(rating)))  # Ensure rating is cleaned and converted to float
