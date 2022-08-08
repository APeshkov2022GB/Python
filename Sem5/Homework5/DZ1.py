# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
find = 'абв'

word = word.split()
print(word)

f = lambda x: not x.count(find) > 0 
lst = list(filter(f, word))
print('lst = ',lst)

str_new = ' '.join(lst)
print(str_new)