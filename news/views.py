from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from datetime import datetime, timedelta

from .models import News, Comment
from .forms import CommentForm


class NewsListView(ListView):
    template_name = 'news/index.html'
    context_object_name = 'trend_10'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        end_date_month = datetime.now().date()
        start_date_month = end_date_month - timedelta(days=30)
        context['trend_month'] = News.objects.filter(
            post_date__gte=start_date_month, post_date__lte=end_date_month).order_by('-viewers')
        return context

    def get_queryset(self):
        return News.objects.filter(post_date__gte=datetime.now().date() - timedelta(days=10)).order_by('-viewers')


class TrendNewsListView(ListView):
    template_name = 'news/trend30.html'
    context_object_name = 'trend'

    def get_queryset(self):
        days = int(self.kwargs['days'])
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        return News.objects.filter(post_date__gte=start_date, post_date__lte=end_date).order_by('-viewers')


class DetailNews(DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'content'

    def get(self, request, *args, **kwargs):
        news = self.get_object()
        viewed_news = request.session.get('viewed_news', [])
        if news.pk not in viewed_news:
            news.viewers += 1
            news.save()
            viewed_news.append(news.pk)
            request.session['viewed_news'] = viewed_news
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comment_set.all()
        return context


@login_required(login_url='/login/')
def comment_add(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.news = news
            new_comment.save()
            return redirect('DetailNews', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'news/comment.html', {'form': form, 'news': news})


def comment_det(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        raise Http404("Comment not found")
    return render(request, 'news/detail.html', {'comments': [comment]})
