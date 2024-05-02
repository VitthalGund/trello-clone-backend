from rest_framework import serializers
from .models import Card
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


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "title", "description", "column", "order"]
        read_only_fields = ["id"]

    def validate_title(self, value):
        # Validate that the title contains only alphabets
        if not value.isalpha():
            raise serializers.ValidationError("Title should contain only alphabets.")
        return value

    def validate_description(self, value):
        # Validate minimum length of description
        min_length = 25
        if len(value) < min_length:
            raise serializers.ValidationError(
                f"Description should be at least {min_length} characters long."
            )
        return value
