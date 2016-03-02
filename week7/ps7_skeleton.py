# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:49:21 2016

@author: VirKrupa
"""

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method 
    to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # name- A string that represents the name of the adoption center
        # location - A tuple (x, y) That represents the x and y as floating 
        #               point coordinates of the adoption center location.
        # species_types- A string:integer dictionary that represents the number
        #                   of specific pets that each adoption center holds. 
        self.name = name
        self.location = (float(location[0]), float(location[1]))
        self.species_types = species_types.copy()
    def get_number_of_species(self, species):
        # Returns the number of a given species that the adoption center has.
        try :
            return self.species_types[species]
        except :
            return 0
    def get_location(self):
        # Returns location of the adoption centre
        return self.location
    def get_species_count(self):
        # Returns a copy of the full list and count of the available species 
        #   at the adoption center.
        return self.species_types.copy()
    def get_name(self):
        # Returns name of center
        return self.name
    def adopt_pet(self, species):
        # Decrements the value of a specific species at the adoption center 
        #   and does not return anything.
        if (self.species_types[species]) > 1 :
            self.species_types[species] -= 1
        else :
            self.species_types.pop(species)
        return None
    
    


class Adopter:#(object): # For super class implementation
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # name- A string that represents the name of the adopter
        # desired_species- A string that represents the desired species to adopt
        self.name = name
        self.desired_species = desired_species
        #print "Adopter Initialized"
    def get_name(self):
        # Returns the name of the adopter
        return self.name
    def get_desired_species(self):
        # Returns the desired species of the adopter
        return self.desired_species
    def get_score(self, adoption_center):
        # Returns the score of adopter based on adoption center
        # For the base Adopter class, this score will be 1 * num_desired 
        # where num_desired is the number of the adopter's desired species 
        # that the adoption center has. 
        return (1.0 * 
                adoption_center.get_number_of_species(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter
    will consider. 
    Their score should be 1x their desired species + .3x all 
    of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
#        super(FlexibleAdopter,self).__init__( name, desired_species)
        # name- A string that represents the name of the adopter
        # desired_species- A string that represents the desired species to adopt
        # considered_species- A string/list represents considered species 
        #                       to adopt 
        
        # convert a string to list for uniform processing
        if str(type(considered_species)) == "<type 'str'>" :
            self.considered_species = [considered_species]
        else:
            self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        # # Returns the score of flexible adopter based on adoption centreadopter
#        base_score = super(FlexibleAdopter,self).get_score(adoption_center)
        # Get the base score from base Adopter class
        base_score = Adopter.get_score(self,adoption_center)
        add_score = sum([adoption_center.get_number_of_species(animal) 
                                    for animal in self.considered_species])
        return (base_score + (0.3 * add_score))


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared 
    species. 
    Their score should be 1x number of desired species - .3x the
    number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
#        super(FearfulAdopter,self).__init__( name, desired_species)
        if str(type(feared_species)) == "<type 'str'>" :
            self.feared_species = [feared_species]
        else:
            self.feared_species = feared_species
    def get_score(self, adoption_center):
#        base_score = super(FearfulAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        add_score = sum([adoption_center.get_number_of_species(animal) 
                                    for animal in self.feared_species])
        base_score -= 0.3 * add_score
        return (0.0 if base_score < 0.0 else base_score)


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and 
    cannot even be around it a little bit! If the adoption center contains one
    or more of these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number
    of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
#        super(FearfulAdopter,self).__init__( name, desired_species)
        if str(type(allergic_species)) == "<type 'str'>" :
            self.allergic_species = [allergic_species]
        else:
            self.allergic_species = allergic_species
    def get_score(self, adoption_center):
#        base_score = super(FearfulAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        for animal in self.allergic_species:
            if( adoption_center.get_number_of_species(animal) > 0):
                return(0.0)
        return (base_score)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be 
    given in a dictionary.
    To calculate the score for a specific adoption center, we want to find 
    what is the most allergy-inducing species that the adoption center has 
    for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the
    MedicatedAllergicAdopter is allergic to, then compare them to the 
    medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and 
    multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species,
                                                 medicine_effectiveness):
        AllergicAdopter.__init__(self,name, desired_species,allergic_species)
#super(MedicatedAllergicAdopter,self).__init__( name, desired_species,
#        allergic_species)
        if str(type(medicine_effectiveness)) == "<type 'str'>" :
            self.medicine_effectiveness = [medicine_effectiveness]
        else:
            self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
#        base_score = super(MedicatedAllergicAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 1.0
        for animal in self.allergic_species:
            if( adoption_center.get_number_of_species(animal) > 0):
                if animal in self.medicine_effectiveness :
                    add_score = min(add_score, self.medicine_effectiveness[animal])
                else :
                    return(0.0)

        return (base_score * add_score)


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
#        super(SluggishAdopter,self).__init__( name, desired_species)
        Adopter.__init__(self, name, desired_species)
        self.adopter_location = (float(location[0]), 
                                     float(location[1]))
    def get_distance(self,adoption_center):
        from math import sqrt
        tmp_location = adoption_center.get_location()
        distance = ((tmp_location[0] - self.adopter_location[0])**2)
        distance += ((tmp_location[1] - self.adopter_location[1])**2)
        return sqrt(distance)
        
    def get_score(self, adoption_center):
        from random import uniform
#        base_score = super(SluggishAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        distance = self.get_distance(adoption_center)
        if distance < 1.0:
            add_score = 1.0
        elif distance < 3.0 :
            add_score = uniform(0.700,0.900)
        elif distance < 5.0 :
            add_score = uniform(0.500,0.700)
        else:
            add_score = uniform(0.100,0.500)
        return (base_score * add_score)

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    score_list = [[ac,adopter.get_score(ac)] for ac in list_of_adoption_centers]
    score_list = sorted(score_list, key=lambda x: (-x[1], x[0].get_name()))
    score_list = [item[0] for item in score_list]
    return score_list

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    score_list = [[ad, ad.get_score(adoption_center)] for ad in list_of_adopters]
    score_list = sorted(score_list, key=lambda x: (-x[1], x[0].get_name()))
    score_list = [item[0] for item in score_list]
    return(score_list[0:n])


#ac1 = AdoptionCenter('AC1',{"Dog": 10, "Cat": 5, "Lizard": 3, "Frog":4},(34,45))
#ac2 = AdoptionCenter('AC2',{"Horse": 10, "Cat": 5, "Lizard": 2, "Frog":3},(3,5))
#ap1 = Adopter('NormalAP1', 'Horse')
#ap2 = Adopter('NormalAP2', 'Dog')
#flap1 = FlexibleAdopter('FlexiAP1','Dog',['Frog','Cat'])
#score1 = flap1.get_score(ac2)
#feap1 = FearfulAdopter('FearAp1', 'Dog', ['Frog','Cat'])
#score1 = feap1.get_score(ac2)
#ac3 = AdoptionCenter('tmp',{'wovywscap': 1, 'Dog': 119},(34,45))
#feap2 = FearfulAdopter('FearAp2', 'wovywscap', ['Dog'])
#score1 = feap2.get_score(ac3)
#ac3 = AdoptionCenter('tmp',{'wovywscap': 1, 'Dog': 119},(34,45))
#feap2 = FearfulAdopter('FearAp2', 'wovywscap', 'Dog')
#score1 = feap2.get_score(ac3)
#print(score1)

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2, "Cat":1}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
a = get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
print [entry.get_score(ac) for entry in a]
print [entry.get_name() for entry in a]
#print [entry.get_score(ac) for entry in a ]
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
b = get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])                            
#print(b)
print [adopter4.get_score(entry) for entry in b]
print [entry.get_name() for entry in b]
# you can print the name and score of each item in the list returned