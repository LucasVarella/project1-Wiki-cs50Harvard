from django import forms

class NewForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))