from rest_framework import serializers
from .models import Users 
from django.shortcuts import get_object_or_404
from .serializers import Userserializer
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
import logging


logger=logging.getLogger('main')
'''
class UserAPI(ListCreateAPIView):
    logger.info("User Has been Generated")
    serializer_class=Userserializer
    queryset=Users.objects.all()


class UserDetailsAPI(RetrieveUpdateDestroyAPIView):
    logger.info("User Has been Generated")
    serializer_class=Userserializer
    queryset=Users.objects.all()
    
'''

class UserView(viewsets.ViewSet):
    serializer_class=Userserializer
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(" User Has been created ")
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        try:
            people=Users.objects.all()
            serializer=self.serializer_class(people,many=True)
            logger.info(" User Has been seen ")
            return Response({
                'data':serializer.data,
                'message':'data fetched successfully'
                },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            logger.error(" Error occure during fetching list of user ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request,pk=None):
        try:
            obj=get_object_or_404(Users,pk=pk)
            serializer=self.serializer_class(obj)
            logger.info(" user Has been retrive ")
            return Response({
                'data':serializer.data,
                'message':'data fetched successfully'
                },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            logger.error(" error occure during fetching user ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)


    def update(self,request,pk=None):
        try:
            obj=get_object_or_404(Users,pk=pk)
            serializer=self.serializer_class(data=request.data,instance=obj,partial=True)
            if not serializer.is_valid():
                return Response({
                    'date':serializer.errors,
                    'message':'something went wrong123'
                },status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data':serializer.data,
                'message':'your blog updated successfully '
            },status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'somthing went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        try:
            obj=get_object_or_404(Users,pk=pk)
            if not Users.exists():
                return Response({
                    'data':{},
                    "message":'invalid ID'
                },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
        else:
            obj.delete()
            return Response({
                'data':{},
                'message':'your blog Deleted successfully '
            },status=status.HTTP_204_NO_CONTENT)






        
            
        

        
            
