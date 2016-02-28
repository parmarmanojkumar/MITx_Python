#import random as rand
import string
#import math

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
    
    


class Adopter:#(object):
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
        # For the base Adopter class, this score will be 1 * num_desired 
        # where num_desired is the number of the adopter's desired species 
        # that the adoption center has. 
        return (1.0 * 
                adoption_center.get_number_of_species(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
#        super(FlexibleAdopter,self).__init__( name, desired_species)
        if str(type(considered_species)) == "<type 'str'>" :
            self.considered_species = [considered_species]
        else:
            self.considered_species = considered_species
    def get_score(self, adoption_center):
#        base_score = super(FlexibleAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 0
        for animal in self.considered_species:
            add_score += adoption_center.get_number_of_species(animal)
        return (base_score + (0.3 * add_score))


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
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
        add_score = 0
        for animal in self.feared_species:
            add_score += adoption_center.get_number_of_species(animal)
        base_score -= 0.3 * add_score
        if base_score < 0.0:
            base_score = 0.0
        return (base_score)


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
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
        add_score = 1
        for animal in self.allergic_species:
            if( adoption_center.get_number_of_species(animal) > 0):
                add_score = 0.0
                break
        return (base_score * add_score)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species,medicine_effectiveness):
        AllergicAdopter.__init__(self,name, desired_species,allergic_species)
#        super(MedicatedAllergicAdopter,self).__init__( name, desired_species,allergic_species)
        if str(type(medicine_effectiveness)) == "<type 'str'>" :
            self.medicine_effectiveness = [medicine_effectiveness]
        else:
            self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
#        base_score = super(MedicatedAllergicAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        add_score = 1.0
        allergic_adoption = []
        for animal in self.allergic_species:
            if( adoption_center.get_number_of_species(animal) > 0):
                allergic_adoption.append(animal)
        for animal in  allergic_adoption:
            try :
                me_score = self.medicine_effectiveness[animal]
            except :
                me_score = 0
            if me_score < add_score :
                add_score = me_score
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
        import math
        tmp_location = adoption_center.get_location()
        distance = ((tmp_location[0] - self.adopter_location[0])**2)
        distance += ((tmp_location[1] - self.adopter_location[1])**2)
        return math.sqrt(distance)
        
    def get_score(self, adoption_center):
        import random as rand
#        base_score = super(SluggishAdopter,self).get_score(adoption_center)
        base_score = Adopter.get_score(self,adoption_center)
        distance = self.get_distance(adoption_center)
        if distance < 1.0:
            add_score = 1.0
        elif distance < 3.0 :
            add_score = rand.uniform(0.700,0.900)
        elif distance < 5.0 :
            add_score = rand.uniform(0.500,0.700)
        else:
            add_score = rand.uniform(0.100,0.500)
        return (base_score * add_score)

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 

ac1 = AdoptionCenter('AC1',{"Dog": 10, "Cat": 5, "Lizard": 3, "Frog":4},(34,45))
ac2 = AdoptionCenter('AC2',{"Horse": 10, "Cat": 5, "Lizard": 2, "Frog":3},(3,5))
ap1 = Adopter('NormalAP1', 'Horse')
ap2 = Adopter('NormalAP2', 'Dog')
flap1 = FlexibleAdopter('FlexiAP1','Dog',['Frog','Cat'])
score1 = flap1.get_score(ac2)
feap1 = FearfulAdopter('FearAp1', 'Dog', ['Frog','Cat'])
score1 = feap1.get_score(ac2)
ac3 = AdoptionCenter('tmp',{'wovywscap': 1, 'Dog': 119},(34,45))
feap2 = FearfulAdopter('FearAp2', 'wovywscap', ['Dog'])
score1 = feap2.get_score(ac3)
ac3 = AdoptionCenter('tmp',{'wovywscap': 1, 'Dog': 119},(34,45))
feap2 = FearfulAdopter('FearAp2', 'wovywscap', 'Dog')
score1 = feap2.get_score(ac3)
print(score1)