from rest_framework import status
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class TodolarAPIView(APIView):
    def get(self, request):
        todolar = Todo.objects.all()
        serializer = TodoSerializer(todolar, many=True)
        return Response(serializer.data)

    def post(self, request):
        todolar = request.data
        ser = TodoSerializer(data=todolar)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        ser = TodoSerializer(todo, request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def patch(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        ser = TodoSerializer(todo, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        try:
            get_object_or_404(Todo, id=pk).delete()
            data = {"xabar":"Muvaffaqiyatli o'chirildi!"}
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {"xabar":"Bu id'da todo yo'q!"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)


