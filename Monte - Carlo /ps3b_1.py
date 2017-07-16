# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics using monte carlo

from ps3b_precompiled_27 import *    
import numpy
import random
import pylab
import gc
''' 
Begin helper code
'''

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
        if 0<=self.maxBirthProb<=1 and 0<=self.clearProb<=1:
            pass
        else:
            raise ValueError 

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        return random.random()<SimpleVirus.getClearProb(self)


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        #0.01 popDensity given by user
        
        self.popDensity = popDensity 
        #random.seed(0)
        #k =  
        #print k
        if random.random() < SimpleVirus.getMaxBirthProb(self) * (1 - self.popDensity):
            newChild = SimpleVirus(SimpleVirus.getMaxBirthProb(self), SimpleVirus.getClearProb(self))
            return newChild
        else:
            raise NoChildException 


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        
        #if type(self.viruses) == list:
        #    pass
        #else:
        #    raise TypeError 

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
    
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        #if len(self.viruses) > 80:
        #    return len(self.viruses)+50
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
    
    
        virusParticle = list()
        
        for obj in gc.get_objects():
            if isinstance(obj, SimpleVirus):
                virusParticle.append(obj)
                #print obj
        virusParticleCopy = virusParticle
        for elem in virusParticle:
            if elem.doesClear()==False:
                pass
            else:
                virusParticleCopy.remove(elem)                
        newPopDensity = float(float(Patient.getTotalPop(self))/float(Patient.getMaxPop(self))) 
        #print newPopDensity
        newlist = list()
        try:
            for elem in virusParticleCopy:
        #    virusParticle.append(elem.reproduce(newPopDensity))
                newlist.append(elem.reproduce(newPopDensity))
        except NoChildException:
            pass
        #print newlist
        self.viruses = virusParticleCopy + newlist
        #print self.viruses
        return Patient.getTotalPop(self)

