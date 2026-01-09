from rest_framework import serializers
from main.utils import get_full_media_url
from .models import Objective, TeamMember, WhoWeAre, OurStory, WhatSetsUsApart, Partner


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


class WhoWeAreSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = WhoWeAre
        fields = [
            'id',
            'title',
            'content',
            'image',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_image(self, obj):
        if obj.image:
            return get_full_media_url(obj.image.url)
        return None


class OurStorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = OurStory
        fields = [
            'id',
            'title',
            'content',
            'image',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_image(self, obj):
        if obj.image:
            return get_full_media_url(obj.image.url)
        return None


class WhatSetsUsApartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatSetsUsApart
        fields = [
            'id',
            'title',
            'description',
            'icon',
            'order',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class PartnerSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id',
            'name',
            'description',
            'logo',
            'website_url',
            'order',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_logo(self, obj):
        if obj.logo:
            return get_full_media_url(obj.logo.url)
        return None
