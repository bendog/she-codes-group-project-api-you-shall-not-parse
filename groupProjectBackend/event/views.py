# from multiprocessing.synchronize import Event
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from rest_framework import status, permissions, generics, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Event, Role, EventModule, Module, EventModuleRole
from .serializers import EventSerializer, ModuleSerializer, RoleSerializer, EventModuleSerializer, EventModuleRoleSerializer
from .permissions import IsAuthorOrReadOnly, IsSuperuserOrReadOnly




class EventList(generics.ListCreateAPIView):
    #get all events

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

class EventDetailApi(generics.RetrieveUpdateDestroyAPIView):
    #get event by id
    # permission_classes = [permissions.IsSuperuserOrReadOnly]
    queryset = Event.objects.filter()
    serializer_class = EventSerializer


class ModuleList(generics.ListCreateAPIView):
    #get all modules

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class RoleList(generics.ListCreateAPIView):
    #get all roles

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class EventModuleList(generics.ListCreateAPIView):
    #get all eventmodules

    queryset = EventModule.objects.all()
    serializer_class = EventModuleSerializer

class EventModuleRoleList(generics.ListCreateAPIView):
    #get all eventmodulesroles

    queryset = EventModuleRole.objects.all()
    serializer_class = EventModuleRoleSerializer


class EventModuleRoleDetailApi(generics.RetrieveUpdateDestroyAPIView):
    #get event by id
    queryset = EventModuleRole.objects.filter()
    serializer_class = EventModuleRoleSerializer



#### WORKING
class FilteredEventModuleRole(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventModuleRole.objects.filter()
    serializer_class = EventModuleRoleSerializer



    def get(self, request, event_module_pk):
        event_module_roles = EventModuleRole.objects.filter(event_module = event_module_pk, mentor__isnull=True)
        serializer = EventModuleRoleSerializer(event_module_roles, many=True)
        return Response(serializer.data)




#########   WORKING
class FilteredEventModule(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventModule.objects.all()
    serializer_class = EventModuleSerializer


    def get(self, request, event_pk):
        event_modules = EventModule.objects.filter(event = event_pk)
        serializer = EventModuleSerializer(event_modules, many=True)
        return Response(serializer.data)




#this is a view test to get from event directly to eventmodulerole
# class FilteredTest(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EventModuleRole.objects.filter()
#     serializer_class = EventModuleRoleSerializer


#     def get(self, request, event_pk):
#         event_module_roles = EventModuleRole.objects.filter(event = event_pk, mentor__isnull=True)
#         serializer = EventModuleRoleSerializer(event_module_roles, many=True)
#         return Response(serializer.data)




def event_module_populate(request, pk):
    """
    Retrieve, update or delete a code em.
    """
    try:
        em = EventModule.objects.get(pk=pk)
    except EventModule.DoesNotExist:
        return HttpResponse(status=404)
    em.populate_roles()
    if request.method == 'GET':
        serializer = EventModuleSerializer(em)
        return JsonResponse(serializer.data)
        
