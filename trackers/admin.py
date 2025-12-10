from django.contrib import admin
from .models import Bill, BillReading


class BillReadingInline(admin.TabularInline):
    model = BillReading
    extra = 1
    fields = ['stage', 'date', 'details', 'document', 'committee_report', 'analysis', 'mp_photo']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['title', 'bill_type', 'status', 'year_introduced', 'mover', 'created_at']
    list_filter = ['bill_type', 'status', 'year_introduced']
    search_fields = ['title', 'mover', 'assigned_to']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    inlines = [BillReadingInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'bill_type', 'year_introduced', 'mover', 'assigned_to', 'status')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Video & Engagement', {
            'fields': ('video_url', 'likes', 'comments', 'shares')
        }),
    )


@admin.register(BillReading)
class BillReadingAdmin(admin.ModelAdmin):
    list_display = ['bill', 'stage', 'date', 'created_at']
    list_filter = ['stage', 'date']
    search_fields = ['bill__title', 'details']
    date_hierarchy = 'date'
    ordering = ['-date']

    fieldsets = (
        ('Reading Information', {
            'fields': ('bill', 'stage', 'date', 'details')
        }),
        ('Documents', {
            'fields': ('document', 'committee_report', 'analysis', 'mp_photo')
        }),
    )