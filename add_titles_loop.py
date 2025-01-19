print("Введите заголовки заметок. Для завершения ввода оставьте строку пустой или введите 'стоп'.")

# Переменные
titles_list=[]
a_inputing=''
number=0

# Цыкл запроса и обработки кода
while a_inputing != 'стоп' :
    a_inputing = input("Введите заголовк заметки :")
    if a_inputing != 'стоп' :
        if a_inputing != None :
            if a_inputing.strip() != '':
                titles_list.append(a_inputing.lstrip())

print("Список заголовок заметок :")

# Цыкл вывода
while number != len(titles_list) :
    print("         Заголовок №",number + 1,":",titles_list[number])
    number = number + 1