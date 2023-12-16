from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length= 100)
    email = forms.EmailField(label='e-mail', max_length= 100)
    assunto = forms.CharField(label='Assunto', max_length= 120)
    menssagen = forms.CharField(label='Menssagen', widget=forms.Textarea)
    
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        menssagen = self.cleaned_data['menssagen']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMenssagen: {menssagen}'
        mail = EmailMessage(
            subject= 'Email Enviado Pelo Sistema DJANGO-2',
            body= conteudo,
            from_email= 'contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers= {'Replay-To': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']

