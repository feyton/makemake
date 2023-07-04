from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.
def index(request):
    products = Product.objects.filter(published=True)[:3]
    return render(request, "index.html", {'products': products})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def shop(request):
    product_list = Product.objects.filter(published=True)
    paginator = Paginator(product_list, 10)  # Show 10 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "single-product.html", {'product': product})
