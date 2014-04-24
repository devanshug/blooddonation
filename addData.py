#Author : Devanshu Gupta
#Date : 16-04-2014
#Function of This Script :
#This file adds data to the database already saved in file
#This file is only used once by seprate calling,
#after creating storage.db

#Call this file after 'python manage.py syncdb'
#Type in 'python manage.py shell'
#After you are in your console
#Type in 'import addData'
#Type in 'addData.addData()'


import os

#List of Import of Models
#from <YourApp>.models import <ModelClass>
from appdata.models import State
from appdata.models import City
from appdata.models import BloodGroupType
from appdata.models import Facts
from appdata.models import NotDonate
from appdata.models import Medication
from appdata.models import FamousQuotes

class Data:
    def __init__(self,filename):
        f = open(filename, 'r')
        self.datafield = map(lambda x: x.strip(), f.readlines())
        self.read = -1
    def nextText(self):
        self.read += 1
        while self.datafield[self.read]!='start':
            self.read += 1
        self.read += 1
        string_arr = []
        while self.datafield[self.read]!='end':
            string_arr.append(self.datafield[self.read])
            self.read += 1
        return "\n".join(string_arr)
    def nextCharField(self):
        self.read += 1
        return self.datafield[self.read]
    def nextIntegerField(self):
        self.read += 1
        return int(self.datafield[self.read])
    def fieldReadCount(self):
        return len(self.datafield)
    
'''
#Method can be used for ForeignKey as well with slight modification
def add<ModelClass>(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,data.fieldReadCount(),<fieldCount>):
        obj = modelclass(<FieldName>=data.next<Type>(), [<FieldName>=data.next<Type>(), [<FieldName>=data.next<Type>()....]])
        obj.save()
'''

def addState(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0, data.fieldReadCount(), 1):
        obj = modelclass(state_name=data.nextCharField())
        obj.save()

def addCity(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,data.fieldReadCount(),2):
        obj = modelclass(city_name=data.nextCharField(), state_name=State(state_name=data.nextCharField()))
        obj.save()

def addBloodGroupType(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,data.fieldReadCount(),1):
        obj = modelclass(bloodtype=data.nextCharField())
        obj.save()

def addFacts(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,data.fieldReadCount(),1):
        obj = modelclass(fact=data.nextCharField())
        obj.save()

def addNotDonate(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,data.fieldReadCount(),1):
        obj = modelclass(notdonate=data.nextCharField())
        obj.save()

def addMedication(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,data.fieldReadCount(),2):
        obj = modelclass(medication=data.nextCharField(), waiting_time=data.nextCharField())
        obj.save()

#addFamousQuotes is a custom made, and revealed some flaw in script
def addFamousQuotes(modelclass,MASTER_DIC):
    filename = os.path.join(MASTER_DIC['DATA_DIR'], MASTER_DIC['FILES'][modelclass.__name__])
    data = Data(filename)
    for i in xrange(0,31):
        obj = modelclass(quote=data.nextText(), author=data.nextCharField(), link=data.nextCharField(), reference=data.nextCharField())
        obj.save()


def addData():

    #Add files to add to the database
    FILES = {
        #'<ModelClass>'   :    '<data_file.txt>',
        'City'           :    'cities_data.txt',
        'State'          :    'state_data.txt',
        'BloodGroupType' :    'blood_group_data.txt',
        'Facts'          :    'facts.txt',
        'NotDonate'      :    'no_donation.txt',
        'Medication'     :    'medication.txt',
        'FamousQuotes'   :    'sayings.txt',
    }

    #Replace by static path of data dictionary
    DATA_DIR_NAME = 'assets//data'

    #No alteration in following variables
    BASE_DIR = os.path.dirname(__file__)

    DATA_DIR = os.path.join(BASE_DIR, DATA_DIR_NAME)

    MASTER_DIC = {'DATA_DIR':DATA_DIR,
                  'FILES':FILES}

    #add<ModelClass>(<ModelClass>, MASTER_DIC)
    #addState(State, MASTER_DIC)
    #addCity(City, MASTER_DIC)
    #addBloodGroupType(BloodGroupType, MASTER_DIC)
    #addFacts(Facts, MASTER_DIC)
    #addNotDonate(NotDonate, MASTER_DIC)
    #addMedication(Medication, MASTER_DIC)
    addFamousQuotes(FamousQuotes, MASTER_DIC)

    print "Congratulations!!! The data has been added to the databases"
        
    
if __name__ == "__main__":
    main()
