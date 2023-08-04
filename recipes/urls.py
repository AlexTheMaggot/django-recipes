from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', RecipeList.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('save/<int:post_id>/', save_post, name='save_post'),
]
