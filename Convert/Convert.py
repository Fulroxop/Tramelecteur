import math
import os

fin=""
f = open("Trame.txt","r")
Fichier = list(f)
trame = " ".join(Fichier)
entete=trame[0:41]
entetip=trame[42:103]
partcp=trame[104:165]

for i in Fichier:
    resu=""
    for y in i.split(" "):
        y=y.upper()
        resu+=chr(int(str(y), 16))
    fin+=resu

c=0
longeur=""
ident=""
flags=""
cheksum=""
ipsource=""
ipdest=""
for i in entetip.split(" "):
    if c==0:
        ver=str(int(i[0],16))
        ihl=str(int(i[1],16))
    elif c==1:
        service=str(int(i,16))
    elif c>=2 and c<=3:
        longeur+=str(int(i,16))
    elif c>=4 and c<=5:
        ident+=str(int(i,16))
    elif c>=6 and c<=7:
        flags+=str(bin(int(i, 16))[2:])
    elif c==8:
        TTL=str(int(i,16))
    elif c==9:
        proto=str(int(i,16))
    elif c >=10 and c <=11:
        cheksum+= str(int(i,16))
    elif c >=12 and c <=15:
        ipsource+= str(int(i,16))+"."
    else:
        ipdest+=str(int(i,16))+"."
    c+=1

if proto == "1":
    tp="ICMP"
elif proto == "2":
    tp="IGMP"
elif proto == "6":
    tp="TCP"
elif proto == "17":
    tp = "UDP"
else:
    tp="Inconnu"

if ver == "4":
    ipto="IP V4"
elif ver == "6":
    ipto="IP V6"
elif ver == "5":
    ipto="ST Datagram Mode"
elif ver == "15" or ver == "0":
    ipto = "Réservé"
else:
    ipto="Non assigné"
ports=""
portd=""
seq=""
Nseq=""
offset=""
flagtcp=""
chektp=""
point=""
c=0
for i in partcp.split(" "):
    if c>=0 and c<=1:
        ports+=str(i)
    elif c>=2 and c<=3:
        portd+=str(i)
    elif c>=4 and c<=7:
        seq=str(int(i,16))
    elif c>=8 and c<=11:
        Nseq+=str(int(i,16))
    elif c>=12 and c<=13:
        offset+=str(bin(int(i, 16))[2:])
    elif c>=14 and c<=15:
        flagtcp=str(bin(int(i, 16))[2:])
    elif c>=16 and c<=17:
        chektp=str(int(i,16))
    elif c >=18 and c <=19:
        point+= str(int(i,16))

    c+=1


print("Partie ethernet:"'\n')
print("l'entete de base: "+'\n')
print("Adresse mac destinataire: "+entete[0:17])
print("Adresse mac source: "+entete[18:35]+'\n'+'\n')
print("la trame ip contient ver: "+ver+" version du protocole: "+ipto+". Et le ihl: "+ihl )
print("service: "+service)
print("longeur: "+longeur)
print("flags: "+flags)
print("le TTL: "+TTL)
print("protocole utiliser: "+proto,"--",tp)
print("cheksum: "+cheksum)
print("Adresse ip source: "+ipsource[:-1])
print("Adresse ip destination: "+ipdest[:-1]
+'\n'+'\n')

print("Partie TCP:"+'\n')

print("Port source: "+str(int(ports,16)))
print("Port destination: "+str(int(portd,16)))
print("Seq: "+seq)
print("Numero de seq: "+Nseq)
print("Offset et autre: "+offset)
print("Flag: "+flagtcp)
print("Cheksum: "+chektp)
print("Point: "+point+'\n'+'\n')

print("La trame complete: "+'\n'+fin)

os.system("pause")





