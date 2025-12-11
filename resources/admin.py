from django.contrib import admin
from .models import Explainers, Report, PartnerPublication, Statement


@admin.register(Explainers)
class ExplainersAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

    fieldsets = (
        ('Explainer Information', {
            'fields': ('name', 'description', 'file')
        }),
    )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

    fieldsets = (
        ('Report Information', {
            'fields': ('name', 'description', 'file')
        }),
    )


@admin.register(PartnerPublication)
class PartnerPublicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

    fieldsets = (
        ('Partner Publication Information', {
            'fields': ('name', 'description', 'file')
        }),
    )


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

    fieldsets = (
        ('Statement Information', {
            'fields': ('name', 'description', 'file')
        }),
    )