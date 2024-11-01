from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AGVData
from .serializers import AGVDataSerializer


@api_view(["GET", "POST"])
def agv_list(request):
    if request.method == "GET":
        agvs = AGVData.objects.all()
        serializer = AGVDataSerializer(agvs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        agv_id = request.data.get('agv_id')
        if AGVData.objects.filter(agv_id=agv_id).exists():
            return Response(
                {"error": "AGV with this ID already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AGVDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
def agv_detail(request, agv_id):
    try:
        agv = AGVData.objects.get(agv_id=agv_id)
    except AGVData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AGVDataSerializer(agv)
        return Response(serializer.data)

    elif request.method == "DELETE":
        agv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)