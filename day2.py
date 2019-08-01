
def part1(path):
    file=open(path);
    nombreDe2=0;
    nombreDe3=0;
    for ligne in file:
        aUnDoublon=False;
        aUnTriplon=False;
        dictionnaire={};
        chaine=ligne.strip();
        for i in range(len(chaine)):
            if chaine[i] in dictionnaire.keys():
                dictionnaire[chaine[i]]=1+dictionnaire[chaine[i]];
            else:
                dictionnaire[chaine[i]]=1;
        for value in dictionnaire.values():
            if value==2 and aUnDoublon==False:
                nombreDe2+=1;
                aUnDoublon=True;
            if value==3 and aUnTriplon==False:
                nombreDe3+=1;
                aUnTriplon=True;
    return(nombreDe2*nombreDe3);

print(part1("02.txt"));

