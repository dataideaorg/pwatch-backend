from django.db import models
from django.conf import settings
import os
import uuid


class ChatConversation(models.Model):
    """Model to store chat conversation sessions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_id = models.CharField(max_length=255, db_index=True, help_text="Session identifier for the conversation")
    ip_address = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of the user")
    user_agent = models.TextField(blank=True, null=True, help_text="User agent string")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Chat Conversation'
        verbose_name_plural = 'Chat Conversations'

    def __str__(self):
        return f"Conversation {self.id} - {self.session_id}"

    @property
    def message_count(self):
        """Get the number of messages in this conversation"""
        return self.messages.count()


class ChatMessage(models.Model):
    """Model to store individual chat messages"""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]

    conversation = models.ForeignKey(
        ChatConversation,
        on_delete=models.CASCADE,
        related_name='messages',
        help_text="The conversation this message belongs to"
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, help_text="Role of the message sender")
    content = models.TextField(help_text="Message content")
    document_name = models.CharField(max_length=255, blank=True, null=True, help_text="Document used for this response")
    document_url = models.URLField(blank=True, null=True, help_text="URL to the document used")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'

    def __str__(self):
        return f"{self.role}: {self.content[:50]}..."


class Document(models.Model):
    """Model to track documents available for the chatbot"""
    name = models.CharField(max_length=255, db_index=True, help_text="Display name for the document")
    file = models.FileField(upload_to='chatbot/documents/', help_text="Upload PDF document")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the document")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name

    @property
    def full_path(self):
        """Get the full file path"""
        if self.file:
            return self.file.path
        return None

    @property
    def file_url(self):
        """Get the URL to access the file"""
        if self.file:
            from main.utils import get_full_media_url
            return get_full_media_url(self.file.url)
        return None

    @property
    def file_type(self):
        """Get file type from extension"""
        if self.file:
            return os.path.splitext(self.file.name)[1].lower().replace('.', '')
        return 'pdf'
