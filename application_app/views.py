from rest_framework import viewsets,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ApplicationSerializer
from .models import Application

'''
class ApplicationAPI(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


'''
class ApplicationViewSet(viewsets.ViewSet):
    serializer_class=ApplicationSerializer
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        try:
            posts=Application.objects.all()
            serializer=self.serializer_class(posts,many=True)
            return Response({
                'data':serializer.data,
                'message':'data fetched successfully'
                },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request,pk=None):
        try:
            obj=get_object_or_404(Application,pk=pk)
            serializer=self.serializer_class(obj)
            return Response({
                'data':serializer.data,
                'message':'data has been fetched'
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def update(self,request,pk=None):
        try:
            obj=get_object_or_404(Application,pk=pk)
            serializer=self.serializer_class(data=request.data,instance=obj)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data': serializer.data,
                    'message':'data has been updated successfully'

                },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self,request,pk=None):
        try:
            obj=get_object_or_404(Application,pk=pk)
            if not Application.exists():
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
