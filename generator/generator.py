def delstr(string, index):
    s = list(string) # конвертируем в список
    del s[index] # удаляем элемент с индексом index
    return "".join(s) # соединяем в строку и возвращаем результат в место вызова

def insertstr(string, index, stuff):
    s = list(string) # конвертируем в список
    s.insert(index, stuff) # добавляет элемент с индексом index
    return "".join(s) # соединяем в строку и возвращаем результат в место вызова

def writecorrectMD(newmd): # оформление в маркдаун
    for i in range (len(newmd)):
        result.write(newmd[i])
        result.write('\n')
        result.write('\n')

def writetopic(topic):# название темы задач
    topic = "# " + topic
    result.write(topic)
    result.write('\n')
    result.write('\n')

def writecode(code):
    flag = 0
    a = 0
    result.write('```python')
    result.write('\n')
    while flag == 0: #код записывается начинаяя с функции
        for i in range(len(code)):
            for j in range(len(code[i])-2):
                if code[i][j] == "d" and code[i][j+1] == "e" and code[i][j+2] == "f":
                    flag = 1
                    a = i
                    break
        if flag == 1:
            break
    for i in range(a, len(code)):  # запись кода с решением задачи
        result.write(code[i])
        result.write('\n')
    result.write('```')

def placeforlink(newmd):# не дописал
    n = len(newmd)
    a = 0
    for i in range(2, n):
        if newmd[i+1][0] == "#" and newmd[i+1][1] == "#":
            a = i


newmd = [] #сюда закину итоговые строки без пустых
titlelinks = [] # здесь лежат ссылки на каждую из задач
in_file = open(r'C:\Users\79046\Desktop\source_leetcode_data.txt','r', encoding='utf-8') # файл с решением задачи
result = open(r'C:\Users\79046\Desktop\result.txt','a', encoding='utf-8') # MD файл
writetopic("inervals") # название темы задач
sourse_lines = in_file.readlines()
sourse_lines[0] = sourse_lines[0][0:-1]
sourse_lines[1] = sourse_lines[1][0:-1]


#начало сбора ссылки
flag = 0
sch = 0
while flag == 0: # удаление номера задачи
    if sourse_lines[0][0] != " ":
        sourse_lines[0] = delstr(sourse_lines[0], 0)
    else:
        sourse_lines[0] = delstr(sourse_lines[0], 0)
        flag = 1
#print(sourse_lines[0])
dopstr = sourse_lines[0]
dopstr2 = "## " + sourse_lines[0]
dopstr = dopstr.lower() # понижаем регистр
l = dopstr.split() # заменяем прбелы на тире
dopstr = '-'.join(l)
sourse_lines[0] = "+ [" + sourse_lines[0] + "](#" + dopstr + ")"
titlelinks.append(sourse_lines[0])
#конец сбора ссылки

dopstr2 = "## " + sourse_lines[0]
newmd.append(sourse_lines[0])
newmd.append(dopstr2)
newmd.append(sourse_lines[1])

writecorrectMD(newmd)
writecode(sourse_lines