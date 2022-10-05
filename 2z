from itertools import product
class Person:
    
    def __init__(self,name=None,rost=None):
        self.name=name
        self.rost=rost
        
    def __eq__(self, obj):
        return (obj.name ==None or self.name==None or obj.name==self.name)\
            and (obj.rost==None or self.rost==None or obj.rost==self.rost)
    
    def __gt__(self, obj):
        return (obj.name ==None or self.name==None or obj.name==self.name)\
            and (obj.rost==None or self.rost==None or obj.rost>self.rost)
        
    def __repr__(self):
        return f"Person('{self.name}',{self.rost})"    
        
to_search= [
    Person('Наташа',120),
]

people=[       
Person('Лена',169),
Person('Наташа',155),
Person('Наташа',125),
Person('Олег',185),
Person('Игорь',179),
Person('Леша',192),
Person('Наташа',119),
Person('Иван',171),
]

for p1,p2 in product(people, to_search):
    print(p1,p2,p1<p2)
