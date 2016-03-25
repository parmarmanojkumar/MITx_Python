"""
 6.00.2x Problem Set 4
"""
# pylint: disable=invalid-name
import pylab
# pylint: disable=E0401, E0602, W0401, W0612
from ps3b import *

#
# PROBLEM 1
#
# pylint: disable=too-many-locals
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # define parameters for patient
    numViruses = 100
    maxPop = 1000
    # define parameters for resistant virus
    clearProb = 0.05
    maxBirthProb = 0.1
    mutProb = 0.005
    resistances = {'guttagonol': False, 'grimpex': False}
    # define step sizes for variable administration
    step1 = [300, 150, 75, 0]
    step2 = 150
    # for runtime improvement, use tmpStep tmpTrial in while than for loop
    tmpStep = 0
    tmpTrial = 0
    # to use subplot function
    subPlot = 0
    # for each variable step size run trials
    for step in step1:
        print "Simulation for step size : ", step
        # initialize viruses
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, \
                                mutProb)]* numViruses
        # initialize virus count to take virus population at end of trial
        virusCount = []
        tmpTrial = numTrials
        # run number of trials
        while tmpTrial > 0:
            # initialize patient for given trial
            patient = TreatedPatient(viruses, maxPop)
            # run 150 timesteps to check growth of viruses
            tmpStep = step
            while tmpStep > 0:
                patient.update()
                tmpStep -= 1
            # administer guttagonol to check impact of it on viruses
            patient.addPrescription("guttagonol")
            # run 150 timesteps to check growth of viruses
            tmpStep = step2
            while tmpStep > 0:
                patient.update()
                tmpStep -= 1
            # check and log the virus population at end of trial
            virusCount.append(patient.getTotalPop())
            tmpTrial -= 1
            # end of a given trial run
        print "End of Trial for step size : ", step
        # preparation of histogram for the variable step size
        subPlot += 1
        pylab.subplot(2, 2, subPlot)
        # each bin of size 50
        pylab.hist(virusCount, bins=12, range=(0, 600))
        pylab.title("Drug ddministration delay : %s"%step)
        pylab.xlabel("Final virus count")
        pylab.ylabel("# trials")
        # end of  trial for variable step size
    pylab.tight_layout()
    pylab.show()
    return None
# pylint: enable=too-many-locals


#
# PROBLEM 2
#
# pylint: disable=too-many-locals
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # define parameters for patient
    numViruses = 100
    maxPop = 1000
    # define parameters for resistant virus
    clearProb = 0.05
    maxBirthProb = 0.1
    mutProb = 0.005
    resistances = {'guttagonol': False, 'grimpex': False}
    # define step sizes for variable administration
    step1 = 150
    step2 = [300, 150, 75, 0]
    step3 = 150
    # for runtime improvement, use tmpStep tmpTrial in while than for loop
    tmpStep = 0
    tmpTrial = 0
    # to use subplot function
    subPlot = 0
    # for each variable step size run trials
    for step in step2:
        print "Simulation for step size : ", step
        # initialize viruses
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, \
                                mutProb)]* numViruses
        # initialize virus count to take virus population at end of trial
        virusCount = []
        tmpTrial = numTrials
        # run number of trials
        while tmpTrial > 0:
            # initialize patient for given trial
            patient = TreatedPatient(viruses, maxPop)
            # run 150 timesteps to check growth of viruses
            tmpStep = step1
            while tmpStep > 0:
                patient.update()
                tmpStep -= 1
            # administer guttagonol to check impact of it on viruses
            patient.addPrescription("guttagonol")
            # run trial specific timesteps to check impact of it on viruses
            tmpStep = step
            while tmpStep > 0:
                patient.update()
                tmpStep -= 1
            # administer grimpex to check impact of it on viruses
            patient.addPrescription("grimpex")
            # run 150 timesteps to check growth of viruses
            tmpStep = step3
            while tmpStep > 0:
                patient.update()
                tmpStep -= 1
            # check and log the virus population at end of trial
            virusCount.append(patient.getTotalPop())
            tmpTrial -= 1
            # end of a given trial run
        print "End of Trial for step size : ", step
        # preparation of histogram for the variable step size
        subPlot += 1
        pylab.subplot(2, 2, subPlot)
        pylab.hist(virusCount, bins=50)
        pylab.title("Drug Administration Delay : %s"%step)
        pylab.xlabel("Virus Frequency")
        pylab.ylabel("Trials")
        # end of  trial for variable step size
    pylab.tight_layout()
    pylab.show()
    return None
