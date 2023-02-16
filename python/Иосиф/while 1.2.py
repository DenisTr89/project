hp_monstr = 100
hp_people = 50
def mostr_attack():
    global hp_people
    hp_people -= 15


def people_attack():
    global hp_monstr
    hp_monstr -= 15


def people_def():
    global hp_people
    hp_people += 10
cnt = 0
while hp_monstr >= 0 and hp_people >= 0:
    if cnt % 2 == 0:
        mostr_attack()
    cnt += 1
    while True:
        command = input("Введите команду attack или def: ")
        if command == "attack":
                people_attack()
                break
        elif command == "def":
                people_def()
                break
        else:
                print("Введена неверная команда")

    if hp_monstr <= 0:
        print("Ура победа")
        break
    if hp_people <= 0:
        print("Человек проиграл. Игра начнется сначала")
        hp_people = 50
        hp_monstr = 100
    print(f"Текущий уровень жизни человека {hp_people}, монстра {hp_monstr}")

        
            

