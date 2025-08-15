import re
# Open the file in read mode

fn = input("Enter file name: ") #Enter file name: c:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\regex_sum_2277849.txt
fh = open(fn)
inp= fh.read()
lst = list()
y = re.findall('[0-9]+',inp)  # Find all sequences of digits
i = [int(l) for l in y]
get = lst.append(y)

    
#sum of all the numbers which where converted from string to integer from the given file.
sum = sum(i)
print("Sum of all the numbers in the file is:", sum) #Sum of all the numbers in the file is: 45
print("numbers in the files as list:", lst) #numbers in the files as list: ['9', '41', '12', '9', '5', '9']

