from django.urls import URLPattern, path

app_name = 'donations'

from donations.views import LandingPage, AddDonation, Register, Login, Logout, UserView

urlpatterns = [
    path('', LandingPage.as_view(), name='home'),
    path('add/', AddDonation.as_view(), name='add'),
    path('add/confirmation', AddDonation.as_view(), name='add-confirmation'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout, name="logout"),
    path('register/', Register.as_view(), name='register'),
    path('profile/', UserView.as_view(), name='profile'),
]
