from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

def product_detail_view(request, *args, **kwargs):

    obj = Product.objects.get(id=1)
    print(obj)
    context = {
        "obj" : obj
    }
    return render(request, "detail.html", context)



def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
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
