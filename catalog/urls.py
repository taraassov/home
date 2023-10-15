from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .apps import CatalogConfig
from .views import HomeView, GoodsView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView, \
    categories

app_name = CatalogConfig.name


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('goods/', GoodsView.as_view(), name='goods'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('categories/', categories, name='categories'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
