from numpy.random import randint
from random import getrandbits, choice


class Person:
    TotalDeaths = 0
    TotalInfectedNow = 0
    TransitionPeriods = 12
    CriticalDistanceOfInfection = 10
    LimitY = 500
    LimitX = 500


    def __init__(self,posx, posy, isTransitioning):
        self.posx = posx
        self.posy = posy
        self.isInfected = False
        self.isTransitioning = isTransitioning
        self.transitionPeriods = 0
        self.periodsInfected = 0
        self.willLastPeriodsInfected = randint(50)
        self.isDead = False
        self.canHeal = bool(choice([0,0,0,0,0,1,1,1,1,1]))
        # print(f'posx:{self.posx}, posy:{self.posy}, isInfected:{self.isInfected}, isTransitioning:{self.isTransitioning}, transitionPeriods:{self.transitionPeriods}, periodsInfected:{self.periodsInfected}, willLastPeriodsInfected:{self.willLastPeriodsInfected}, isDead:{self.isDead}.')


    def updatePerson(self, move):
        if (not self.isDead):
            self.checkIsTransitioning()
            self.checkIsInfected()
            self.checkIsHealed()
            self.giveMovement(move)
            self.checkIsDead()
            # print(f'posx:{self.posx}, posy:{self.posy}, isInfected:{self.isInfected}, isTransitioning:{self.isTransitioning}, transitionPeriods:{self.transitionPeriods}, periodsInfected:{self.periodsInfected}, willLastPeriodsInfected:{self.willLastPeriodsInfected}, isDead:{self.isDead}.')

    def giveMovement(self, move):
        if not self.isDead:
            self.posx = self.posx + move[0]
            self.posy = self.posy + move[1]
            if self.posx > Person.LimitX + 1:
                self.posx = 0
            elif self.posx < 0 - 1:
                self.posx = Person.LimitX
            if self.posy > Person.LimitY + 1:
                self.posy = 0
            elif self.posy < 0 - 1:
                self.posy = Person.LimitY 

    def checkSouround(self, otherPerson):
        if not self.isDead and not otherPerson.isDead:
            if self.isInfected or otherPerson.isInfected:
                if Person.CriticalDistanceOfInfection > round(abs(self.posx - otherPerson.posx)) and Person.CriticalDistanceOfInfection > round(abs(self.posy - otherPerson.posy)):
                    if not self.isInfected:
                        self.isTransitioning = True
                    if not otherPerson.isInfected:
                        otherPerson.isTransitioning = True

    def checkIsHealed(self):
        if not self.isDead and self.canHeal:
            if self.periodsInfected >= self.willLastPeriodsInfected/2:
                self.isInfected = False
                self.periodsInfected = 0
                self.transitionPeriods = 0
                Person.TotalInfectedNow = Person.TotalInfectedNow - 1 

    def checkIsDead(self):
        if (self.isDead or self.periodsInfected >= self.willLastPeriodsInfected):
            self.isDead = True
            self.isInfected = False
            self.periodsInfected = 0
            self.transitionPeriods = 0
            Person.TotalDeaths = Person.TotalDeaths + 1
            Person.TotalInfectedNow = Person.TotalInfectedNow - 1    

    def checkIsInfected(self):
        if (self.isInfected):
            self.periodsInfected = self.periodsInfected + 1
    
    def checkIsTransitioning(self):
        if (self.isTransitioning):
            self.transitionPeriods = self.transitionPeriods + 1
            if (self.transitionPeriods >= Person.TransitionPeriods):
                self.isTransitioning = False
                self.isInfected = True
                self.periodsInfected = 0
                self.transitionPeriods = 0
                Person.TotalInfectedNow = Person.TotalInfectedNow + 1
    

