from django.urls import path, include
from . import views

# appended with /api/account/ in the url
urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name="profile-detail"),
    path('auth/login/', views.LoginView.as_view(), name="knox_login"),
    path('auth/logout/', views.LogoutView.as_view(), name='knox_logout'),
    path('auth/logoutall/', views.LogoutAllView.as_view(), name='knox_logoutall'),
]
