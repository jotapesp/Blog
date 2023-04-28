from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='blogs/', permanent=True)),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/bloggers/', views.BloggerListView.as_view(), name='blogger-list'),
    path('blogs/posts/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('blogs/bloggers/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('user/create/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('user/<int:pk>/delete', views.UserDeleteView.as_view(), name='user-delete'),
    path('blogs/posts/create', views.post_blog, name='new-post'),
    path('blogs/posts/<int:pk>/comment/', views.post_comment, name='new-comment'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='delete-comment'),
]
