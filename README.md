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
python manage.py migrate

# Criando primeira aplicação
python manage.py startapp core
mv core simplemooc

# Criando segunda aplicação
python manage.py startapp courses
mv courses simplemooc

# Instalando biblioteca de gerenciamento de imagem
pip install Pillow

# Registrando a model da aplicação courses e fazendo as migrações de banco
python manage.py makemigrations
python manage.py migrate

# Abrindo o shell do python para Django
python manage.py shell

	# Importando Course
	from simplemooc.courses.models import Course

	# Instanciando a classe
	course = Course()

	# Adicionando informações no banco de dados
	course.name = "Python na Web com Django"

	course.slug = "django"

	from datetime import date
	course.start_date = date.today()
	course.save()
	course.id # 1
	course.pk # 1
	course.name # 'Python na Web com Django'

	course.name = "Python com Django"
	course.save()
	course.created_at
	course.updated_at
	course.delete()

# Deletar banco de dados pelo terminal
	No diretório onde tiver o arquivo db.sqlite3, dê rm db.sqlite3

# Criando o banco de dados novamente (removi acima)
	python manage.py migrate

# Criando superusuário
	python manage.py createsuperuser

	# Criar super usuário
		# pine
		# pine@pine.com
		# 1234
