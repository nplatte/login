from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate
from django.urls import reverse


def landing(request):
    context = {}
    return render(request, 'login/landing.html', context=context)


class LoginView(View):

    template_name = 'login/landing.html'

    def get_context(self):
        context = {}
        return context

    def get(self, request):
        return render(request, self.template_name, context=self.get_context())
    
    def post(self, request):
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return redirect(reverse('landing'))
        return render(request, self.template_name, context=self.get_context())
