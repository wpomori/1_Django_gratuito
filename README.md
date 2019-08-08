# Intalação Django 1.6.0
#
# Crie um ambiente virtual com conda para instalar o python 3.3 (última versão que funciona com o Django usado no curso da Udemy)
conda create --name py33 python=3.3 --channel conda-forge

	# Ative o ambiente
	source activate py33

	# Instale o Django 1.6.0
	pip install Django==1.6.0


# Criar projeto simplemooc
django-admin.py startproject simplemooc
cd simplemooc

# Rodar o servidor localmente
python manage.py runserver

	# Para acessar a página da aplicação
	# Abre página de parabenização, tudo está OK
	http://127.0.0.1:8000/

# Abra o arquivo settings.py
# Em 'LANGUAGE_CODE', altere 'en-us' para 'pt-br'

# Para criar o banco de dados
python manage.py syncdb

	# Criar super usuário
		# pine
		# pine@pine.com
		# 1234

# Criando a aplicação
python manage.py startapp core
mv core simplemooc

