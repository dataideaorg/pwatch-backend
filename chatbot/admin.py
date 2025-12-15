from django.contrib import admin
from .models import Document, ChatConversation, ChatMessage


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'file_type', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at', 'file_type']
    
    fieldsets = (
        ('Document Information', {
            'fields': ('name', 'file', 'description')
        }),
        ('Metadata', {
            'fields': ('file_type', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class ChatMessageInline(admin.TabularInline):
    """Inline admin for chat messages"""
    model = ChatMessage
    extra = 0
    readonly_fields = ['created_at']
    fields = ['role', 'content', 'document_name', 'created_at']
    can_delete = False


@admin.register(ChatConversation)
class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_id', 'message_count', 'ip_address', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['session_id', 'ip_address']
    readonly_fields = ['id', 'created_at', 'updated_at', 'message_count']
    inlines = [ChatMessageInline]
    
    fieldsets = (
        ('Conversation Information', {
            'fields': ('id', 'session_id', 'message_count')
        }),
        ('Metadata', {
            'fields': ('ip_address', 'user_agent', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'conversation', 'role', 'content_preview', 'document_name', 'created_at']
    list_filter = ['role', 'created_at', 'conversation']
    search_fields = ['content', 'document_name', 'conversation__session_id']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Message Information', {
            'fields': ('conversation', 'role', 'content')
        }),
        ('Document Reference', {
            'fields': ('document_name', 'document_url'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def content_preview(self, obj):
        """Show a preview of the message content"""
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content Preview'
