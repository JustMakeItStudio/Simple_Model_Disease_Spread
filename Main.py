from Person import Person
from numpy.random import randint, rand
from random import getrandbits, choice
from matplotlib import pyplot as plt
import pygame
from time import sleep

NumberOfPeriods = 0
NumberOfPersons = 1000
TotalNumberOfInfectedPerPeriod = []
TotalNumberOfDeaths = []
positionsX = []
positionsY = []

if __name__ == "__main__":
    # hero = Person(250,250,True)
    pygame.init()
    WIN = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Transmition of Disease')
    persons = []
    for i in range(NumberOfPersons):
        positionsX.append(randint(500))
        positionsY.append(randint(500))
        persons.append(Person(posx=positionsX[i], posy=positionsY[i], isTransitioning=bool(choice([0,0,0,0,0,0,0,0,0,1]))))

    running = True
    while (running):
        sleep(0.1)
        pygame.display.update() # updates the screen
        WIN.fill((0,0,0))
        ev = pygame.event.get() # get all events
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()

        print(f"------ Period: {NumberOfPeriods} ------")   
        for i in range(NumberOfPersons):
            move = [15*(rand()-0.5), 15*(rand()-0.5)]
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
                pygame.draw.circle(WIN, color, center=(positionsX[i], positionsY[i]), radius=6)


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




