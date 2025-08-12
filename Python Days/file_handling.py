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
