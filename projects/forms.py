from django import forms
from . import models
# للترجمة للعربية
from django.utils.translation import gettext_lazy as _
attrs = {'class': 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        labels = {
            'category': _('Category'),  # ترجمة
            'title': _('Title'),        # ترجمة
            'description': _('Description'),  # ترجمة
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        labels = {
            'category': _('Category'),  # ترجمة
            'title': _('Title'),        # ترجمة
            'status': _('Status'),      # ترجمة
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs),
        }