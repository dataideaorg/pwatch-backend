from rest_framework import serializers
from .models import Bill, BillReading, MP, DebtData


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


class MPListSerializer(serializers.ModelSerializer):
    """Simplified serializer for MP listing"""

    class Meta:
        model = MP
        fields = [
            'id',
            'name',
            'first_name',
            'middle_name',
            'last_name',
            'party',
            'phone_no',
            'constituency',
            'district',
            'photo',
            'email',
        ]


class MPDetailSerializer(serializers.ModelSerializer):
    """Full serializer for MP detail view"""

    class Meta:
        model = MP
        fields = [
            'id',
            'name',
            'first_name',
            'middle_name',
            'last_name',
            'party',
            'constituency',
            'district',
            'phone_no',
            'email',
            'photo',
            'bio',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class DebtDataSerializer(serializers.ModelSerializer):
    """Serializer for Debt Data"""

    class Meta:
        model = DebtData
        fields = [
            'id',
            'year',
            'national_debt',
            'gdp',
            'interest',
            'total_expenditure',
            'debt_per_citizen',
            'gdp_per_capita',
            'per_capita_income',
            'population',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']