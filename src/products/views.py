

from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm

def product_detail_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Product, id=id)
    context = {
        "obj" : obj
    }
    return render(request, "detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "obj" : obj
    }
    return render(request, "delete.html", context)


def product_create_view(request, *args, **kwargs):
    initial_data = {
        "title": "My awesome title"
    }

    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    # form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form" : form
    }
    return render(request, "create.html", context)

# def product_create_view(request, *args, **kwargs):
#
#
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#
#     form = RawProductForm()
#     context = {
#         "form" : form
#     }
#     return render(request, "create.html", context)
