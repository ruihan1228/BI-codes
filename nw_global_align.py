#This is the Needleman-Wunsch global alignment algorithm without gaps in the model
# and with match value = 1, and mismatch value = -1, and indel(gap) value = -2
import numpy as np

string1 = "AATTAGGTTGA"
string2 = "ATAATCGTTAA"
#split up the line into individual characters
#and place the characters into a list, whose
#first index is 0
charlist_string1 = list(string1)
charlist_string2 = list(string2)
print("The lengths of the two strings are " + str(len(string1)) + " and " + str(len(string2)) + "\n")

#Set penalties
match = 1
mismatch = 1
gap = 2

#Initialize the matrix
#create an additional matrix with the same size to save the "arrow" for tracing or considering gaps
nrow = len(string1) + 1
ncol = len(string2) + 1

V = np.zeros((nrow,ncol))

#Initialize the first col
for i in range(nrow):
    V[i][0] = -i * gap

#Initialize the first row
for j in range(ncol):
    V[0][j] = -j * gap
#print(V)

for i in range(1, nrow):
    for j in range(1, ncol):
        # horizontal: add gap and assign to current max value
        current_max_value = V[i-1][j] - gap
        # vertical: add gap and compare with current max value
        if current_max_value < (V[i][j-1] - gap):
            current_max_value = V[i][j-1] - gap
        # diagonal: add match/mismatch and compare with current max value
        if charlist_string1[i-1] == charlist_string2[j-1]:
            if current_max_value < (V[i-1][j-1] + match):
                current_max_value = V[i-1][j-1] + match
        else:
            if current_max_value < (V[i-1][j-1] - mismatch):
                current_max_value = V[i-1][j-1] - mismatch
        V[i][j] = current_max_value

print(V)

print("The similarity value of the two strings is " + str(V[nrow-1][ncol-1]) + "\n")
#print(np.transpose(V), file = open('output.txt', 'a'))


