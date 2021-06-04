from django.forms import ModelForm, fields
from .models import BlogPost

class CreateBlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title","author","body","image",)