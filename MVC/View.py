from Model import Person

def showAllView(list):
    print(len(list))

    for item in list:
        print(item.name())

def startView():
    print('MVC - the simplest example')
    print('Do yu want to see everyone in my db? [y/n]')

def endView():
    print('GoodBye!')