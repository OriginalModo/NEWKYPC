from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import *
from .forms import *

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'

    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_home')


class NewsDetail(DetailView):
    model = Article
    # template_name = 'news/article_detail.html'
    # context_object_name = 'article'

def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {
        'news': news,
    })

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
    form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)