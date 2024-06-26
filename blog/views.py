from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm
from blog.models import Blog


class BlogRequiredMixin:
    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name='content').exists():
            return BlogForm
        raise PermissionDenied


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, BlogRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_name = form.save()
            new_name.slug = slugify(new_name.title)
            new_name.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, BlogRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, BlogRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
