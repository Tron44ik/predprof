file=open("songs.csv", encoding="UTF-8")

songs=[]
for i in file:
    songs.append(i.split(';'))
while True:
    flag=False
    zapros=input("Введите имя артиста: ")
    if zapros=="0":
        break
    else:
        for i in range(len(songs)):
            if songs[i][1]==zapros:
                print(f"У {zapros} найдена песня: {songs[i][2]}")
                flag=True
                break
        if not(flag):
                print("К сожалению, ничего не удалось найти")

