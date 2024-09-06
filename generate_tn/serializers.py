from rest_framework import serializers
from .models import TrackingNumber
import random
import string


class TrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumber
        fields = [
            'tracking_no', 'origin_country_id', 'destination_country_id', 'weight',
            'customer_id', 'customer_name', 'customer_slug', 'created_at']

class GenerateTrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumber
        fields = [
            'origin_country_id', 'destination_country_id', 'weight', 'customer_id',
            'customer_name', 'customer_slug', 'created_at']

    def validate_origin_country_id(self, value):
        if len(value) != 2:
            raise serializers.ValidationError("Origin country ID must be a 2-character ISO 3166-1 alpha-2 code.")
        return value

    def validate_destination_country_id(self, value):
        if len(value) != 2:
            raise serializers.ValidationError("Destination country ID must be a 2-character ISO 3166-1 alpha-2 code.")
        return value

    def validate_weight(self, value):
        if value <= 0:
            raise serializers.ValidationError("Weight must be greater than 0.")
        return value

    def validate_customer_slug(self, value):
        if not value.islower() or ' ' in value:
            raise serializers.ValidationError("Customer slug must be in slug-case (kebab-case).")
        return value

    def create(self, validated_data):
        for _ in range(10):
            tracking_no = self.generate_unique_tracking_number()
            if not TrackingNumber.objects.filter(tracking_no=tracking_no).exists():
                validated_data['tracking_no'] = tracking_no
                return super().create(validated_data)

        raise serializers.ValidationError("Unable to generate a unique tracking number.")

    def generate_unique_tracking_number(self):
        return self.validated_data['origin_country_id'] + \
            self.validated_data['destination_country_id'] + \
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
