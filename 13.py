f = open('ergasiespython.txt', 'r') 		#open file
data = f.read()                    		#save file's data in data
alphabet = '~`!@#$%^&*()_+-=[]{};:"",./<>?\|123456789'    #creating an alphabet in order to replace them later

for i in data:
	if i in alphabet or i=="'" or i=="" :    #if u find a symbol from our alphabet replace it with space
		data=data.replace(i," ")
print(data)
list1=data.split(" ")                        #creating a list with the words of the txt and the spaces of the aplhabet
#print(list1)

while ('' in list1):                         #we want to be left only with the words of the txt
	for stoixeio in list1:                       #double loop to search all the lenght of the list
		if stoixeio=='' :						 #so we search if there are spaces on the list to remove them
			list1.pop(list1.index(stoixeio))     #remove the spaces from the list
#print(list1)

for i in range (0, len(list1)-1):                #double loop to go through all the lenght of every word
	for j in range(i, len(list1)):				 #and the next word
		if (len(list1[i]) + len(list1[j])) == 20:     #if word1 and word2 have character length=20 print the pair
			print('Character length=20:',"'", list1[i],"'", 'and',"'", list1[j],"'", '!Pair found!')

