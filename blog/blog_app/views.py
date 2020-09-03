from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.views import generic
from django.views.generic import FormView, DeleteView

from .models import Article
from .forms import BasicArticleForm


class ArticleList(generic.ListView):
    queryset = Article.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleNewView(LoginRequiredMixin, FormView):
    form_class = BasicArticleForm
    template_name = "new_article.html"
    success_url = "/accounts/dashboard"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(obj.title)
        obj.save()

        return HttpResponseRedirect(self.get_success_url())


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    context_object_name = "article"
    success_url = "/accounts/dashboard/"
    template_name = "article_confirm_delete.html"
