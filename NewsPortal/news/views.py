from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from pprint import pprint
from .models import Post
from .filters import PostFilter
from .forms import PostForm

#Создаем свои классы, которые наследуются от ListView и DetailView.
class PostList(ListView):
    model = Post
    ordering = '-time_of_creation'
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        pprint(context)
        return context

# Добавляем новое представление для поиска постов.
class PostSearch(ListView):
    model = Post
    ordering = '-time_of_creation'
    template_name = 'post_search.html'
    context_object_name = 'post_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'

# Добавляем новое представление для создания постов.
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

# Добавляем представление для изменения постов.
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

# Представление, удаляющее товар.
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')