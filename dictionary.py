print("HELLO WORLD")
user = {
    'username': 'name',
    "password": 1234,
    "robux": 100500,
    "age": 49,
    "gender": "male"

    }
print("Имя пользователя:", user["username"])
print("У вас", user["robux"], "робуксов")

# user.clear()
# print(user)

print(user.get("gender")) 
print(user.items())
print(user.keys())
# print(user.pop("robux"))
print(user.values())
user["robux"] = 123456789


print(user)
user.setdefault("new key", " Moyo novoe znachenie")
print(user)

player ={
    "name": "Pupa",
    "hp" : 120,
    "dmg": 20
}

enemy = {
    "name": "владыка",
    "hp" : 100,
    "dmg" : 10
}
def Fight(player=dict, enemy=dict):
    print(f'Игрок{player["name"]} атакует {enemy["name"]} и наносит {player["dmg"]}')
    enemy["hp"] -= player["dmg"]
    print(f'У {enemy["name"]} осталось {enemy["hp"]} здоровья')
Fight(player,enemy)