import random 
import string
import math
from operator import itemgetter, attrgetter

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):

        self.name = name
        self.species_types = species_types
        self.location = location
        
    def get_number_of_species(self, animal):
        if self.species_types.get(animal) == None:
                return 0
        return self.species_types.get(animal)
        
    def get_location(self):
        return float(self.location[0]), float(self.location[1]) 
    
    def get_species_count(self):
        self.copyspecies_types = self.species_types.copy()
        return self.copyspecies_types
        
    def get_name(self):
        return self.name
    
    def adopt_pet(self, species):
        if species in AdoptionCenter.get_species_count(self):
            self.species_types[species] = self.species_types.get(species)-1
        if self.species_types.get(species) == 0:
            try:
                del self.species_types[species]
            except KeyError:
                pass
            
            


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
        
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        
        self.num_desired = 1* (adoption_center.get_number_of_species(Adopter.get_desired_species(self)))
        if self.num_desired == 0:
            return 0
        return float(self.num_desired)
        


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    def get_name(self):
        return Adopter.get_name(self)
        
    def get_desired_species(self):
        return Adopter.get_desired_species(self)    
        
    def get_score(self, adoption_center):
        newscore=0
        for elem in self.considered_species:
            score = 0.3 * adoption_center.get_number_of_species(elem)
            newscore = newscore+ score        
            
        self.num_desired = Adopter.get_score(self, adoption_center) + newscore
        if self.num_desired == 0:
            return 0
        return float(self.num_desired)

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
        self.feared_species = feared_species
    def get_name(self):
        return Adopter.get_name(self)
        
    def get_desired_species(self):
        return Adopter.get_desired_species(self)    
        
    def get_score(self, adoption_center):
        newscore = 0
        score = 0.3 * adoption_center.get_number_of_species(self.feared_species)
        newscore = newscore+ score        
            
        self.num_desired = Adopter.get_score(self, adoption_center) - newscore
        if self.num_desired == 0:
            return 0.0
        if self.num_desired <0:
            return 0.0
        return float(self.num_desired)
        
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    def get_allergic_species(self):
        return self.allergic_species
    
    def get_name(self):
        return Adopter.get_name(self)
        
    def get_desired_species(self):
        return Adopter.get_desired_species(self)    
        
    def get_score(self, adoption_center):
        for elem in self.allergic_species:
            for key in adoption_center.get_species_count(self):
                if elem == key:
                    return 0.0
             
        return float(Adopter.get_score(self, adoption_center))
                        
            


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most 
    allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is 
    allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's 
    calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species,allergic_species )
        self.medicine_effectiveness= medicine_effectiveness
    
    def get_name(self):
        return Adopter.get_name(self)
    
    def get_medicine_efficiveness(self, medicine):
        return self.medicine_effectiveness.get(medicine)
        
    def get_desired_species(self):
        return Adopter.get_desired_species(self)    
        
    def get_score(self, adoption_center):
        med_value = list()
        for key in adoption_center.get_species_count():
            for key2 in self.medicine_effectiveness:
                if key == key2:
                    med_value.append(self.medicine_effectiveness.get(key2))
        if len(med_value)>0:
            lowest_value= min(med_value)
            score = (Adopter.get_score(self, adoption_center))*lowest_value  
            return float(score)
        
        else:        
            return float(Adopter.get_score(self, adoption_center))


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
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    
    def get_allergic_species(self):
        return self.allergic_species
    
    def get_name(self):
        return Adopter.get_name(self)
        
    def get_desired_species(self):
        return Adopter.get_desired_species(self)  
    
    def get_location(self):
        if -5.0 <=float(self.location[0]) <= 5.0:
            if -5.0 <=float(self.location[1]) <= 5.0:
                return  float(self.location[0]), float(self.location[1])
            else:
                raise ValueError
        else:
            raise ValueError
            
    def get_linear_distance(self, to_location):
        self.to_location = to_location
        d = math.sqrt(math.pow((self.to_location[0] - self.location[0]),2) + math.pow((self.to_location[1] - self.location[1]),2))
        return float(d)
    
    def get_score(self, adoption_center):
        if SluggishAdopter.get_linear_distance(self, adoption_center.get_location()) <1:
            return float(Adopter.get_score(self, adoption_center))    
            
        if 1<=SluggishAdopter.get_linear_distance(self, adoption_center.get_location())<3:
            rand_num = random.uniform(0.7, 0.9)
            return float(rand_num * float(Adopter.get_score(self, adoption_center)))
            
        if 3<=SluggishAdopter.get_linear_distance(self, adoption_center.get_location())<5:
            rand_num = random.uniform(0.5, 0.7)
            return float(rand_num * float(Adopter.get_score(self, adoption_center)))   
                 
        if SluggishAdopter.get_linear_distance(self, adoption_center.get_location()) >= 5:
            rand_num = random.uniform(0.1, 0.5)
            return float(rand_num * float(Adopter.get_score(self, adoption_center)))
            
            
            
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each 
    AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    score = list()
    adoption_centre =list ()
    final_list = list()
    sorted_list = list()
    sorted_names = list()
    dict = {}
    for item in list_of_adoption_centers:
        score.append(adopter.get_score(item))
        adoption_centre.append(item.get_name())
        final_list.append((adopter.get_score(item),item))
        
    sorted_list = sorted(final_list, key=lambda place: place[0], reverse = True)
    print sorted_list
    for elem in sorted_list:
        sorted_names.append(elem[1])
    return sorted_names
        

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    score = list()
    final_list = list()
    sorted_list= list()
    sorted_names = list()
    for item in list_of_adopters:
        final_list.append((item.get_score(adoption_center), item.get_name()))
    
    sorted_list = sorted(final_list, key = lambda place: place[0], reverse = False)
    print sorted_list
    for elem in sorted_list:
        sorted_names.append(elem[1])
    return sorted_names
