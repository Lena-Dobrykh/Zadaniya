from itertools import product

def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count+= s2.count(ngram)
        
    return count/max(len(s1), len(s2))>0.6

class Person:
    
    def __init__(self,name=None,rost=None):
        self.name =name
        self.rost = rost
        
    def __eq__(self, obj):
        return (obj.name==None or self.name==None or compare(obj.name, self.name)) \
        and (obj.rost==None or self.rost==None or abs(obj.rost - self.rost)<3)
        
    def __repr__(self):
        return f"Person('{self.name}',{self.rost})"
        
to_search= [
    Person('наташа',120),

]
people=[       
Person('Лена',169),
Person('Наташа',120),
Person('Нташа',121),
Person('Олег',185),
Person('Игорь',179),
Person('Наташа',125),
Person('Леша',192),
Person('Наташа',118),
Person('Иван',171),
]
for p1,p2 in product(people, to_search):
    print(p1,p2, p1==p2)
