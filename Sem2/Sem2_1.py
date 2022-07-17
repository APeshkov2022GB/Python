# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
   
# number = int(input("Введите количество шагов: "))

# def list_from(number: int):
#     list_numbers = []
#     for element in range (0, number):
#         list_numbers.append((-3)**element)
#     return list_numbers

# print(list_from(number))
  
# #--------------------------------------------------------------------------------

def sequence(n: int):
    sequence_list = [1]
    i = 0
    while i < n-1:
        sequence_list.append(sequence_list[i]*-3)
        i += 1
    return sequence_list


n = int(input('Введите n: '))
print(sequence(n))

# #-----------------------------------------------------------


# def Input_values(write_what_you_want: str):
#     for_checking = False
#     while not for_checking:
#         try:
#             number = int(input(f'{write_what_you_want}'))
#             for_checking = True
#         except ValueError:
#             print("Попробуй снова. Ты должен ввести число.")
#     return number

# def progression(N:int):
#     help_number = 1
#     for i in range(N):
#         print(help_number)
#         help_number = help_number * -3

# number_N = Input_values("Введите число N: ")
# progression(number_N)
