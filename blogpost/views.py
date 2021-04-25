from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#  to restrict pages that we do not want to access without logging in
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# For creating user
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm
# For creating user
from .models import Post
from django.urls import reverse_lazy
# Create your views here.


# @method_decorator(login_required, name='dispatch')
# restrict user access on certain pages
class BlogListView(ListView):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super(BlogListView, self).dispatch(*args, **kwargs)
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):

        return super(BlogDetailView, self).dispatch(*args, **kwargs)
    model = Post
    template_name = 'details.html'


class BlogCreateView(CreateView):

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super(BlogCreateView, self).dispatch(*args, **kwargs)

    model = Post
    template_name = 'createPost.html'
    fields = ['title', 'author', 'body']


class BlogEditView(UpdateView):
    model = Post
    template_name = 'EditPost.html'
    fields = ['title', 'body']


class BlogDeletePostView(DeleteView):
    model = Post
    template_name = 'DeletePost.html'
    success_url = reverse_lazy('home')


# @login_required(login_url='login')
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account created successfully for'+user)
                return redirect('login')

        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def Login(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is Incorrect")
        context = {}
        return render(request, 'login.html', context)


def Logout(request):
    logout(request)
    return redirect('login')
