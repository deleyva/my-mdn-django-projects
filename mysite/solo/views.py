from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MainView(LoginRequiredMixin, TemplateView):
    template_name = "solo/main.html"

    def get(self, request):
        result = request.session.get("result", False)
        if result:
            del request.session["result"]
        return render(request, self.template_name, {"result": result})

    def post(self, request):
        field1 = request.POST.get("field1")[::-1].strip()
        field2 = request.POST.get("field2")[::-1].strip()
        request.session["result"] = f"{field2} {field1}"
        return redirect(reverse("solo:main"))
