from django import forms
from .models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        exclude = ('created_at','updated_at',)  #入力項目から作成日時、更新日時を除外










"""
from django import forms
from .models import App

class AppForm(forms.ModelForm)
    class Meta:
        model = App
        exclude = ('product_name','price','url',)
"""