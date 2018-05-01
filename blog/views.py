from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    qs = Post.objects.all()
    # less than equal
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')
    paginate_by = 2
    return render(request, 'blog/post_list.html', {'post_list': qs})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    form = PostForm(request.Post, request.FILES, instance=post)
    if form.is_valid():
        port = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return PostForm()
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})