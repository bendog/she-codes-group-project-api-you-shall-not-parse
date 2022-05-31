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
    #get all eventmodules

    queryset = EventModuleRole.objects.all()
    serializer_class = EventModuleRoleSerializer


class EventModuleRoleDetailApi(generics.RetrieveUpdateDestroyAPIView):
    #get event by id
    # permission_classes = [permissions.IsSuperuserOrReadOnly]
    queryset = EventModuleRole.objects.filter()
    serializer_class = EventModuleRoleSerializer



class FilteredEventModuleRole(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventModuleRole.objects.all()
    serializer_class = EventModuleRole
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly
    # ]

    def get_object(self, event):
        try:
            event_module_role = EventModuleRole.objects.select_related("event").get(event_id=event)
            self.check_object_permissions(self.request, event_module_role)
            return event
        except Event.DoesNotExist:
            raise Http404








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
        
