file='stock.csv'
f = open(file,'r',encoding="utf8")
y=int(0)
numero=int(0)
criga=0
conta=int(0)
conta_elementi=int(0)
elementi_secondari=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
last_line=str
for x in f:
 conta_elementi=f.readline().count(';')+1
 break
f.close()
f = open(file,'r',encoding="utf8")
prima_linea=f.readline().strip('\n')
for a in range(conta_elementi):
 if a == 0:
  elemento_riferimento=prima_linea.split(';')[a]
 else:
   elementi_secondari[a]=prima_linea.split(';')[a]
f.close() 
f = open(file,'r',encoding="utf8")
for x in f:
 numero_linee=len(f.readlines())+1
f.close()
"""
 VECCHIO CODICE CHE CONTA GLI ELEMENTI E GLI ASSEGNA IL VALORE
while conta <conta_elementi :
 if conta==0:
  elemento_riferimento=f.readline().split(';')[conta]
 conta=conta+1
 break
f.close()
f = open('stock.csv','r',encoding="utf8")
AGGIUNGE ULTIMA RIGA A CASO
"""
f = open(file,'r',encoding="utf8")
for x in f:
 line = f.readline()
 numero=x.count(';')+1
 for y in range(numero):
  if line.count(';') != 0:
   if y == 0:
    print(elemento_riferimento.replace('"','') + ': ' + line.split(';')[y])
   else:
    if elementi_secondari[y] != "" :
     print('-',elementi_secondari[y].replace('"',''),':',line.split(';')[y].replace('"',''))
  else:
#CODICE SEGUENTE VA A LEGGERE ULTIMA RIGA DEL CSV SOLO SE LA LINEA NELLA PRIMA LETTURA DEL FILE RISULTA VUOTA
   with open(file,encoding="utf8") as f:
    for line in f:
        pass
    last_line = line
   for y in range(numero):
    if y == 0:
     print(elemento_riferimento.replace('"','') + ': ' + line.split(';')[y])
    else:
     if elementi_secondari[y] != "" :
      print('-',elementi_secondari[y].replace('"',''),':',line.split(';')[y].replace('"',''))
   break