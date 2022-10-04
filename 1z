from pprint import pprint
class Person:
    def __init__(self,surname,name,age, rost):
        self.surname,self.name,self.age,self.rost = surname, name, age,rost
        self.key = (name, rost)
    def __repr__(self):
        return "Person('%s','%s','%s','%s')" % (self.surname,self.name,self.age,self.rost)
        
lena = Person("Добрых","Лена",21,169)
natasha = Person("Кудрявцева","Наташа",20,155)
oleg = Person("Лопатин","Олег",25,185)
igor = Person("Соколов","Игорь",33,179)
lesha = Person("Баталов","Леша",27,192)
nata = Person("Попова","Наташа",23,159)
ivan = Person("Биянов","Иван",21,171)
people = {
    lena.key: lena,
    natasha.key: natasha,
    oleg.key: oleg,
    igor.key: igor,
    lesha.key: lesha,
    nata.key: nata,
    ivan.key: ivan,
}
pprint(people[lena.key])
