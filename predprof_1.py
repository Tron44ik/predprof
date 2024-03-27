


file=open("songs.csv", encoding="UTF-8")

songs=[]
for i in file:
    songs.append(i.split(';'))
#print(songs)
for i in songs[1:]:
    data=[]
    for j in range(3,len(i),3):
        data.append(i[j].split("."))
    if int(data[0][2])<2002:
        print(i[2],"-",i[1],"-",i[0])
    elif (int(data[0][2])==2002 and int(data[0][1])==1 and int(data[0][0])==1):
        print(i[2], "-", i[1], "-", i[0])


