from rest_framework import serializers
from .models import XSpace, Podcast, Gallery


class XSpaceSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = XSpace
        fields = [
            'id',
            'title',
            'description',
            'host',
            'scheduled_date',
            'duration',
            'x_space_url',
            'recording_url',
            'thumbnail',
            'status',
            'status_display',
            'topics',
            'speakers',
            'created_at',
            'updated_at',
        ]


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = [
            'id',
            'title',
            'description',
            'host',
            'guest',
            'youtube_url',
            'thumbnail',
            'duration',
            'published_date',
            'episode_number',
            'category',
            'tags',
            'created_at',
            'updated_at',
        ]


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [
            'id',
            'title',
            'description',
            'image',
            'category',
            'event_date',
            'photographer',
            'tags',
            'featured',
            'created_at',
            'updated_at',
        ]

