from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import AuthorForm
from .forms import PostForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
#from django.views.generic.edit import UpdateView
#from django.views.generic.edit import DeleteView
#from blog.models import Author
#from django.core.urlresolvers import reverse_lazy
import datetime
from django.views.generic.base import View


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def submit(request):
    print request.method
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog.views.post_list'))
        else:
            messages.error(request, "Error")
    return render(request, 'blog/submit.html', {'form': PostForm()})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



 
