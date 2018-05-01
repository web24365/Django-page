from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect


class index_page(TemplateView):
    template_name = "index.html"


class about_page(TemplateView):
    template_name = "about.html"


class security_page(TemplateView):
    template_name = "security.html"


class product_page(TemplateView):
    template_name = "product.html"


class service_page(TemplateView):
    template_name = "service.html"