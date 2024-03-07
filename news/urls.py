# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('trend_10/', views.all_trend_10, name='all_trend_10'),
#     path('trend_month/', views.all_trend_a_month, name='all_trend_a_month'),
#     path('news/detail/<int:pk>/', views.DetailNews.as_view(), name='DetailNews'),
#     path('news/<int:pk>/comment/', views.comment_add, name='comment_add'),
# ]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='home'),
    path('trend/<int:days>/', views.TrendNewsListView.as_view(), name='all_trend'),  # Updated
    path('news/detail/<int:pk>/', views.DetailNews.as_view(), name='DetailNews'),
    path('news/<int:pk>/comment/', views.comment_add, name='comment_add'),
]
