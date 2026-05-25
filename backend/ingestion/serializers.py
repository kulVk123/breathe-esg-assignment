from rest_framework import serializers

from .models import UploadRecord


class UploadSerializer(
serializers.ModelSerializer
):


    class Meta:

        model=UploadRecord

        fields='__all__'