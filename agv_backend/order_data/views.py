from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        orders = Order.objects.all().order_by('order_id')  # Sort by order_id
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # Check if request.data is a list (for bulk creation)
        if isinstance(request.data, list):
            # Set many=True to handle multiple objects
            serializer = OrderSerializer(data=request.data, many=True)
        else:
            serializer = OrderSerializer(data=request.data)  # Single object

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def order_detail(request, id):
    try:
        order = Order.objects.get(
            order_id=id
        )  # ! because order_id is the primary key, use order_id=id instead of id=id
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
