from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .models import headerSection
from .models import logo

# Create your views here.
def IndexView(request):
    post = Post.objects.all()
    header = headerSection.objects.all()
    return render(request, 'index.html',{'post':post, 'headpost':header})

def SinglePost(request, id):
    get_single_post = get_object_or_404(Post, pk=id)

    return render(request, 'post.html',{'single_post':get_single_post})


