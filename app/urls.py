from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('category/<slug:category_slug>/<int:product_id>/', views.product, name='product'),
]