from django import forms

class ContactForm(forms.Form):
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(label = 'Nombre', max_length=64)
    message = forms.CharField(label = 'Mensaje')