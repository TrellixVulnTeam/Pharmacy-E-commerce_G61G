from myapp.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'orderitem', OrderItemViewSet, basename='orderitem')
router.register(r'shippingaddress', ShippingAddressViewSet, basename='shippingaddress')
