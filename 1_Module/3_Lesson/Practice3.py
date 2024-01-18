#Кожен пише суму списку за допомогою for та While
print('Task 1/5 \n')
print ('Цикл for')
my_list = [1, 2, 3, 4, 5, 6]
total = 0

for num in my_list:
    total += num
print (f'Загальна сумма: {total} \n')
print ('Цикл While')
my_list2 = [7, 8, 9, 10, 11, 12]
list_sum = 0
index = 0

while index < len(my_list):
    list_sum += my_list2[index]
    index += 1

print ("Сума елементів списку:", list_sum)
print()

#Банкомат видає суму максимально можливими купюрами
print ('Task 4/5')

in_sum = int(input('Введіть суму, яку бажаєте отримати готівкою: '))
thousands = (in_sum % 1000000) // 1000 #тисячні
print ('1000 грн X', thousands, 'купюр')
hundreds = (in_sum % 1000) // 100 #Сотні
print('100 грн X', hundreds, 'купюр')
tens = (in_sum % 100) // 10 #десятки
print('10 грн X', tens, 'купюр')
units = in_sum % 10 #Одиниці

if units != 0:
    print ('Банкомат видає тільки круглу сумму!')

#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
print ()
print ('Task 5/5 \n')
amount = int(input('Введіть суму: '))
nominal = [50, 20, 10, 5]

notes_count = {}

for denomination in nominal:
    count = min(amount // denomination, 10)
    if count > 0:
        notes_count[denomination] = count
        amount -= count * denomination

if amount == 0:
    print('Купюри для видачі: ', end=' ')
    for denomination, count in notes_count.items():
        print(f'{count}x{denomination} грн')

else:
    print('Неможливо видати задану суму')
