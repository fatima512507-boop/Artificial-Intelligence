#Name: Fatima            BSAI(3A)
#ROll no: SU92-BSAIM-S25-025

#TASK 2:


for num in range(1, 101):

    if num % 3==0 and num % 5==0:
        print("Fizz Buzz")

    elif num % 3==0:
        print("Fizz")    
    
    elif num % 5==0:
        print("Buzz") 

    else:
        print(num)    





# Movie Budget:


movies =[
    ("Enternal Sunshine of the spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ulron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

n = int(input("How many movies do you want to add? "))

for i in range(n):
    name=input("Enter movie name:")
    budget=int(input("Enter movie budget"))
    movies.append(name,budget)

total=0

for movie in movies:
    total+=movies[1]

average = total/ len(movies)

print("\n Average Budget =", average)


count=0

print("\n \movies with above average budget:\n")


for movie in movies:
    name= movie[0]
    budget= movie[1]


    if budget>average:
        difference=budget-average
        print("name is higher than budgrt by", difference)
        count+=1


print("\n Number of movies above Average Budget =", count)
