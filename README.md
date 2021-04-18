# Simple Model of Disease Spread
A simple two dimensional simulation of the spread of a disease displayed by a basic visualization method. 


Build in Python 3.
## The aim
Is to recreate the natural way of disease transmision and return different statistics graphs.

### Actual implementation
An area is created with a number of entities inside it. The boundaries are periodic boundary conditions, meaning thw area is looping on it self. Each entity has some attributes that describe its state (dead, infected, can heal, etc.). In addition, every entity can move randomly. Now, by defining a critical distance between two entities, the transmision of the disease is simulated. Also, each entity has a random delay from the time of contact with an infected till the time of actually been infected and gaining the ability to infect further, called the transision period. Finally, the entities are displayed as circles, the colors are white-not infected, blue-transitioning, red-infected. 
 

#### Libraries used:
- [pygame]
- [time]
- [random]
- [numpy]
- [matplotlib]

### Installation and Execution
To run the code, you need Python3 and the libraries above installed on your computer.
To install a libray for python open the command prompt and follow the example bellow.

```sh
$ pip install pygame
```
To execute the simulataion navigate to the Main.py file, you can then change different parameters like the number of entities (NumberOfPersons), etc., and run the Main.py file.
You can stop the simulation by exiting the window created, afterwards the statistics graphs are displayed.

To clone the repository, open the command prompt at the directory of choise and type:
```sh
$  git clone --recursive https://github.com/rocku0/Simple_Model_Disease_Spread.git
```
### An example with 150 Periods and 1000 Entities:
![image](https://user-images.githubusercontent.com/71210416/114858845-aa50ca80-9df2-11eb-8a56-acf01165c069.png)


### An example with 1038 Periods and 1000 Entities with different settings:
![image](https://user-images.githubusercontent.com/71210416/115117150-d06a9c00-9fa5-11eb-8e5e-fc5764cbf2a0.png)


### An example with 1038 Periods and 500 Entities with different settings:
![image](https://user-images.githubusercontent.com/71210416/115155837-4ba57e00-a08a-11eb-9e23-d71ad9f7fc2b.png)

**Use this as you like.**

   [pygame]: <https://www.pygame.org/docs/>
   [time]: <https://docs.python.org/3/library/time.html>
   [random]: <https://docs.python.org/3/library/random.html>
   [matplotlib]: <https://matplotlib.org/stable/contents.html>
   [numpy]: <https://numpy.org/doc/>
