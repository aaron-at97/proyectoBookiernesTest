from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import (ModelForm, TextInput, PasswordInput)
from eBook.models import Book, Writer, Clients


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'class':'form-control input-md input-with-feedback',
        'id': 'username',
        'style': 'min-width: 0; width: 35%; margin: 2% 0; display: inline;',
        'placeholder' : 'Username'
    }), required=True)

    password = forms.CharField(widget=PasswordInput(attrs={
        'class':'form-control input-md',
        'id': 'password',
        'style': 'min-width: 0; width: 35%; margin: 2% 0; display: inline;',
        'placeholder': 'Password'
    }), required=True)

    class Meta:
        model = User

    fields = [
        'username',
        'password',
    ]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['id_book',
                  'title',
                  'genere',
                  'body',
                  ]

    id_book = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ISBN',}),label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo',}),label='')
    genere = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genero',}),label='')
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descripcion',}),label='')

class addWriterForm(ModelForm):
    class Meta:
        model = Writer
        fields = ['books',
                  ]
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all())

class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['name',
                  'nombre',
                  'apellido',
                  'direccion',
                  'codi_postal',
                  'telefon',
                  'correo',
                  ]
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name WebService',}),label='Name WebService')
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',}),label='Name')
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surnames',}),label='Surnames')
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Direction',}),label='Direction')
    codi_postal = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal Code',}),label='Postal Code')
    telefon = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone',}),label='Phone')
    correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email',}),label='Email')

class AceptRejectForm(ModelForm):
    class Meta:
        model = Book
        fields = ['state',
                  ]
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'state',}),label='')

class rejectForm(ModelForm):
    class Meta:
        model = Book
        fields = ['state',
                  'body',
                  ]
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'state',}),label='')
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'body',}),label='')
