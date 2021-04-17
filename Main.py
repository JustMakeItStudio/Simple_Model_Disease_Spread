from Person import Person
from numpy.random import randint, rand
from random import getrandbits, choice
from matplotlib import pyplot as plt
import pygame
from time import sleep

# Don't change these variables
NumberOfPeriods = 0
TotalNumberOfInfectedPerPeriod = []
TotalNumberOfDeaths = []
positionsX = []
positionsY = []


# Change these variables to see the resulting outcome
NumberOfPersons = 1000
WindowDimensions = (700,700) # width and hight
InitialTransitioning = [0,0,0,0,0,0,0,0,0,1] # 1 / 10 = 10% of persons will be in the transitioning stage at period 0
SleepTimeBetweenPeriods = 0.001 # seconds
MaxPosibleMovementPerPeriod = 15
CircleRadius = 4 # pixels
TransitionPeriods = 12
CriticalDistanceOfInfection = 10 # pixels
willLastPeriodsInfected = 60
canHeal = [0,1,1,1,1,1,1,1,1,1] # initialized at 50%


if __name__ == "__main__":
    # Setup the static variables of the person class 
    Person(setup=True, CriticalDistanceOfInfection=CriticalDistanceOfInfection, TransitionPeriods=TransitionPeriods, canHeal=canHeal, willLastPeriodsInfected=willLastPeriodsInfected, LimitX=WindowDimensions[0], LimitY=WindowDimensions[1])
    pygame.init()
    WIN = pygame.display.set_mode((WindowDimensions[0], WindowDimensions[1]))
    pygame.display.set_caption('Transmition of Disease')
    persons = []
    for i in range(NumberOfPersons):
        positionsX.append(randint(WindowDimensions[0]))
        positionsY.append(randint(WindowDimensions[1]))
        persons.append(Person(posx=positionsX[i], posy=positionsY[i], isTransitioning=bool(choice(InitialTransitioning))))

    running = True
    while (running):
        sleep(SleepTimeBetweenPeriods)
        pygame.display.update() # updates the screen
        WIN.fill((0,0,0))
        ev = pygame.event.get() # get all events
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()

        print(f"------ Period: {NumberOfPeriods} ------")   
        for i in range(NumberOfPersons):
            move = [MaxPosibleMovementPerPeriod*(rand()-0.5), MaxPosibleMovementPerPeriod*(rand()-0.5)]
            persons[i].updatePerson(move)
            positionsX[i] = persons[i].posx
            positionsY[i] = persons[i].posy
            if not persons[i].isDead:
                if persons[i].isInfected:
                    color = (150,30,50) # Red
                elif persons[i].isTransitioning:
                    color = (10,50,150) # Blue
                else:
                    color = (255,255,255) # White
                pygame.draw.circle(WIN, color, center=(positionsX[i], positionsY[i]), radius=CircleRadius)


        for i in range(NumberOfPersons):
            for j in range(NumberOfPersons-i):
                persons[i].checkSouround(persons[j])
       
        TotalNumberOfDeaths.append(Person.TotalDeaths)  
        TotalNumberOfInfectedPerPeriod.append(Person.TotalInfectedNow)
        # print(f"-------------- Total number of infected: {Person.TotalInfectedNow}")
        # print(f"-------------- Total number of Deaths: {Person.TotalDeaths}")
        NumberOfPeriods = NumberOfPeriods + 1


    plt.figure(1)

    plt.subplot(211)
    plt.plot(TotalNumberOfInfectedPerPeriod)
    plt.ylabel("Number of Infected People")
    # plt.xlabel("Periods")

    plt.subplot(212)
    plt.plot(TotalNumberOfDeaths)
    plt.ylabel("Number of Dead People thus far")
    plt.xlabel("Periods")
    plt.show()




