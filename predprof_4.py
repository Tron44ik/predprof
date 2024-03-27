file=open("songs.csv", encoding="UTF-8")
rus='йцукеёнгшщзхъфывапролджэячсмитьбюЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
russian_artist=''
foreign_artists=''
songs=[]
for i in file:
    songs.append(i.split(';'))
for i in songs[1:]:
    for j in i[1]:
        if j in rus and i[1] not in russian_artist:
            russian_artist+= i[1]+"\n"
        if j not in (rus) and i[1] not in foreign_artists:
            foreign_artists+=i[1]+"\n"
file.close

file=open("russian_artists.txt","w",encoding="UTF-8")
file.write(russian_artist)
file.close
file=open("foreign_artists.txt","w",encoding="UTF-8")
file.write(foreign_artists)
file.close