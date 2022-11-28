from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from autos.models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {"make_count": mc, "auto_list": al}
        return render(request, "autos/auto_list.html", ctx)


class MakeView(LoginRequiredMixin, ListView):
    model = Make


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")
