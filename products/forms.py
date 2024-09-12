from django.forms import ModelForm
from products.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = (
            'user',
        )
