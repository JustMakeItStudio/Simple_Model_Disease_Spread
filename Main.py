from Person import Person
from numpy.random import randint, rand
from random import getrandbits, choice
from matplotlib import pyplot as plt
import pygame
from time import sleep

# Don't change these variables
NumberOfPeriods = 0
TotalNumberOfInfectedPerPeriod = [0]
TotalNumberOfDeaths = [0]
positionsX = []
positionsY = []
persons = []
fontColor = (172, 163, 159) # Grayish
backgroundColor = (33, 17, 23) # Dark Purple
deadColor = (207, 51, 30) # Red
infectedColor = (242, 157, 44) # Orange

# Change these variables to see the resulting outcome
NumberOfPersons = 300
WindowDimensions = (900,700) # width and hight
InitialTransitioning = [0,0,0,0,0,0,0,1,1,1] # 1 / 10 = 10% of persons will be in the transitioning stage at period 0
SleepTimeBetweenPeriods = 0.08 # seconds
MaxPosibleMovementPerPeriod = 15
CircleRadius = 4 # pixels
TransitionPeriods = 12
CriticalDistanceOfInfection = 15 # pixels
WillLastPeriodsInfected = 20
CanHeal = [0,0,0,0,0,1,1,1,1,1] # initialized at 50%


if __name__ == "__main__":
    # Setup the static variables of the person class 
    Person(setup=True, CriticalDistanceOfInfection=CriticalDistanceOfInfection, TransitionPeriods=TransitionPeriods, CanHeal=CanHeal, WillLastPeriodsInfected=WillLastPeriodsInfected, LimitX=WindowDimensions[0]-260, LimitY=WindowDimensions[1]-10)
    pygame.init()
    
    font = pygame.font.SysFont(None, 24)

    WIN = pygame.display.set_mode((WindowDimensions[0], WindowDimensions[1]))
    pygame.display.set_caption('Transmition of Disease')
    
    for i in range(NumberOfPersons):
        positionsX.append(randint(WindowDimensions[0]))
        positionsY.append(randint(WindowDimensions[1]))
        persons.append(Person(posx=positionsX[i], posy=positionsY[i], isTransitioning=bool(choice(InitialTransitioning))))

    running = True
    while (running):
        sleep(SleepTimeBetweenPeriods)
        
        pygame.display.update() # updates the screen
        WIN.fill(backgroundColor)

        NumberOfPersons_txt = font.render(f'Number Of Persons: {NumberOfPersons}', True, fontColor)
        WIN.blit(NumberOfPersons_txt, (WindowDimensions[0]-250, 10))
        InitialTransitioning_txt = font.render(f'Initial Transitioning: {100*sum(InitialTransitioning)/10}%', True, fontColor)
        WIN.blit(InitialTransitioning_txt, (WindowDimensions[0]-250, 30))
        TransitionPeriods_txt = font.render(f'Transition Periods: {TransitionPeriods}', True, fontColor)
        WIN.blit(TransitionPeriods_txt, (WindowDimensions[0]-250, 50))
        CriticalDistanceOfInfection_txt = font.render(f'Critical Infection Distance: {CriticalDistanceOfInfection}px', True, fontColor)
        WIN.blit(CriticalDistanceOfInfection_txt, (WindowDimensions[0]-250, 70))
        MaxPosibleMovementPerPeriod_txt = font.render(f'Max Movement: {MaxPosibleMovementPerPeriod}px/period', True, fontColor)
        WIN.blit(MaxPosibleMovementPerPeriod_txt, (WindowDimensions[0]-250, 90))
        WillLastPeriodsInfected_txt = font.render(f'Infection Span: 0-{WillLastPeriodsInfected}periods', True, fontColor)
        WIN.blit(WillLastPeriodsInfected_txt, (WindowDimensions[0]-250, 110))
        CanHeal_txt = font.render(f'People That Can Heal: {100*sum(CanHeal)/10}%', True, fontColor)
        WIN.blit(CanHeal_txt, (WindowDimensions[0]-250, 130))
        TotalNumberOfDeaths_txt = font.render(f'Total Deaths: {TotalNumberOfDeaths[-1]}', True, deadColor)
        WIN.blit(TotalNumberOfDeaths_txt, (WindowDimensions[0]-250, 150))
        TotalNumberOfInfectedPerPeriod_txt = font.render(f'Total Infected Now: {TotalNumberOfInfectedPerPeriod[-1]}', True, infectedColor)
        WIN.blit(TotalNumberOfInfectedPerPeriod_txt, (WindowDimensions[0]-250, 170))
        NumberOfPeriods_txt = font.render(f'Period Number: {NumberOfPeriods}', True, fontColor)
        WIN.blit(NumberOfPeriods_txt, (WindowDimensions[0]-250, 190))

        ev = pygame.event.get() # get all events
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()
   
        for i in range(NumberOfPersons):
            move = [MaxPosibleMovementPerPeriod*(rand()-0.5), MaxPosibleMovementPerPeriod*(rand()-0.5)]
            persons[i].updatePerson(move)
            positionsX[i] = persons[i].posx
            positionsY[i] = persons[i].posy
            if not persons[i].isDead:
                if persons[i].isInfected:
                    color = deadColor # Red
                elif persons[i].isTransitioning:
                    color = infectedColor # Orange
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




