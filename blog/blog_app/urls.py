from . import views
from django.urls import path


urlpatterns = [
    path("", views.ArticleList.as_view(), name="home"),
    path("new/", views.ArticleNewView.as_view(), name="new_article"),
    path(
        "delete/<slug:slug>", views.ArticleDeleteView.as_view(), name="delete_article"
    ),
    path("articles/<slug:slug>/", views.ArticleDetail.as_view(), name="article_detail"),
]
