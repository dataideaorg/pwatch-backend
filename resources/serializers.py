from rest_framework import serializers
from .models import Explainers, Report, PartnerPublication, Statement


class ExplainersSerializer(serializers.ModelSerializer):
    """Serializer for Explainers"""

    class Meta:
        model = Explainers
        fields = [
            'id',
            'name',
            'description',
            'file',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class ReportSerializer(serializers.ModelSerializer):
    """Serializer for Reports"""

    class Meta:
        model = Report
        fields = [
            'id',
            'name',
            'description',
            'file',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class PartnerPublicationSerializer(serializers.ModelSerializer):
    """Serializer for Partner Publications"""

    class Meta:
        model = PartnerPublication
        fields = [
            'id',
            'name',
            'description',
            'file',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class StatementSerializer(serializers.ModelSerializer):
    """Serializer for Statements"""

    class Meta:
        model = Statement
        fields = [
            'id',
            'name',
            'description',
            'file',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']