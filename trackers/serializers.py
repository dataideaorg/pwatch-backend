from rest_framework import serializers
from .models import Bill, BillReading


class BillReadingSerializer(serializers.ModelSerializer):
    stage_display = serializers.CharField(source='get_stage_display', read_only=True)

    class Meta:
        model = BillReading
        fields = [
            'id',
            'stage',
            'stage_display',
            'date',
            'details',
            'document',
            'committee_report',
            'analysis',
            'mp_photo',
            'created_at',
            'updated_at',
        ]


class BillSerializer(serializers.ModelSerializer):
    bill_type_display = serializers.CharField(source='get_bill_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    readings = BillReadingSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = [
            'id',
            'title',
            'bill_type',
            'bill_type_display',
            'year_introduced',
            'mover',
            'assigned_to',
            'status',
            'status_display',
            'description',
            'video_url',
            'likes',
            'comments',
            'shares',
            'readings',
            'created_at',
            'updated_at',
        ]


class BillListSerializer(serializers.ModelSerializer):
    """Simplified serializer for bill listing"""
    bill_type_display = serializers.CharField(source='get_bill_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Bill
        fields = [
            'id',
            'title',
            'bill_type',
            'bill_type_display',
            'year_introduced',
            'mover',
            'status',
            'status_display',
            'created_at',
        ]