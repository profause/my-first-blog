from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from blog.models import Post
from django.views import generic
from django.contrib.auth import authenticate,login,logout
from blog.forms import PostForm
from blog.forms import UserForm
from blog.forms import UserLoginForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
import datetime

# Create your views here.

def index(request):
     return render(request,'blog/index.html',{})

class IndexView():
    template_name = 'blog/index.html'

class PostView(generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Post

def post_add(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
           new_post = form.save(commit=False)
           new_post.author = request.user
           new_post.created_date = datetime.datetime.now()
           new_post.published_date = datetime.datetime.now()
           new_post.save()
        return HttpResponseRedirect(new_post.get_absolute_url())

    else:
        form = PostForm()

    return render(request,'blog/post_form.html',{'form':form})


class PostUpdate(UpdateView):
    model = Post
    #fields = ['title','text','author']
    form_class = PostForm

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')

class UserFormView(View):
    form_class = UserForm
    template_name = 'blog/register.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #display form with post data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
           user = form.save(commit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']

           user.set_password(password)
           user.save()

           #authenticate user
           user = authenticate(username=username,password=password)

           if user is not None:
               if user.is_active:
                   login(request,user)
                   return redirect('blog:posts')


        return render(request,self.template_name,{'form':form})

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'blog/login.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #display form with post data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
           #user = form.save(commit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']

           #authenticate user
           user = authenticate(username=username,password=password)
           if user is not None:
               if user.is_active:
                   login(request,user)
                   return redirect('blog:posts')


        return render(request,self.template_name,{'form':form})

def logout_view(request):
    logout(request)
    return redirect('blog:index')
