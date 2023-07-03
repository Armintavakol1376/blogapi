from django.views.generic import ListView

from .models import Products


class ProductsListView(ListView):
    model = Products
    template_name = "products_list.html"
