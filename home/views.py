from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.parsers import MultiPartParser

def home(request):
    return render(request ,'home.html')

def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data=request.data
            folder_name="media"

            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'files uploaded successfully',
                    'data': {'folder': 'media' }
                })

            return Response({
                'status' : 400,
                'message': 'something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)