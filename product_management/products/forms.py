from django import forms
from .models import Product, Category

# Form used for BOTH Adding and Editing a Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'price', 'stock', 'image', 'description', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Casual Cotton T-Shirt'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. TSHIRT-001'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional product description...'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    # Validation: Price must be greater than 0
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price

    # Validation: Stock cannot be negative
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("Stock quantity cannot be negative.")
        return stock

    # Validation: SKU unique check
    def clean_sku(self):
        sku = self.cleaned_data.get('sku', '').strip()
        # If updating, exclude the current product from the check
        existing = Product.objects.filter(sku__iexact=sku)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
        if existing.exists():
            raise forms.ValidationError("A product with this SKU already exists. SKU must be unique.")
        return sku
