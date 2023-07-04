from django.urls import path
from .views import index, contact, about, shop, product_view

urlpatterns = [
    path("", index),
    path("about", about),
    path("contact", contact),
    path("shop", shop),
    path("shop/<pk>/", product_view, name="product-detail"),
]
