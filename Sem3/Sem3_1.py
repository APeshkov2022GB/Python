# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.
# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1



# org_text = ["qwe", "asd", "zxc", "qwe", "ertqwe"] 
# # org_text = input("Введите строку: ")
# find_text = input("Введите искомую строку: ")

# def text_finder(org_text: str, find_text: str):
#     counter = 0
#     for index in range (0, len(org_text) - len(find_text)+1):
#         if find_text in org_text[index:index+len(find_text)]: counter += 1
#     return counter

# print(f"Текст '{find_text}' втречается в тексте {text_finder(org_text, find_text)} раз")
подходит
#--------------------------------------------------------------------------------------------

str_list = ['12asd36', '256', 'dsds89358', '5698a']

s_nym = input('Enter the number: ')
is_Found = False

for item in str_list:
    print(item)
    if item.__contains__(s_nym):
        is_Found = True
        break

print(is_Found)



# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

list = ['123', '321', '456', '96']
count = '3'
array_find = []

for find_count in list:
    if count in find_count:
        array_find.append(find_count)
print(array_find)

