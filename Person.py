from numpy.random import randint
from random import getrandbits, choice


class Person:
    TotalDeaths = 0
    TotalInfectedNow = 0
    TransitionPeriods = 12
    CriticalDistanceOfInfection = 10 # pixels
    WillLastPeriodsInfected = 50
    CanHeal = [0,0,0,0,0,1,1,1,1,1] # initialized at 50%
    LimitY = 500 # pixels
    LimitX = 500 # pixels


    def __init__(self,posx=None, posy=None, isTransitioning=None, setup=False, CriticalDistanceOfInfection=None, TransitionPeriods=None, CanHeal=None, WillLastPeriodsInfected=None, LimitX=None, LimitY=None):
        if setup:
            Person.CriticalDistanceOfInfection = CriticalDistanceOfInfection
            Person.TransitionPeriods = TransitionPeriods
            Person.CanHeal = CanHeal
            Person.WillLastPeriodsInfected = WillLastPeriodsInfected
            Person.LimitY = LimitY
            Person.LimitX = LimitX
        else:
            self.posx = posx
            self.posy = posy
            self.isInfected = False
            self.isTransitioning = isTransitioning
            self.transitionPeriods = 0
            self.periodsInfected = 0
            self.WillLastPeriodsInfected = randint(Person.WillLastPeriodsInfected)
            self.isDead = False
            self.CanHeal = bool(choice(Person.CanHeal))
            # print(f'posx:{self.posx}, posy:{self.posy}, isInfected:{self.isInfected}, isTransitioning:{self.isTransitioning}, transitionPeriods:{self.transitionPeriods}, periodsInfected:{self.periodsInfected}, WillLastPeriodsInfected:{self.WillLastPeriodsInfected}, isDead:{self.isDead}.')


    def updatePerson(self, move):
        if (not self.isDead):
            self.checkIsTransitioning()
            self.checkIsInfected()
            
            self.giveMovement(move)
            self.checkIsDead()
            self.checkIsHealed()
            # print(f'posx:{self.posx}, posy:{self.posy}, isInfected:{self.isInfected}, isTransitioning:{self.isTransitioning}, transitionPeriods:{self.transitionPeriods}, periodsInfected:{self.periodsInfected}, WillLastPeriodsInfected:{self.WillLastPeriodsInfected}, isDead:{self.isDead}.')

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
        if not self.isDead and self.CanHeal:
            if self.periodsInfected >= self.WillLastPeriodsInfected/2:
                self.isInfected = False
                self.periodsInfected = 0
                self.transitionPeriods = 0
                Person.TotalInfectedNow = Person.TotalInfectedNow - 1 

    def checkIsDead(self):
        if (self.isDead or self.periodsInfected >= self.WillLastPeriodsInfected):
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
    

