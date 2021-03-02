import string
import collections
f = open('ergasiespython.txt', 'r') #open file
data = f.read()                     #save file's data in data
print(data)
list1=[]
for i in range(len(data)):
    x=ord(data[i])
    if x%2 == 1 :                   #create list with the odd ascii numbers
        list1.append(x)
print(list1)                        #print the list with the odd ascii numbers

def count_letters(text_file):
    alphabet = string.ascii_letters + string.digits + string.punctuation #letters,digits,special characters
    alphabet_set = set(alphabet)
    counts = collections.Counter(c for c in text_file if c in alphabet_set)
    list = []                     #This list will contain the letters and their probability
    for letter in alphabet:       #Calculating probability
        total = sum(counts.values())
        prob = counts[letter] / total
        if counts[letter] != 0:   #Discard the letters with zero probability
            list.append(letter)
            list.append("%.2f" % round(prob, 2))  #Rounding and using only two decimal places
    return list
counts = count_letters(data)
#print (counts)                 #The original list containing all letters and probabilities

for i in counts:
    a = ''.join(list(i))         #Seperate the data and their probabilities in 2 lines
    if len(a)==1:               #Only get the line with the data's character
        print(a + ':')
    else:                       #Only get the line with the probabilities
        b= list(i)[-2: ]        #Get the last 2 digits of the probability
        c=(''.join(b))
        #print(c + "%")         #Printing and converting the probability to the 100% scale
        star='*'
        print(star * int(c))    #Print as many stars as the probability value. For example: 8% = 8 stars

#f.close()
