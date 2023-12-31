from django.urls import path
from django.contrib.auth.views import LoginView


from . import views

app_name = "users"
urlpatterns = [
    path("signin/", LoginView.as_view(template_name='signin.html'), name='signin'),
    path("signout/", views.signout_view, name="signout"),
    path("signup/", views.signup, name="signup")
]