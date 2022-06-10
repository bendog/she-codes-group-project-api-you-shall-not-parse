# from multiprocessing.synchronize import Event
# from django.shortcuts import render
# from django.http import Http404
from django.http import HttpResponse, JsonResponse
from rest_framework import status, permissions, generics, exceptions
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .models import Event, Role, EventModule, Module, EventModuleRole
from .serializers import EventSerializer, ModuleSerializer, RoleSerializer, EventModuleSerializer, EventModuleRoleSerializer
# from .permissions import IsAuthorOrReadOnly, IsSuperuserOrReadOnly


class EventList(generics.ListCreateAPIView):
    # get all events

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailApi(generics.RetrieveUpdateDestroyAPIView):
    # get event by id
    # permission_classes = [permissions.IsSuperuserOrReadOnly]
    queryset = Event.objects.filter()
    serializer_class = EventSerializer


class ModuleList(generics.ListCreateAPIView):
    # get all modules

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class RoleList(generics.ListCreateAPIView):
    # get all roles

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class EventModuleList(generics.ListCreateAPIView):
    # get all eventmodules

    queryset = EventModule.objects.all()
    serializer_class = EventModuleSerializer


class EventModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    # get all eventmodules
    queryset = EventModule.objects.all()
    serializer_class = EventModuleSerializer


class EventModuleDetailRoles(generics.ListCreateAPIView):
    serializer_class = EventModuleRoleSerializer

    def get_queryset(self):
        mentor_filter = self.request.query_params.get('mentored')
        qs = EventModule.objects.get(pk=self.kwargs['pk']).required_roles.all()
        if mentor_filter:
            qs = qs.filter(mentoring__isnull=mentor_filter == 'true')
        return qs


class EventModuleRoleList(generics.ListCreateAPIView):
    # get all eventmodulesroles

    queryset = EventModuleRole.objects.all()
    serializer_class = EventModuleRoleSerializer


class EventModuleRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    # get event by id
    queryset = EventModuleRole.objects.all()
    serializer_class = EventModuleRoleSerializer


class UserRoleList(generics.ListCreateAPIView):
    serializer_class = EventModuleRoleSerializer

    def get_queryset(self):
        return self.request.user.registered_roles.all()




#
# #########   WORKING
# class FilteredEventModule(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EventModule.objects.all()
#     serializer_class = EventModuleSerializer
#
#     def get(self, request, event_pk):
#         event_modules = EventModule.objects.filter(event=event_pk)
#         serializer = EventModuleSerializer(event_modules, many=True)
#         return Response(serializer.data)
#
#
# class FilteredEventModuleRoleUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EventModuleRole.objects.filter()
#     serializer_class = EventModuleRoleSerializer
#
#     def get(self, request, mentor_pk):
#         event_module_roles = EventModuleRole.objects.filter(mentor=mentor_pk)
#         serializer = EventModuleRoleSerializer(event_module_roles, many=True)
#         return Response(serializer.data)
#
#
# #### WORKING
# class FilteredEventModuleRole(APIView):
#     queryset = EventModuleRole.objects.all()
#     serializer_class = EventModuleRoleSerializer
#
#     def get(self, request, event_module_pk):
#         event_module_roles = EventModuleRole.objects.filter(event_module=event_module_pk, mentor__isnull=True)
#         serializer = EventModuleRoleSerializer(event_module_roles, many=True)
#         return Response(serializer.data)


# class EventModuleRoleDetail(generics.RetrieveUpdateDestroyAPIView):
#     """ This is a detail view laura, call it the right thing """
#     queryset = EventModuleRole.objects.all()
#     serializer_class = EventModuleRoleSerializer
#
#     def get_object(self, event_module_pk, role_pk):
#         try:
#             return EventModuleRole.objects.filter(event_module=event_module_pk).get(role=role_pk)
#         except EventModuleRole.DoesNotExist as e:
#             raise Http404 from e
#
#     # def put(self, request, event_module_pk, role_pk):
#     #     print(event_module_pk, role_pk)
#     #     event_module_roles = self.get_object(event_module_pk, role_pk)
#     #     data = request.data
#     #     serializer = EventModuleRoleSerializer(
#     #         instance=event_module_roles,
#     #         data=data,
#     #         partial=True
#     #     )
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(
#     #             serializer.data,
#     #             status=status.HTTP_201_CREATED
#     #         )
#     #     return Response(
#     #         serializer.errors,
#     #     )


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
