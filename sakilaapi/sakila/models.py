from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Actor(models.Model):
	actor_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	class Meta:
		db_table = 'actor'
		ordering = ['actor_id']
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class ActorInfo(models.Model):
	actor_id = models.OneToOneField(Actor, primary_key=True, db_column='actor_id')
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	film_info = models.TextField()
	class Meta:
		db_table = 'actor_info'
		ordering = ['actor_id']
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Language(models.Model):
	language_id = models.IntegerField(primary_key=True, db_column='language_id')
	name = models.CharField(max_length=20)
	class Meta:
		db_table = 'language'
		ordering = ['language_id']
	def __unicode__(self):
		return self.name

class Film(models.Model):
	film_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	release_year = models.IntegerField()
	language_url = models.OneToOneField(Language, db_column='language_id')
	rental_duration = models.IntegerField()
	rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
	length = models.IntegerField()
	replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
	rating = models.CharField(max_length=5, choices=(('G', 'General'), ('PG', 'Parental Guidance'), ('PG-13', 'Parental Guidance 13'), ('R', 'Rated'), ('NC-17', 'NC-17')))
	special_features = JSONField()
	actors = models.ManyToManyField(Actor, through='FilmActor')
	class Meta:
		db_table = 'film'
		ordering = ['film_id']
	def __unicode__(self):
		return self.title

class FilmActor(models.Model):
	actor_id = models.ForeignKey(Actor, db_column='actor_id', related_name='films')
	#forgive me father for I have sinned
	film_id = models.ForeignKey(Film, primary_key=True, db_column='film_id')
	class Meta:
		db_table = 'film_actor'
		ordering = ['actor_id']

class Category(models.Model):
	category_id = models.IntegerField(primary_key=True, db_column='category_id')
	name = models.CharField(max_length=25)
	films = models.ManyToManyField(Film, through='FilmCategory')
	class Meta:
		db_table = 'category'
		ordering = ['category_id']

class FilmCategory(models.Model):
	film_id = models.OneToOneField(Film, db_column='film_id', related_name='category_url')
	category_id = models.ForeignKey(Category, primary_key=True, db_column='category_id')
	class Meta:
		db_table = 'film_category'
		ordering = ['film_id']

class Country(models.Model):
	country_id = models.IntegerField(primary_key=True)
	country = models.CharField(max_length=50)
	class Meta:
		db_table = 'country'
		ordering = ['country_id']

class City(models.Model):
	city_id = models.IntegerField(primary_key=True)
	city = models.CharField(max_length=50)
	country = models.ForeignKey(Country, db_column='country_id', related_name='cities')
	class Meta:
		db_table = 'city'
		ordering = ['city_id']

class Address(models.Model):
	address_id = models.IntegerField(primary_key=True)
	address = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	district = models.CharField(max_length=20)
	city = models.ForeignKey(City, db_column='city_id', related_name='addresses')
	postal_code = models.CharField(max_length=10)
	phone = models.CharField(max_length=20)
	class Meta:
		db_table = 'address'
		ordering = ['address_id']

class Staff(models.Model):
	staff_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	address = models.ForeignKey(Address, db_column='address_id', related_name='staff')
	email = models.CharField(max_length=50)
	# store = models.ForeignKey(Store, db_column='store_id')
	active = models.IntegerField()
	username = models.CharField(max_length=16)
	class Meta:
		db_table = 'staff'
		ordering = ['staff_id']

class Store(models.Model):
	store_id = models.IntegerField(primary_key=True, db_column='store_id')
	manager = models.ForeignKey(Staff, db_column='manager_staff_id')
	address = models.ForeignKey(Address, db_column='address_id', related_name='stores')
	class Meta:
		db_table = 'store'
		ordering = ['store_id']

class Customer(models.Model):
	customer_id = models.IntegerField(primary_key=True)
	store = models.ForeignKey(Store, db_column='store_id')
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=50)
	address = models.ForeignKey(Address, db_column='address_id', related_name='customers')
	active = models.IntegerField()
	create_date = models.DateField()
	last_update = models.DateTimeField()
	class Meta:
		db_table = 'customer'
		ordering = ['customer_id']

