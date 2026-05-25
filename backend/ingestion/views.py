from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UploadRecord
from .serializers import UploadSerializer


class GetData(APIView):

    def get(self,request):

        data=UploadRecord.objects.all()

        serializer=UploadSerializer(
            data,
            many=True
        )

        return Response(
            serializer.data
        )



class Approve(APIView):


    def post(self,request,id):

        record=UploadRecord.objects.get(
            id=id
        )

        record.approved=True

        record.save()

        return Response({

            "message":"Approved"

        })