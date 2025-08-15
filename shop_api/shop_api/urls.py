from django.contrib import admin
from django.urls import path

# product views
from product import views as pviews

# users views
from users.views import RegisterView, ConfirmView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', pviews.category_list_create_api_view),
    path('api/v1/categories/<int:id>/', pviews.category_detail_api_view),
    path('api/v1/products/', pviews.product_list_create_api_view),
    path('api/v1/products/<int:id>/', pviews.product_detail_api_view),
    path('api/v1/products/reviews/', pviews.products_with_reviews_api_view),
    path('api/v1/reviews/', pviews.review_list_create_api_view),
    path('api/v1/reviews/<int:id>/', pviews.review_detail_api_view),
    path('api/v1/users/register/', RegisterView.as_view()),
    path('api/v1/users/confirm/', ConfirmView.as_view()),
    path('api/v1/users/login/', LoginView.as_view()),
]
