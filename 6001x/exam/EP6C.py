# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:19:26 2016

@author: VirKrupa
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. '+self.name + ' says: ' + self.lecture(stuff)



e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 

print e.say('the sky is blue')
print le.say('the sky is blue')
print le.lecture('the sky is blue')
print pe.say('the sky is blue')
print pe.lecture('the sky is blue')
