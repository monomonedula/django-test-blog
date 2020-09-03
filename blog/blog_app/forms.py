from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Article


class BasicArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ("author", "is_read_only", "slug")
        widgets = {
            "content": SummernoteInplaceWidget(),
        }
