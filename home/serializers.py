from rest_framework import serializers
from .models import HeroImage, Headline


class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = [
            'id',
            'title',
            'image',
            'order',
            'is_active',
            'alt_text',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = [
            'id',
            'text',
            'is_bold',
            'order',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

