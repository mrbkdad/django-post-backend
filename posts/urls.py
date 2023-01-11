from django.urls import path
from .views import Posts, PostDetail

urlpatterns = [
    path("",Posts.as_view()),
    path("<int:pk>",PostDetail.as_view())
]
