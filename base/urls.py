from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    BookList,
    BookDetail,
    AddToCart,
    RemoveFromCart,
    PlaceOrder,
    UserList,
    UserDetail,
)
from django.contrib import admin

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetail.as_view(), name='book-detail'),
    path('cart/add/<int:pk>/', AddToCart.as_view(), name='add-to-cart'),
    path('cart/remove/<int:pk>/', RemoveFromCart.as_view(), name='remove-from-cart'),
    path('cart/place-order/', PlaceOrder.as_view(), name='place-order'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('admin/', admin.site.urls),
]
