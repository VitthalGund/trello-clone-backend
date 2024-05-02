# serializers.py

from rest_framework import serializers
from .models import Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ["id", "title", "order", "created_at", "updated_at"]

    def validate_title(self, value):
        # Add validation rules for title field
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        if len(value) > 100:
            raise serializers.ValidationError(
                "Title must be less than or equal to 100 characters"
            )
        return value

    def validate_order(self, value):
        # Add validation rules for order field
        if value < 0:
            raise serializers.ValidationError("Order cannot be negative")
        # Add additional validation rules as needed
        return value
