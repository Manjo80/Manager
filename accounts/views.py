from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

class LoginView(DjangoLoginView):
    template_name = "accounts/login.html"

class LogoutView(DjangoLogoutView):
    next_page = "/login/"
