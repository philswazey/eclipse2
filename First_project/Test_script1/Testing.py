'''
Created on May 2, 2019

@author: phil
'''

class Person(object):
    '''
    classdocs
    '''


    def __init__(self, Firstname = "", Lastname = ""):
        self.Firstname = Firstname
        self.Lastname = Lastname
        def __str__(self):
            return self.Firstname + " " +  self.Lastname 
        '''
        Constructor
        '''
        #a = "phil swazey"
        Person()
        p = Person('Phil','Swazey')
        print ("this is p= ", p)
        print (Firstname)