# pylint: enable=too-many-locals

# this implementation is slower by 3 seconds when running ith 100 samples.
## PROBLEM 2
##
## pylint: disable=too-many-locals
#def simulationTwoDrugsDelayedTreatment(numTrials):
#    """
#    Runs simulations and make histograms for problem 2.
#
#    Runs numTrials simulations to show the relationship between administration
#    of multiple drugs and patient outcome.
#
#    Histograms of final total virus populations are displayed for lag times of
#    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
#    150 timesteps of simulation).
#
#    numTrials: number of simulation runs to execute (an integer)
#    """
#    # define parameters for patient
#    numViruses = 100
#    maxPop = 1000
#    # define parameters for resistant virus
#    clearProb = 0.05
#    maxBirthProb = 0.1
#    mutProb = 0.005
#    resistances = {'guttagonol': False, 'grimpex': False}
#    # define step sizes for variable administration
#    step1 = 150
#    step2 = [300, 150, 75, 0]
#    step3 = 150
#    # for runtime improvement, use tmpStep tmpTrial in while than for loop
#    tmpCount = 0
#    tmpTrial = 0
#    # to use subplot function
#    subPlot = 0
#    # for each variable step size run trials
#    for step in step2:
#        print "Simulation for step size : ", step
#        # initialize viruses
#        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, \
#                                mutProb)]* numViruses
#        # initialize virus count to take virus population at end of trial
#        virusCount = []
#        tmpTrial = numTrials
#        # run number of trials
#        while tmpTrial > 0:
#            totalStep = step1 + step + step3
#            tmpCount = runOneTrialTwoDrugSimulation(numViruses, maxPop, maxBirthProb,
#                                      clearProb, resistances, mutProb, step1,step,
#                                      totalStep)
#            virusCount.append(tmpCount)
#            tmpTrial -= 1
#            # end of a given trial run
#        print "End of Trial for step size : ", step
#        # preparation of histogram for the variable step size
#        subPlot += 1
#        pylab.subplot(2, 2, subPlot)
#        # each bin of size 50
#        pylab.hist(virusCount, bins=12, range=(0, 600))
#        pylab.title("Drug ddministration delay : %s"%step)
#        pylab.xlabel("Final virus Count")
#        pylab.ylabel("# trials")
#        # end of  trial for variable step size
#    pylab.tight_layout()
#    pylab.show()
#    return None
#
#def runOneTrialTwoDrugSimulation(numViruses, maxPop, maxBirthProb, clearProb, \
#                                     resistances, mutProb, \
#                                     numStepsBeforeDrugOneApplied, \
#                                     numStepsBeforeDrugTwoApplied, \
#                                     totalNumSteps):
#    """
#    Helper function for doing one actual simulation run with drugs applied
#    """
#
#    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, \
#                                mutProb)]* numViruses
#
#    patient = TreatedPatient(viruses, maxPop)
#
#
#
#    step1 = totalNumSteps - numStepsBeforeDrugOneApplied
#    step2 = step1 - numStepsBeforeDrugTwoApplied
#
#
#    while totalNumSteps > 0:
#        if step1 == totalNumSteps:
#            patient.addPrescription("guttagonol")
#        if step2 == totalNumSteps:
#            patient.addPrescription("grimpex")
#        patient.update()
#        totalNumSteps -= 1
#
#    return patient.getTotalPop()
simulationDelayedTreatment(100)
#simulationTwoDrugsDelayedTreatment(100)
