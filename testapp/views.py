import os
from threading import Thread, Lock

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
import time, random, pickle

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from testapp.forms import RegisterUserForm, LoginUserForm

menu = [
   {'title': 'О сайте', 'url_name': 'about'},
]



# def five_sec_number():
#     time.sleep(5)
#     num = random.randint(0, 100)
#     return num
lock = Lock()


# GIL makes to work this thread forever because random.randint uses the CPU
# def change_random_num(mas):
#     while True:
#         lock.acquire()
#         mas[0] = random.randint(0, 100)
#         print(mas[0], 'HAHAHAHAHAHAHAHAHA')
#         time.sleep(5)
#         lock.release()




def index(request):
    #db = open('E:/allprojects/testnum/testproject/testapp/data_random.pkl', 'rb')
    #RANDOM_NUM = pickle.load(db)
    #db.close()
    path_view = os.path.dirname(__file__)

    file = open('%s/data.txt' % path_view, 'r')
    RANDOM_NUM = file.read()
    file.close()
    context = {
        'menu': menu,
        'random_num': RANDOM_NUM,
    }
    return render(request, 'testapp/base.html', context)
    # lock.acquire()
    #random_num = [random.randint(0, 100), ]
    # thr1 = Thread(target=change_random_num, args=random_num)
    # thr1.start()
    #
    # context = {
    #     'menu': menu,
    #     'random_num': random_num[:][0],
    # }
    #lock.release()
    #return render(request, 'testapp/base.html', context)



def about(request):
    return HttpResponse('about')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'testapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'testapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')

    @staticmethod
    def logout_user(request):
        logout(request)
        return redirect('home')