from django.db import models
from django.urls import reverse
from django.conf import settings

class CourseManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query)|\
			models.Q( description__icontains=query)
			)

class Course(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição simples', blank = True)
	about = models.TextField('Sobre o Curso', blank=True)
	start_date = models.DateField(
		'Data de Início', null = True, blank = True)
	image = models.ImageField(upload_to='courses/images'
		, verbose_name = 'Imagem', null = True, blank = True)
	created_at = models.DateTimeField ('Criado em',
		auto_now_add=True)
	updated_at = models.DateTimeField ('Atualizado em',
		auto_now=True)
	objects = CourseManager()

	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('details',args=(self.slug,))

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']

class Enrollment(models.Model):

	STATUS_CHOICES = (
		(0, 'Pendente'),
		(1, 'Aprovado'),
		(2, 'Cancelado'),
	)

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Usuário',
		related_name='enrollments', on_delete=models.PROTECT
	)
	course = models.ForeignKey(
		Course, verbose_name='Curso', related_name='enrollments',
		 on_delete=models.PROTECT
	)
	status = models.IntegerField(
		'Situação', choices=STATUS_CHOICES, default=1, blank=True
	)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def active(self):
		self.status = 1
		self.save()

	def is_approved(self):
		return self.status ==1

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'
		#usuario so pode de cadastrar 1 vez nesse curso
		unique_together = (('user', 'course'), )

class Announcement(models.Model):

	course = models.ForeignKey(Course, verbose_name='Curso', related_name='announcements',on_delete=models.PROTECT)
	title = models.CharField('Título', max_length=100)
	content = models.TextField('Conteúdo')
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Anúncio'
		verbose_name_plural = 'Anúncios'
		ordering = ['-created_at']

class Comment(models.Model):

	announcement = models.ForeignKey(
		Announcement, verbose_name='Anúncio',
		related_name='comments', on_delete=models.PROTECT)
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.PROTECT)
	comment = models.TextField('Comentário')
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'
		ordering = ['created_at']
