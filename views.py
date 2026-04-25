from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.urls import reverse

from login.forms import LoginForm

from django.contrib.auth.decorators import login_required


@login_required
def landing(request):
    context = {}
    return render(request, 'login/landing.html', context=context)


class LoginView(View):

    template_name = 'login/login.html'

    def get_context(self):
        context = {'login_form': LoginForm()}
        return context

    def get(self, request):
        return render(request, self.template_name, context=self.get_context())
    
    def post(self, request):
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return redirect(reverse('landing'))
        return render(request, self.template_name, context=self.get_context())
