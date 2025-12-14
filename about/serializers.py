from rest_framework import serializers
from main.utils import get_full_media_url
from .models import Objective, TeamMember


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = [
            'id',
            'title',
            'description',
            'order',
            'icon',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class TeamMemberSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = [
            'id',
            'name',
            'title',
            'bio',
            'photo',
            'email',
            'phone',
            'linkedin_url',
            'twitter_url',
            'facebook_url',
            'order',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_photo(self, obj):
        if obj.photo:
            return get_full_media_url(obj.photo.url)
        return None


