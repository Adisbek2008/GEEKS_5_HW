from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView,
    ReviewListCreateView, ReviewDetailView
)
from users.views import RegisterView, ConfirmUserView, LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/categories/", CategoryListCreateView.as_view()),
    path("api/v1/categories/<int:id>/", CategoryDetailView.as_view()),
    path("api/v1/products/", ProductListCreateView.as_view()),
    path("api/v1/products/<int:id>/", ProductDetailView.as_view()),
    path("api/v1/reviews/", ReviewListCreateView.as_view()),
    path("api/v1/reviews/<int:id>/", ReviewDetailView.as_view()),
    path("api/v1/users/register/", RegisterView.as_view()),
    path("api/v1/users/confirm/", ConfirmUserView.as_view()),
    path("api/v1/users/login/", LoginView.as_view()),
]
