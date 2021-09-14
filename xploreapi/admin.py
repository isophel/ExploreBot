from django.contrib import admin
from .models import Destinations,Trips,Tourguides,TourCompanies,Animals,Tweets,updates,CarHire,Hotels,Facts

# Register your models here.
admin.site.register(Destinations)
admin.site.register(Trips)
admin.site.register(updates)
admin.site.register(Tourguides)
admin.site.register(TourCompanies)
admin.site.register(Animals)
admin.site.register(Tweets)
admin.site.register(CarHire)
admin.site.register(Hotels)
admin.site.register(Facts)
