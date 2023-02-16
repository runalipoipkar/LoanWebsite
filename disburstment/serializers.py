from rest_framework import serializers
from .models import Vendor,Installment,Disbursement


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'


class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Installment
        fields='__all__'


class DisbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disbursement
        fields='__all__'