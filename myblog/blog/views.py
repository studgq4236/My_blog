from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return HttpResponse("欢迎访问我的博客首页！")

# Create your views here.

def blog_index(request):
    blog_list = Post.objects.all().order_by('-created_time')		#获取数据库里面所拥有BlogPost对象
    return render(request,'blog/index.html',{'blog_list':blog_list})


def index(request):
    return render(request,'blog/index.html',context= {
    	'title':'我的博客首页',
    	'welcome':'欢迎访问我的博客首页！',
    	})


def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/detail.html',context={'post':post})