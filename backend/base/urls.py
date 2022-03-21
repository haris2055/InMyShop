from django.urls import path
from . import views
from base.all_views import user_views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('products/<str:pk>/', views.getProduct, name="product"),
    path('users/login/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('users/register/', user_views.registerUser, name='register'),
]