import markdown
from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from comments.forms import Comment

def index(request):
    return HttpResponse("欢迎二狗访问我的博客！")

# Create your views here.

def blog_index(request):
    blog_list = Post.objects.all().order_by('-created_time')		#获取数据库里面所拥有Post对象
    return render(request,'blog/index.html',{'blog_list':blog_list})


def index(request):
    return render(request,'blog/index.html',context= {
    	'title':'我的博客',
    	'welcome':'欢迎二狗访问我的博客！',
    	})



def archives(request,year,month):
	post_list = Post.objects.filter(created_time__year=year,
									created_time__month=month,
		).order_by('-created_time')
	return render(request,'blog/index.html',context={'post_list':post_list})


def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.body = markdown(post.body,
			#渲染函数传递了额外的参数 extensions
			extensions=[
			#extra本身包含很多拓展
			'markdown.extensions.extra',
			#cidehilite是语法高亮
			'markdown.extensions.codehilite',
			#允许自动生成文件目录
			'markdown.extensions.toc',
			])
	form = CommentForm()
	#获取文章post下的所有评论
	comment_list = post.comment_set.all()
	#将文章、表单以及文章下的评论列表作为模板变量传给detail.html模板。以便渲染数据
	context = {
		'post':post,
		'form':form,
		'comment_list':comment_list,
	}

	return render(request,'blog/detail.html',context=context)


def category(request,pk):
	cate = get_object_or_404(Category,pk=pk)
	post_list = Post.objects.filter(category=cate).order_by('-created_time')
	return render(request,'blog/index.html',context={'post_list':post_list})
