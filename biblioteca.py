def newBook(name,author,gender,year,cost):
    dic[name]=[author,gender,year,cost]
def searchBook(name,author):
    if name is None:
        books=[x[0] for x in dic.items() if x[1][0]==author]
        print(','.join(books))
    else:
        print(dic[name])
def updateQuant(quant,book):
    dic[book][3] = quant
def updatePrice(price,book):
    dic[book[4]] = price
def deleteObs(nom):
    aux=input(f"Do you really want to delete {dic[nom]}? (please write yes if you agree): ").lower()
    if aux == "yes":
        del dic[nom]
def reportGenerator():
    #totalValue=sum(map(lambda x: x[3]*x[4], dic.values()))
    totalValue= sum([x[3]*x[4] for x in dic.values()])
    #totalValue=sum(map(lambda x: x[0]*x[1], inventory.values()))

    return(totalValue)

dic={"book1":["author1","gender1",1967,2,15.00],"book2":["author2","gender2",1967,3,20],"book3": ("author1", "gender2", 1975,1,10.00)}
print(reportGenerator())