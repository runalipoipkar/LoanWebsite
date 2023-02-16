from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vendor,Installment,Disbursement
from .serializers import VendorSerializer,InstallmentSerializer,DisbursementSerializer
import logging
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from fpdf import FPDF


logger=logging.getLogger('main')


class VendorViewSet(viewsets.ViewSet):
    serializer_class=VendorSerializer
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(" vendor Has been Added")
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        try:
            posts=Vendor.objects.all()
            serializer=self.serializer_class(posts,many=True)
            logger.info(" Vendor Has been seen ")
            return Response({
                'data':serializer.data,
                'message':'data fetched successfully'
                },status=status.HTTP_200_OK)
        except Exception as e:
            logger.error("Error occure during vendor retrieve")
            print(e)
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request,pk=None):
        try:
            obj=get_object_or_404(Vendor,pk=pk)
            serializer=self.serializer_class(obj)
            logger.info(" Perticular Vendor Has been fetched ")
            return Response({
                'data':serializer.data,
                'message':'data has been fetched'
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            logger.error(" error occure during fetching Perticular Vendor ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def update(self,request,pk=None):
        try:
            obj=get_object_or_404(Vendor,pk=pk)
            serializer=self.serializer_class(data=request.data,instance=obj)
            if serializer.is_valid():
                serializer.save()
                logger.info(" Vendor's data has been Updated ")            
                return Response({
                    'data': serializer.data,
                    'message':'data has been updated successfully'

                },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            logger.error(" error during vendor update ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self,request,pk=None):
        try:
            obj=get_object_or_404(Vendor,pk=pk)
            if not Vendor.exists():
                return Response({
                    'data':{},
                    "message":'invalid ID'
                },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            logger.error(" Error during Deleting Vendor's data ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
        else:
            obj.delete()
            logger.info(" Vendor Has been deleted ")
            return Response({
                'data':{},
                'message':'your blog Deleted successfully '
            },status=status.HTTP_204_NO_CONTENT)


class InstallmentViewSet(viewsets.ViewSet):
    serializer_class=InstallmentSerializer
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(" Installment Has been created ")
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        try:
            posts=Installment.objects.all()
            serializer=self.serializer_class(posts,many=True)
            logger.info(" Installments list Has been seen ")
            return Response({
                'data':serializer.data,
                'message':'data fetched successfully'
                },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            logger.info(" Installment fetching error ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request,pk=None):
        try:
            obj=get_object_or_404(Installment,pk=pk)
            serializer=self.serializer_class(obj)
            logger.info(" fetching perticular user's installment ")
            return Response({
                'data':serializer.data,
                'message':'data has been fetched'
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            logger.error("fetching error during fetching perticular error ")
            return Response({
                'data':{},
                'message':"somthing went wrong 123"
            },status=status.HTTP_400_BAD_REQUEST)
    

    def update(self,request,pk=None):
        try:
            obj=get_object_or_404(Installment,pk=pk)
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
            obj=get_object_or_404(Installment,pk=pk)
            if not Installment.exists():
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


class DisbursementViewSet(viewsets.ViewSet):
    serializer_class=DisbursementSerializer
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        try:
            posts=Disbursement.objects.all()
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
            obj=get_object_or_404(Disbursement,pk=pk)
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
            obj=get_object_or_404(Disbursement,pk=pk)
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
            obj=get_object_or_404(Disbursement,pk=pk)
            if not Disbursement.exists():
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



def send_new_mail(request, pk):
    print(pk)
    obj = Disbursement.objects.get(id=pk)
    mail_from = settings.EMAIL_HOST_USER
    sub = 'LOAN DISBURSEMENT'
    msg = f'hello, with your loan ID = {obj.loan}, \nThis is to inform you that, \n  Your loan has been disbursed, \n please check the attachment for more details'
    with open ('disbursement_loan.txt', 'w') as fh:
        fh.write(f'\n CHECK THE DETAILED INFORMATION ABOUT YOUR LOAN DISBURSEMENT\n')
        fh.write('*'*80)
        fh.write(f'\nLOAN ID = {obj.loan}')
        fh.write(f'\nPAYMENT MODE = {obj.payment_mode}')
        fh.write(f'\nNET DISBURSED AMOUNT = Rs. {obj.net_disbursed_amount}')
        fh.write(f'\nAMOUNT DISBURSED TO ACCOUNT NO = {obj.disbursed_to_account_no}\n')
        fh.write('*'*80)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    with open ('disbursement_loan.txt','r') as fh:
        for i in fh:
            pdf.cell(200, 10, txt = i, ln = 1, align = 'l')
    pdf.output("myfile_in_pdf.pdf")
    pdf.output(f'E:\CJC\project TASK\loan project\day 5\loan_for_company_interior\confirmation_file\disbursement\{obj.loan}.pdf')
    email_message = EmailMessage(sub, msg, mail_from, ['rahulaglawe744@gmail.com',] )
    email_message.attach_file(f'E:\CJC\project TASK\loan project\day 5\loan_for_company_interior\confirmation_file\disbursement\{obj.loan}.pdf')
    email_message.send()
    print('*****Email sent******')
    return HttpResponse('<h1>Email has been sent</h1>')