from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from user.forms import PostForm, ImageForm
from .models import Post,Images


def about(request):
    return render(request, 'home/about.html',{'title':'about'})


def home(request):
    return render(request, 'home/home.html',{'title':'home'})


class PostListView(ListView):
    model = Post
    template_name = 'home/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5



class UserPostListView(ListView):
    model = Post
    template_name = 'user/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateImageView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Images
    form_class = ImageForm

    def form_valid(self, form):
        form.instance.post.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def postdetail(request, post_id):
    args = {'post':Post.objects.get(id=post_id)}
    return render(request, "home/postdetail.html", args)

@login_required
def create_post(request):
    if request.method == 'POST':

        form = PostForm(request.POST)
        formset = ImageForm(request.POST or None, request.FILES or None)

        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            photo = Images(post=post, image=formset.cleaned_data['image'],image2=formset.cleaned_data['image2'],
                               image3=formset.cleaned_data['image3'], image4=formset.cleaned_data['image4'],
                               image5=formset.cleaned_data['image5'], image6=formset.cleaned_data['image6'],
                               image7=formset.cleaned_data['image7'], image8=formset.cleaned_data['image8'],
                               image9=formset.cleaned_data['image9'], image10=formset.cleaned_data['image10'])
            photo.save()

            return redirect('home-blog')

    else:
        form = PostForm()
        formset = ImageForm()

    context = {
        'form':form,
        'formset':formset,

    }
    return  render(request, 'home/post_create.html', context)


'''class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
@login_required
def upload(request):
    if request.method == 'POST':
        p_form = PostForm(request.POST, request.FILES, instance=request.user)
        if p_form.is_valid():
            p_form.save()
            return redirect('home-blog')

    else:
        p_form = PostForm(instance=request.user)

    context = {
        'p_form': p_form
    }
    return render(request, 'home/fileup2.html', context)

'''





'''class BasicUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title','file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
'''
