from django.contrib import admin
from appdata.models import City
from appdata.models import State
from appdata.models import BloodGroupType
from appdata.models import Facts
from appdata.models import NotDonate
from appdata.models import Medication
from appdata.models import FamousQuotes
from appdata.models import Details
from appdata.models import UrgentBlood

admin.site.register(City)
admin.site.register(State)
admin.site.register(BloodGroupType)
admin.site.register(Facts)
admin.site.register(NotDonate)
admin.site.register(Medication)
admin.site.register(FamousQuotes)
admin.site.register(Details)
admin.site.register(UrgentBlood)
