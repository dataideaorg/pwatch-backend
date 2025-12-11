from django.contrib import admin
from .models import XSpace, Podcast, Gallery


@admin.register(XSpace)
class XSpaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'host', 'scheduled_date', 'status', 'created_at']
    list_filter = ['status', 'scheduled_date']
    search_fields = ['title', 'description', 'host', 'topics', 'speakers']
    date_hierarchy = 'scheduled_date'
    ordering = ['-scheduled_date', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'host', 'status')
        }),
        ('Schedule', {
            'fields': ('scheduled_date', 'duration')
        }),
        ('Links', {
            'fields': ('x_space_url', 'recording_url')
        }),
        ('Media', {
            'fields': ('thumbnail',)
        }),
        ('Details', {
            'fields': ('topics', 'speakers')
        }),
    )


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'host', 'guest', 'published_date', 'episode_number']
    list_filter = ['category', 'published_date']
    search_fields = ['title', 'description', 'host', 'guest', 'tags']
    date_hierarchy = 'published_date'
    ordering = ['-published_date', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'host', 'guest')
        }),
        ('Episode Details', {
            'fields': ('episode_number', 'published_date', 'duration')
        }),
        ('YouTube', {
            'fields': ('youtube_url', 'thumbnail')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'event_date', 'photographer', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'event_date']
    search_fields = ['title', 'description', 'photographer', 'tags']
    date_hierarchy = 'event_date'
    ordering = ['-featured', '-event_date', '-created_at']
    list_editable = ['featured']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Details', {
            'fields': ('category', 'event_date', 'photographer')
        }),
        ('Organization', {
            'fields': ('tags', 'featured')
        }),
    )

