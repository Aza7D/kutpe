from django.urls import path

from .views import (first_page, user_login,
                    registration,
                    home,
                    profile_view,
                    edit_profile,
                    logout_view,
                    products,)

urlpatterns = [
    path('', home, name='home'),
    path('choice/', first_page, name="first_page"),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('products/', products, name="products"),
]
