from django.urls import path
from rest_framework.routers import DefaultRouter
from products.api.views import ProductListView, ProductsFilterView,TilePageView, MessageView, index,RecPropertyView,RecPropertyView

router = DefaultRouter()
router.register(r'props', RecPropertyView, basename='user')

urlpatterns = [
    # path('props', RecPropertyView.as_view(), name = 'properties-list'),
    path('products', ProductListView.as_view(), name = 'product-list'),
    path('filter/', ProductsFilterView.as_view(), name = 'product-filter'),
    path('products/<int:pk>/',TilePageView.as_view(), name = 'product-page' ),
    path('message/', MessageView.as_view(), name = 'post'),
    path('form/', index, name='index')
] + router.urls
