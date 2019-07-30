from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from random import randrange

@api_view(['GET', 'POST', 'DELETE'])
def friendship_view(request):
    if Person.objects.all().count() == 0:
        print("removing entities")
        Person.objects.all().delete()
        Friendship.objects.all().delete()
        print("adding entities")
        for i in range(0, 10):
            new_name = "name" + str(i)
            Person.objects.create(name=new_name)
        print(Person.objects.all())

        for i in range(0, 10):
            id1 = randrange(0, 10)
            id2 = randrange(0, 10)
            while id1 == id2:
                id1 = randrange(0, 10)
                id2 = randrange(0, 10)
            pa = Person.objects.all()[id1]
            pb = Person.objects.all()[id2]
            Friendship.objects.create(personA=pa, personB=pb)
        print(Friendship.objects.all)

    if request.method == 'GET':
        persons = Person.objects.all()
        return Response(str(persons))

    elif request.method == 'POST':


        id1 = request.data['id1']
        id2 = request.data['id2']

        pa = Person.objects.get(id=id1)
        pb = Person.objects.get(id=id2)
        Friendship.objects.create(personA=pa, personB=pb)
        return Response("created")

    elif request.method == 'DELETE':
        id_removed = request.data['id']

        fs = Friendship.objects.get(id=id_removed)
        fs.delete()

        return Response("removed")