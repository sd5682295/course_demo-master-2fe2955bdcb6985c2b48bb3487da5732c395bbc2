from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

import markdown2

def index(request):
	post_list = Post.objects.all().order_by('-publish_date')
	return render(request, 'blog/index.html', {'post_list': post_list})

def blog_detail(request, blog_link):
	post = get_object_or_404(Post, link = blog_link)
	post.content = markdown2.markdown(post.content)
	return render(request, 'blog/post.html', {'post': post})