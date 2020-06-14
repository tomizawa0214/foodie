from django import forms
from .models import Category, Area, Review

class SearchForm(forms.Form):
    area = forms.ModelChoiceField(
        label='エリア名',
        required=False,
        queryset=Area.objects,
    )
    category = forms.ModelChoiceField(
        label='カテゴリ',
        required=False,
        queryset=Category.objects,
    )
    freeword = forms.CharField(
        label='フリーワード',
        required=False,
        min_length=2,
        max_length=100
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        area = self.fields['area']
        category = self.fields['category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['score', 'comment']