from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Column
from .serializers import ColumnSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

logger = logging.getLogger(__name__)


@api_view(["GET", "POST"])
def column_list_create(request):
    try:
        if request.method == "GET":
            columns = Column.objects.all()

            # Pagination
            page_number = request.GET.get("page", 1)
            page_size = request.GET.get("page_size", 10)
            paginator = Paginator(columns, page_size)
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)

            # Sorting
            sort_by = request.GET.get("sort_by", "title")
            if sort_by in ["title", "order", "created_at", "updated_at"]:
                page = page.order_by(sort_by)

            # Filtering
            title_contains = request.GET.get("title_contains")
            if title_contains:
                page = page.filter(title__icontains=title_contains)

            serializer = ColumnSerializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serializer = ColumnSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return Response(
            {"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def column_detail(request, pk):
    try:
        try:
            column = Column.objects.get(pk=pk)
        except Column.DoesNotExist:
            return Response(
                {"error": "Column not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if request.method == "GET":
            serializer = ColumnSerializer(column)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            serializer = ColumnSerializer(column, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            column.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return Response(
            {"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
