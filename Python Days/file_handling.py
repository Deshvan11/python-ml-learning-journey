# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fn = input("Enter file name: ") #Enter file name: C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\mbox-short.txt
fh = open(fn)
inp= fh.read()

for letter in fh:
    letter= letter.rstrip()
    h=(letter.upper())
    print(h)

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ") #Enter file name: C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\mbox-short.txt
fh = open(fname)
confidence_count = 0
confidence_total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Find where the value starts on the line
    colon_pos = line.find(':')
    value_str = line[colon_pos+1:].strip()
    value = float(value_str)
    confidence_count += 1
    confidence_total += value

if confidence_count > 0:
    print("Average spam confidence:", confidence_total / confidence_count)
else:

    print("No valid X-DSPAM-Confidence lines in file.")


# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
fname = input("Enter file name: ") #Enter file name: C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\mbox-short.txt
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"Error: File '{fname}' not found.")
    exit() # Exit the program if the file is not found

count = 0
for line in fh:  # Corrected: Iterate through lines in the file handle 'fh'
    line = line.strip() # Remove leading/trailing whitespace, including newline characters
    if not line.startswith("From:"): # Assuming "From" is the desired prefix, case-sensitive
        continue
    words = line.split()
    
    print(words[1])
    count += 1# Increment count for lines that start with "From"


print("There were",count,"lines in the file with From as the first word")
fh.close() # Close the file when done
#output:
#Enter file name: C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\mbox-short.txt
#output: stephen.marquard@uct.ac.za 
######  There were 27 lines in the file with From as the first word


#Dictionaries:
#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Open the file (replace filename if needed)
fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"Error: File '{fname}' not found.")
    exit()

senders = {}  # Dictionary to store sender counts

for line in fh:
    line = line.strip()
    if not line.startswith('From '):  # Note the space after 'From'
        continue
    words = line.split()
    if len(words) < 2:
        continue  # Skip malformed lines
    sender = words[1]
    senders[sender] = senders.get(sender, 0) + 1  # Increment count

# Find the sender with the highest count
max_count = 0
max_sender = None
for sender, count in senders.items():
    if count > max_count or max_sender is None:
        max_count = count
        max_sender = sender

# Output the result
print(max_sender, max_count)

fh.close()
#output:
#Enter file name: C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\mbox-short.txt
#output: cwen@iupui.edu 5


# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below

# Open the file
fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"Error: File '{fname}' not found.")
    exit()

hour_counts = {}  # Dictionary to count emails by hour

for line in fh:
    line = line.strip()
    if not line.startswith('From '):
        continue
    # Split the line into words, e.g.: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    words = line.split()
    if len(words) < 6:  # Ensure line is well-formed
        continue
    # Extract time, e.g., '09:14:16'
    time = words[5]
    # Split by ':' to get hours, minutes, seconds
    hour = time.split(':')[0]
    # Update counter
    hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort dictionary by hour (key)
sorted_hours = sorted(hour_counts.items())

# Print results
for hour, count in sorted_hours:
    print(hour, count)

#output:
#Enter file name: C:\Users\TANMAY\OneDrive\Documents\GitHub\python-ml-learning-journey\Python Days\mbox-short.txt
#output:
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1  