class ResistantVirus(SimpleVirus):


    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.mutProb = mutProb
        self.resistances = resistances


    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug):
        return self.resistances.get(drug)       

    def reproduce(self, popDensity, activeDrugs):
        self.popDensity = popDensity
        self.activeDrugs = activeDrugs
        if len(activeDrugs) >0:
            for elem in activeDrugs:
                if ResistantVirus.isResistantTo(self,elem)==True:
                    pass
                else:
                    raise NoChildException
            
        if random.random()< self.maxBirthProb * (1 - popDensity):
            newDict = self.resistances.copy() 
            for key in self.resistances:
            
                if self.mutProb == 1.0:
                    if self.resistances.get(key) == True:
                        newDict[key] = False
                    elif self.resistances.get(key) == False:
                        newDict[key] = True
                        
                if random.random()< self.mutProb:
                    if self.resistances.get(key) == True:
                        newDict[key] = False
                    elif self.resistances.get(key) == False:
                        newDict[key] == True
                 
            newChild = ResistantVirus(self.maxBirthProb, self.clearProb, newDict, self.mutProb)
            return newChild
        else:
            raise NoChildException
            
            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        self.drugList = list()
        Patient.__init__(self, viruses, maxPop)

        #getViruses and getMaxPop can now be used
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        
        self.newDrug = newDrug
        if self.newDrug in self.drugList:
            pass
        else: 
            self.drugList.append(self.newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugList


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count =0
        dictList= list()
        self.drugResist = drugResist
        
        for elem in self.viruses:
            newDict = elem.getResistances()
            dictList.append(newDict)
        #print dictList
        
        
        totalList = list()
        for resistance in dictList:
            count =0
            #print resistance, "resistances"
            conList = list()
            for elem in self.drugResist:
                
                if elem in resistance and resistance.get(elem) == True:
                    #print True
                    conList.append(True)
                if elem in resistance and resistance.get(elem) == False:
                    #print False
                    conList.append(False)
                if elem not in resistance:
                    #print False
                    conList.append(False)
            #print conList, "conList"
            if False in conList:
                count =0
            else:
                count =1
                totalList.append(count)
        return sum(totalList)
             
                        

                

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        virusParticleList = self.viruses
          
        
        for infector in virusParticleList:
            if infector.doesClear()==False:
                pass
            else:
                virusParticleList.remove(infector)
        self.viruses = virusParticleList
        virusParticleCopy = virusParticleList
                     
        newPopDensity = float(float( TreatedPatient.getResistPop(self, TreatedPatient.getPrescriptions(self)))/float(TreatedPatient.getMaxPop(self)) ) 
        newlist = list()
        try:
            for elem in virusParticleCopy:
                newlist.append(elem.reproduce(newPopDensity, TreatedPatient.getPrescriptions(self)))
        except NoChildException:
            pass
        self.viruses = virusParticleCopy + newlist
        k = TreatedPatient.getTotalPop(self) + TreatedPatient.getResistPop(self, TreatedPatient.getPrescriptions(self))
        return k

           


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    virusList = list()
    popList= list()
    popListNew= list()
    trialList = list()
    avgList = list()
    avgListNew = list()
    numList = list()
    plotList= list()
    plotList2= list()
    drugResist = list()
    resistantList = list()
    avgResistantList = list()
    for a in range(numViruses):
        virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    #print virusList

    for key in resistances:
        drugResist.append(key)
    print drugResist
            
    for i in range(numTrials):
        patient = TreatedPatient(virusList, maxPop)
        popList = list()

        for j in range(0,150):

            tot = patient.update()
            avgVal = float(tot)
            popList.append(avgVal)
            trialList.append(j)
            resistantpop = patient.getResistPop(drugResist) 
            resistantList.append(float(resistantpop)) 
        
        patient.addPrescription("guttagonol") 
        for x in range(0, 150):
     
            newtot = patient.update()
            avgValNew = float(newtot)
            popList.append(avgValNew)
            #resistantpopNew = patient.getResistPop(drugResist)
            #resistantList.append(float(resistantpopNew))        
    
        avgList.append(popList)
        avgResistantList.append(resistantList)
    print avgList
    print avgResistantList
    for j in range(300):
        i =0
        newVal = 0
        while i !=len(avgList):
            val = avgList[i][j]
            i +=1     
            newVal = newVal+ val
        plotList.append(newVal/len(avgList))
        
    for x in range(300):
        l = 0
        newResistVal = 0 
        while l != len(avgResistantList):
            val = avgResistantList[l][x]
            l +=1     
            newResistVal = newResistVal+ val
        plotList2.append(newResistVal / len(avgResistantList))
    #print plotList2
    #print plotList
    pylab.figure('Virus-Development')
    pylab.title('Avg Virus Populations for 300 steps per trial')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Avg Populations')
    pylab.legend(loc = 'upper center')   

    
    #pylab.plot(plotList)
#===========================================================================

#Create one plot that records both the average total virus population 
#and the average population of guttagonol-resistant virus particles over time.
    #pylab.plot()
    

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    virusList = list()
    popList= list()
    trialList = list()
    avgList = list()
    numList = list()
    for a in range(numViruses):
        virusList.append(SimpleVirus(maxBirthProb, clearProb))
    #print virusList
    
    for i in range(numTrials):   
        patient = Patient(virusList, maxPop)
        #patient.update()
        for j in range(1,301):
            tot = patient.update()
            #newTot = newTot + tot
            avgVal = float(tot)#/float(j)
            popList.append(avgVal)
            trialList.append(j)
        avgList.append(popList)
        #print avgList

    for elem in avgList:
        pylab.plot(elem)

    pylab.figure('Virus-Development')
    pylab.title('Avg Virus Populations for 300 steps per trial')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Avg Populations')
    pylab.legend(loc = 'upper center') 
    pylab.show()
    
        
        
            
