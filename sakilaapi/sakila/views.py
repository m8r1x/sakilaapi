from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from sakilaapi.sakila.models import Actor, ActorInfo, Language, Film, FilmActor, Category, FilmCategory, Customer, Address, City, Country, Staff, Store
from sakilaapi.sakila.serializers import ActorSerializer, ActorInfoSerializer, LanguageSerializer, FilmSerializer, FilmActorSerializer, CategorySerializer, FilmCategorySerializer, CustomerSerializer, AddressSerializer, CitySerializer, CountrySerializer, StaffSerializer, StoreSerializer

class ActorViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class ActorInfoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = ActorInfo.objects.all()
	serializer_class = ActorInfoSerializer

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer

class FilmViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Film.objects.all()
	serializer_class = FilmSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class AddressViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class CityViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = City.objects.all()
	serializer_class = CitySerializer

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer

class StaffViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Staff.objects.all()
	serializer_class = StaffSerializer

class StoreViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer
