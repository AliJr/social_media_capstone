from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Root URL redirects to login if not logged in
    path('home/', views.home, name='home'),  # This will be your home page URL
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('reset_password/', views.reset_password_view, name='reset_password'),  # Password reset page
    path('logout/', views.logout_view, name='logout'),  # Logout page
]
