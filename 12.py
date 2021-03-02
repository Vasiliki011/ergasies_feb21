"""
Επειδή η πλειοψηφία των κατοπτρικών χαρακτήρων έχουν τιμή(int) 130 και πάνω,
αντιστοιχούν στον extended ASCII code, δηλαδή στα διάφορα σύμβολα,
οπότε είναι λογικό στο τελικό αποτέλεσμα να βρίσκονται τα σύμβολα αυτά ή ακόμη και
κουτάκια που στην ουσία παραμπέμπουν και αυτά στα ίδια σύμβολα.
"""
f = open('ergasiespython.txt', 'r') #open file
data = f.read()                     #save file's data in data
#print(data)
list1=[]
for i in range(len(data)):
    x = 255 - ord(data[i])          #pername sto x ton katoptriko tou ascii tou kathe stoixeiou tou txt
    list1.append(x)                 #dimiourgia listas me ta katoptrika ascii

print(list1)
list1=list1[::-1]                   #allazw twra tin seira twn dedomenwn apo kanoniki se anapodi
for i in list1:                     #gia na ta ektipwsw kateutheian me antestrammeni seira meta
    print("".join(chr(i)),end='')   #metatropi tou ascii se text kai ektiposi telikou zitoumenou



