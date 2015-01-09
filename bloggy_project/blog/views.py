from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404

from blog.models import Post

def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	t = loader.get_template('blog/index.html')
	c = Context({'latest_posts': latest_posts,})
	return HttpResponse(t.render(c))

def post(request, post_id):
	single_post = get_object_or_404(Post, pk=post_id)
	t = loader.get_template('blog/post.html')
	c = Context({'single_post':single_post,})
	return HttpResponse(t.render(c))


