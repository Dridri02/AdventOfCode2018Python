#!/usr/bin/env python
# coding: utf-8

# In[ ]:






def somme(path):
    file=open(path);
    resultat=0;
    for ligne in file:
        resultat+=int(ligne.strip());
    return(resultat);
    

print(somme("01.txt"));

def firstDoubled(path):
    file=open(path);
    dejaVu=[0];
    resultat=0;
    NumberOfLine = 0;
    onADouble=False;
    for line in file:
        NumberOfLine += 1 ;
    file.seek(0);
    indice=0;
    lignes=[]; 
    while onADouble==False and indice<NumberOfLine:
        indice+=1;
        ligne=file.readline();
        resultat= resultat + int(ligne.strip());
        lignes=lignes+[int(ligne.strip())];
        if resultat in dejaVu:
            onADouble=True;
            return resultat;
        else:
            dejaVu= dejaVu + [resultat];
    indice=0;
    while onADouble==False:
        ligne=lignes[indice];
        indice+=1;
        resultat= resultat + ligne;
        if resultat in dejaVu:
            onADouble=True;
            return resultat;
        else:
            dejaVu= dejaVu + [resultat];
            if indice==NumberOfLine:
                indice=0;
  


print(firstDoubled("01.txt"));




        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




