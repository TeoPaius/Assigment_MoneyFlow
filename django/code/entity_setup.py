from persons.models import Person
from persons.models import Friendship
from random import randrange

def setup():
    print("removing entities")
    Person.objects.all().delete()
    Friendship.objects.all().delete()
    print("adding entities")
    for i in range(0,10):
        new_name = "name" + str(i)
        Person.objects.create(name=new_name)
    print(Person.objects.all())

    for i in range(0,10):
        id1 = randrange(0,10)
        id2 = randrange(0,10)
        while id1 == id2:
            id1 = randrange(0, 10)
            id2 = randrange(0, 10)
        pa = Person.objects.all()[id1]
        pb = Person.objects.all()[id2]
        Friendship.objects.create(personA = pa, personB = pb)
    print(Friendship.objects.all)