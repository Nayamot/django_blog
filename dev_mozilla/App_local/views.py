import App_local
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from.models import BlogPost
from .forms import CreateBlogForm


# Create your views here.

def home(request):
    return render(request, 'app_local/home.html')


def blogpost(request):
    blogs = BlogPost.objects.all()
    return render(request, 'app_local/blog.html', {"blogs":blogs})


def blog_detail(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    return render(request, 'app_local/blog_detail.html', {"blog":blog})


def create_blog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/")
    form = CreateBlogForm()
    return render(request, 'app_local/create_blog.html', {"form":form})



def edit_blog(request,pk):
    blog = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, instance=blog)
        form.save()
        return HttpResponseRedirect("/blog/")

    form = CreateBlogForm(instance=blog)
    return render(request, 'app_local/edit_blog.html',{"form":form})



def delete_blog(request,pk):
    blog = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return HttpResponseRedirect("/blog/")

    return render(request, 'app_local/delete_blog.html',{"blog":blog})
        
















def contact(request):
    return render(request, 'app_local/contact.html')


def about(request):
    return render(request, 'app_local/about.html')



def lalbag(request):
    return render(request, 'app_local/lalbag.html')


def mountainpakistan(request):
    return render(request, 'app_local/mountainpakistan.html')


def pyramid_egypt(request):
    return render(request, 'app_local/egypt.html')


