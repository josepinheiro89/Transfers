from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import PaymentSchedule
from .serializers import PaymentScheduleSerializer

import json

#Criar agendamentos
@api_view(['POST'])
def create_schedule(request):
    serializer = PaymentScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Listar todos
@api_view(['GET'])
def list_schedules(request):
    if request.method == 'GET':
        schedules = PaymentSchedule.objects.all()
        serializer = PaymentScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)



#Pesquisar pelo ID
@api_view(['GET'])
def get_schedule(request, id):
    try:
        schedule = PaymentSchedule.objects.get(id=id)
    except PaymentSchedule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PaymentScheduleSerializer(schedule)
    return Response(serializer.data)



#Deletar agendamento pelo ID
@api_view(['DELETE'])
def delete_schedule(request, id):
    try:
        schedule = PaymentSchedule.objects.get(id=id)
    except PaymentSchedule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    schedule.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
