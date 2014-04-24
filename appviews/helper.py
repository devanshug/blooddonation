#Imports
from appdata.models import BloodGroupType
from appdata.models import Details
from appdata.models import UrgentBlood

#This class gives the help to the views
class HelperFunctions:
    def getCount(self):
        bloodgroups = []
        for bloodgroupobject in BloodGroupType.objects.all():
            count = Details.objects.filter(bloodgroup=bloodgroupobject.bloodtype).count()
            bloodgroup = {'name' : str(bloodgroupobject),
                          'count' : count}
            bloodgroups.append(bloodgroup)
        return bloodgroups
    def getBloodRequirements(self, username):
        try:
            ret = {'requirements':UrgentBlood.objects.filter(username=Details.objects.get(username=username).bloodgroup)}
            if len(ret['requirements'])==0:
                return {'requirements':UrgentBlood.objects.all()}
            return ret
        except:
            return {'requirements':UrgentBlood.objects.all()}
