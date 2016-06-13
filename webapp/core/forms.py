from django import forms
from django.core.exceptions import ValidationError
from webapp.core.models import EmailNewsletter


class EmailNewsletterForm(forms.ModelForm):

    error_css_class = 'alert alert-error'

    class Meta:
        model   = EmailNewsletter
        fields  = ['nome', 'email']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]
        return ' '.join(words)

    def clean(self):
        #validar integridade do model pra depois validar os dados do form
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email'):
            raise ValidationError('Informe seu e-mail')
        return self.cleaned_data

class ContatoForm(forms.Form):

    error_css_class = 'alert alert-error'
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    mensagem = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Escreva a mensagem aqui'})
    )

    class Meta:
        pass

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('nome'):
            raise ValidationError('Informe seu nome')
        if not self.cleaned_data.get('email'):
            raise ValidationError('Informe seu e-mail')
        if not self.cleaned_data.get('mensagem'):
            raise ValidationError('Escreva a mensagem')
        elif len( self.cleaned_data.get('mensagem')) < 20:
            raise ValidationError('Escreva mais de 20 caracteres na mensagem')

        return self.cleaned_data