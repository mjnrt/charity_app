from django.shortcuts import render
from django.views import View


class LandingPage(View):
    template_name = "charity/index.html"

    def get(self, request):
        return render(request, self.template_name)


class AddDonation(View):
    template_name = "charity/form.html"

    def get(self, request):
        return render(request, self.template_name)


class Login(View):
    template_name = "charity/login.html"

    def get(self, request):
        return render(request, self.template_name)


class Register(View):
    template_name = "charity/register.html"

    def get(self, request):
        return render(request, self.template_name)
