from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

def enter(request):
    if request.user.is_authenticated:
        return redirect('/hello')
    else:
        return redirect('/login')

class Log_view(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/login.html')
    def post(self, request, *args, **kwargs):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/hello')
        else:
            return redirect('/')



class Hello(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'hello_page/hello.html')


class Rules(TemplateView):
    template_name = 'hello_page/hello.html'

    # def get_context_data(self, *args, **kwargs):
    #     context['message'] = 'Tosca'
    #     return context
