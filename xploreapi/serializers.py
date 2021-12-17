from rest_framework import serializers
from .models import Destinations, Trips, Tourguides, TourCompanies, Animals, Tweets, updates, CarHire, Hotels, Facts, Activities


class DestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destinations
        fields = ('id', 'name', 'image', 'about', 'link')


class TourCompaniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TourCompanies
        fields = ('id', 'Cname', 'Cimage', 'location', 'Services', 'website', 'email')


class CarHireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarHire
        fields = ('id', 'type', 'carimage', 'carlocation', 'price', 'contact')


class HotelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotels
        fields = ('id', 'rates', 'Image', 'Hname', 'location', 'website', 'Services', 'email')


class TourguidesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tourguides
        fields = ('id', 'Tname', 'profileimage', 'phonenumber', 'Bio', 'link')


class TweetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = ('id', 'body', 'tweetedby', 'thumbnail', 'tweetedOn', 'runyatweet', 'lugatweet')


class FactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facts
        fields = ('id', 'Fbody', 'Image')


class TripsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trips
        fields = ('id', 'poster', 'Date', 'desc', 'Inclusions',
                  'Exclusions', 'duration', 'price', 'Triptype', 'accmtype', 'paymentmthd')


class updatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = updates
        fields = ('id', 'image','body', 'link', 'runya', 'luga', 'Date','postedby')


class AnimalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animals
        fields = ('id', 'name', 'about', 'image', 'sightloc')

class ActivitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activites
        fields = ('id', 'name', 'about', 'image', 'sight')
