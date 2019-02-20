from Model import Person
import View

def showAll():
    people_in_db = Person.getAll()
    return

View.showAll(people_in_db)

def start():
    View.startView()
    input_value = input()

    if input_value == 'y':
        return showAll()
    else:
        return View.endView()

if __name__ == "__main__":
    start()