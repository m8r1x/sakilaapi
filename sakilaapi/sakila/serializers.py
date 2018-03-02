from rest_framework import serializers

from sakilaapi.sakila.models import Actor, ActorInfo, Language, Film, FilmActor, Category, FilmCategory, Customer, Address, City, Country, Store, Staff, Store

class ActorSerializer(serializers.HyperlinkedModelSerializer):
	films = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='film-detail')
	class Meta:
		model = Actor
		fields = ('url', 'first_name', 'last_name', 'films')

class ActorInfoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ActorInfo
		fields = '__all__'

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Language
		fields = '__all__'

class FilmSerializer(serializers.HyperlinkedModelSerializer):
	rental_rate = serializers.DecimalField(max_digits=4, decimal_places=2, coerce_to_string=False)
	replacement_cost = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
	category_url = serializers.HyperlinkedRelatedField(read_only=True, view_name='category-detail')
	class Meta:
		model = Film
		fields = (
			'url', 'title', 'description', 'release_year', 'length',
			'rating', 'rental_rate', 'rental_duration', 'replacement_cost',
			'original_language_id', 'special_features','actors',
			'category_url', 'language_url'
		)

class FilmActorSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='film-detail')
	class Meta:
		model = FilmActor
		fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class FilmCategorySerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='film-detail')
	class Meta:
		model = FilmCategory
		fields = '__all__'

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	customers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='customer-detail')
	staff = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='staff-detail')
	stores = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='store-detail')
	class Meta:
		model = Address
		fields = ('url', 'address', 'address2', 'district', 'postal_code', 'phone', 'city', 'customers', 'staff', 'stores')

class CitySerializer(serializers.HyperlinkedModelSerializer):
	addresses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='address-detail')
	class Meta:
		model = City
		fields = ('url', 'city', 'country', 'addresses')

class CountrySerializer(serializers.HyperlinkedModelSerializer):
	cities = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='city-detail')
	class Meta:
		model = Country
		fields = ('url', 'country', 'cities')

class StaffSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Staff
		fields = '__all__'

class StoreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Store
		fields = '__all__'
