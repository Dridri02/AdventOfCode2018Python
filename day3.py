
def part1(path):
    file=open(path);
    tableauRempli=[]
    for i in range(2000):
        tableauRempli.append([0] * 2000)
    resultat=0;
    for ligne in file:
        departX='';
        departY='';
        longueurX='';
        longeurY='';
        partieLue=0;
        chaine=ligne.strip()
        for i in range(len(chaine)):
            if chaine[i]=='@':
                partieLue=1;
            if chaine[i]==',':
                partieLue=2; 
            if chaine[i]==':':
                partieLue=3;  
            if chaine[i]=='x':
                partieLue=4;    
            if partieLue==1 and chaine[i]!='@':
                departX+=chaine[i];
            if partieLue==2 and chaine[i]!=',':
                departY+=chaine[i];
            if partieLue==3 and chaine[i]!=':':
                longueurX+=chaine[i];
            if partieLue==4 and chaine[i]!='x':
                longeurY+=chaine[i];
        departX=int(departX);
        departY=int(departY);
        longueurX=int(longueurX);
        longeurY=int(longeurY);
        for i in range(longueurX):
            for j in range(longeurY): 
                if(tableauRempli[departX+i][departY+j]==1):
                    resultat+=1;
                tableauRempli[departX+i][departY+j]+=1
                
            
            
        
               
    return(resultat);



def part2(path):
    file=open(path);
    tableauRempli=[]
    for i in range(2000):
        tableauRempli.append([0] * 2000)
    listParcelles=[];
    listParcellesChevauchees=[];
    resultat=0;
    for ligne in file:
        departX='';
        departY='';
        longueurX='';
        longeurY='';
        idParcelle='';
        partieLue=0;
        chaine=ligne.strip()
        for i in range(len(chaine)):
            if chaine[i]=='#':
                partieLue=1;
            if chaine[i]=='@':
                partieLue=2;
            if chaine[i]==',':
                partieLue=3; 
            if chaine[i]==':':
                partieLue=4;  
            if chaine[i]=='x':
                partieLue=5;    
            if partieLue==1 and chaine[i]!='#':
                idParcelle+=chaine[i];
            if partieLue==2 and chaine[i]!='@':
                departX+=chaine[i];
            if partieLue==3 and chaine[i]!=',':
                departY+=chaine[i];
            if partieLue==4 and chaine[i]!=':':
                longueurX+=chaine[i];
            if partieLue==5 and chaine[i]!='x':
                longeurY+=chaine[i];
        departX=int(departX);
        departY=int(departY);
        longueurX=int(longueurX);
        longeurY=int(longeurY);
        idParcelle=int(idParcelle);
        listParcelles.append(idParcelle);
        for i in range(longueurX):
            for j in range(longeurY): 
                if(tableauRempli[departX+i][departY+j]!=0):
                    if not tableauRempli[departX+i][departY+j] in listParcellesChevauchees:
                        listParcellesChevauchees.append(tableauRempli[departX+i][departY+j])
                    if not idParcelle in listParcellesChevauchees:
                        listParcellesChevauchees.append(idParcelle)
                tableauRempli[departX+i][departY+j]=idParcelle  
    return(sum(listParcelles)-sum(listParcellesChevauchees));


print(part1("03.txt"));
print(part2("03.txt"));