from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    mail = forms.EmailField(label="Email")
    content = forms.CharField(label="Mensaje", required = "True", widget=forms.Textarea)