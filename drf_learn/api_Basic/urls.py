from django.urls import path
from .views import article_list , ArticleApiView , article_detail, ArticleDetailView, GenericApiView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleApiView.as_view()),
    path('generic/article/<int:id>', GenericApiView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetailView.as_view()),
]
