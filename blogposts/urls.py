from django.urls import path

from blogposts.apps import BlogpostsConfig
from blogposts.views import BlogpostCreateView, BlogpostListView, BlogpostDetailView, BlogpostUpdateView, \
    BlogpostDeleteView

app_name = BlogpostsConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create'),
    path('', BlogpostListView.as_view(), name='list'),
    path('view/<int:pk>', BlogpostDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogpostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogpostDeleteView.as_view(), name='delete')
]