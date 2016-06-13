# Projeto base para  apps Django 1.9

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:robertoludwig/base-django.git base-django
cd base-django
python -m venv .base-django
source .base-django/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
# hbn.link/secret_gen
heroku config:set DEBUG=False
# configure o email e depois...
git push heroku master --force
``` 

## Criando bucket Amazon S3
1. configure as chaves de acesso da Amazon no .env
2. no terminal, execute: 'python manage.py test webapp.core.tests.test_s3_connection'
3. vá até as propriedades do bucket criado, depois em Permissions e clique em "Edit CORS Configuration", depois salve