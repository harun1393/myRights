from django import forms

class OvizogForm(forms.Form):
    description = forms.CharField()
    nid = forms.IntegerField()
    authority = forms.CharField()
    word = forms.IntegerField()

class LoginForm(forms.Form):
    nid = forms.IntegerField()
    word = forms.IntegerField()