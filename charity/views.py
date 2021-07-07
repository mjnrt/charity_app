from django.shortcuts import render
from django.views import View
from .models import Donation, Institution


class LandingPage(View):
    template_name = "charity/index.html"

    def get(self, request):
        bags_quantity = []
        for x in Donation.objects.all():
            bags_quantity.append(x.quantity)
        institutions = Institution.objects.count()
        ctx = {'bags': sum(bags_quantity),
               'institution': institutions}
        return render(request, self.template_name, ctx)


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
