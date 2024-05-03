from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Column, Card
from .serializers import ColumnSerializer, CardSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

logger = logging.getLogger(__name__)


@api_view(["GET"])
def welcome(request):
    return Response(
        {"message": "Welcome to Trello backend API"}, status=status.HTTP_200_OK
    )


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


@api_view(["PUT"])
def reorder_columns(request):
    try:
        column_ids = request.data.get("column_ids", [])
        updated_columns = []

        for index, column_id in enumerate(column_ids, start=1):
            column = Column.objects.get(pk=column_id)
            old_order = column.order
            column.order = index
            column.save()

            # Shift other columns with the same order
            other_columns = Column.objects.filter(order=old_order).exclude(pk=column_id)
            for other_column in other_columns:
                other_column.order += 1
                other_column.save()

            updated_columns.append(column)

        # Serialize the updated columns and return them
        serializer = ColumnSerializer(updated_columns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Card Views:


@api_view(["POST"])
def create_card(request):
    try:
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "PUT", "DELETE"])
def card_retrieve_update_delete(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)

        if request.method == "GET":
            serializer = CardSerializer(card)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            serializer = CardSerializer(instance=card, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            card.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Card.DoesNotExist:
        return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def move_card(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)
        new_column_id = request.data.get("new_column_id")

        # Check if the new column exists
        try:
            new_column = Column.objects.get(pk=new_column_id)
        except Column.DoesNotExist:
            return Response(
                {"error": "New column does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Move the card to the new column
        card.column = new_column
        card.save()

        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Card.DoesNotExist:
        return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def reorder_cards(request, column_id):
    try:
        column = Column.objects.get(pk=column_id)
        card_orders = request.data.get("card_orders", {})

        total_cards = (
            column.cards.count()
        )  # Get the total number of cards in the column

        for card_id, new_order in card_orders.items():
            try:
                new_order = int(new_order)
                if 1 <= new_order <= total_cards:  # Validate the new order
                    card = Card.objects.get(pk=card_id, column=column)
                    card.order = new_order
                    card.save()
                else:
                    return Response(
                        {"error": f"Invalid order number for card {card_id}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except ValueError:
                return Response(
                    {"error": f"Invalid order format for card {card_id}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Card.DoesNotExist:
                pass  # Ignore if card not found in the column

        return Response(status=status.HTTP_200_OK)
    except Column.DoesNotExist:
        return Response({"error": "Column not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
