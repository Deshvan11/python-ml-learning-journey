#A list is an ordered collection of items (can be of any type).
#Defined using square brackets []
fruits = ["apple", "banana", "cherry"]
print(fruits)
#Accessing elements in a list
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: cherry
#Modifying elements in a list
fruits[1] = "mango"
print(fruits)  # Output: ['apple', 'mango', 'cherry']
#Adding elements to a list
fruits.append("kiwi")
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'kiwi']
#inserting elements at a specific position
fruits.insert(1, "grapes")
print(fruits)  # Output: ['apple', 'grapes', 'mango', 'cherry', 'kiwi']
#Removing elements from a list
fruits.remove("apple")
print(fruits)  # Output: ['grapes', 'mango', 'cherry', 'kiwi']
#Removing elements by index
del fruits[2]
print(fruits)  # Output: ['grapes', 'mango', 'kiwi']
#Popping elements from a list
popped_fruit = fruits.pop(1)
print(popped_fruit)  # Output: mango
print(fruits)  # Output: ['grapes', 'kiwi']
#looping through a list
for fruit in fruits:
    print(fruit)
#List length
print(len(fruits))  # Output: 2
#List slicing
print(fruits[0:2])  # Output: ['grapes', 'kiwi']
#List concatenation
vegetables = ["carrot", "broccoli"]
combined = fruits + vegetables
print(combined)  # Output: ['grapes', 'kiwi', 'carrot', 'broccoli']
#List repetition
repeated_fruits = fruits * 2
print(repeated_fruits)  # Output: ['grapes', 'kiwi', 'grapes', 'kiwi']
#List membership
print("apple" in fruits)  # Output: False
# List methods
print(fruits.count("kiwi"))  # Output: 1
# Sorting a list
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']
# Reversing a list
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']
# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])  # Output: [1, 2, 3]
# Accessing elements in a nested list
print(nested_list[1][2])  # Output: 6
# List comprehensions
# Create a list of even numbers from 0 to 20
evens = [x for x in range(21) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#-------# Practice Task-------------
# Create a list of your 5 favorite movies   
movies = ["Inception", "The Matrix", "Interstellar", "The Shawshank Redemption", "Pulp Fiction"]
# Print the first, middle and last movie in the list
print("First movie:", movies[0])  # First movie
print("Middle movie:", movies[len(movies) // 2])  # Middle movie    
print("Last movie:", movies[-1])  # Last movie
# Add a new movie to the list
movies.append("The Godfather")
print("Updated movie list:", movies)
# Remove one movie from the list
movies.remove("Pulp Fiction")
print("After removal:", movies)
#loop through the list and print each movie
for movie in movies:
    print(movie)
# try slicing the list: print(movies[1:4])
print("Sliced movies:", movies[1:4])  # Slicing the list to get movies from index 1 to 3 #output: ['The Matrix', 'Interstellar', 'The Shawshank Redemption']
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ") #enter"C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\romeo.txt"
fh = open(fname)
lst = []
for line in fh:
    # Remove leading/trailing whitespace and split into words
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
#output: ['Arise', 'But', 'By', 'Come', 'It', 'Juliet', 'O', 'and', 'envious', 'eyes', 'fair', 'from', 'is', 'moon', 'not', 'that', 'the', 'who']