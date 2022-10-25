#Резюме
print("                      Резюме            ")
fio = "Ф.И.О : Конусбанв Жасурбек"
date_of_birth = "Дата рождения : 30.07.2001"
obrazovanie = "Образование : Satbayev University"
print(fio)
print(date_of_birth)
obrazovanie = {
    'ВУЗ': 'Satbayev University',
    'Специальность ': 'Computer Science',
    'GPA': '3.4',
    'Год окончания ': '2023'
}
for x, y in obrazovanie.items():
    print(x + ' : ' + y)

skills = ['Языки программирования C , Python', 'OS Linux', 'HTML,CSS']
for x in skills:
    print("\tОсновные навыки : " + x)

info = []
info.append("Номер телефона : ")
info.append("Эл.почта : ")
print(info[0] + '87477052500')
print(info[1] + 'jasurbek200176@gmail.com')
print("Цель : " + "Получение вакантной должности программиста-стажера")

#1.Бағдарламалау секцияларына қатысатын әртүрлі топтағы студенттерді таныстыруды сұрайтын бағдарламаны жазыңыз.
# Тізімді сыныптардың өсу реті бойынша сұрыптау қажет. Фамилиялар мен сыныптардың тізімін басып шығарыңыз.
d = {}
n = int(input('Студенттердің санын енгізіңіз :  '))
# Пустой лист құрамыз
# Студент жайлы ақпаратты енгіземіз
list = []
for i in range(0, n):
	# split
	x,y = input("Студенттің аты - жөні және бағасы : ").split()
	#  x - аты , y - бағасы
	list.append((y,x))
  #баға бойынша сортировка жасаймыз
list = sorted(list, reverse = False)

print('Өсу реті бойынша өңделген тізім : ')

for i in list:
	print(i[1], i[0])

    #4. Алдыңғы жағдайдағыдай пайдаланушыдан бүтін сандарды сұрайтын және оларды тізім ретінде сақтайтын
# бағдарламаны жазыңыз. Нөл мәндерді енгізудің аяқталуының көрсеткіші ретінде де қызмет етуі керек. Бұл жолы
# енгізілген мәндерді кему ретімен көрсету қажет.

list = []
while True:
    n = input('Бүтін санды енгізіңіз: ')
    list += [n]
    if n == 0:
        break
print(sorted(list, reverse=True))

#Тізім қайтаратын функция жазып шығу. Алдын ала студенттердің пәндері және бағалары бар тізім құрастыр.
# Және сол тізім бойынша студенттің атын еңгізген кезде, сол студенттің бағаларын шығарып бертін болсын

def get_student_grades():
    student_grades = {
      'Jasurbek': 89,
      'Shyngys' : 75,
      'Abylai': 95,
      'Samat' : 93,
    }
    while True:
      student_name = input()  #Студенттің есімін енгіземіз
      for student in student_grades:  # Словарьдың ішінен іздейтін цикл
            if student == student_name: #Егер студенттің есімі словарьда болса
                    print(student_grades[student])  #Бағасын шығару
                    break #Программаны тоқтату
            else: #Егер енгізілген есім болмаса
                print('Бұл есім табылмады.')

table = get_student_grades()
for student, grade in table.items():
    print(student, grade)