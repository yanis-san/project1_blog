from django.urls import path
from blog.views import post_list, post_detail, PostListView

app_name = 'blog'

urlpatterns = [
    path('',PostListView.as_view(),name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail,name='post_detail'),
    path('<int:post_id>/share/',
views.post_share, name='post_share'),
]
