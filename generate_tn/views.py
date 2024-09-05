from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GenerateTrackingNumberSerializer, TrackingNumberSerializer
from django.utils.dateparse import parse_datetime


class TrackingNumberGenerator(APIView):
    def get(self, request, *args, **kwargs):
        try:
            origin_country_id = request.query_params.get('origin_country_id')
            destination_country_id = request.query_params.get('destination_country_id')
            weight = request.query_params.get('weight')
            created_at = request.query_params.get('created_at')
            customer_id = request.query_params.get('customer_id')
            customer_name = request.query_params.get('customer_name')
            customer_slug = request.query_params.get('customer_slug')

            
            if created_at:
                created_at = parse_datetime(created_at)
            
            data = {
                'origin_country_id': origin_country_id,
                'destination_country_id': destination_country_id,
                'weight': weight,
                'customer_id': customer_id,
                'customer_name': customer_name,
                'customer_slug': customer_slug,
                'created_at': created_at
            }

            serializer = GenerateTrackingNumberSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response_serializer = TrackingNumberSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
