from django.db import models


class Objective(models.Model):
    """
    Model for CEPA Objectives
    """
    title = models.CharField(max_length=200, help_text="Objective title or number")
    description = models.TextField(help_text="Detailed description of the objective")
    order = models.IntegerField(default=0, help_text="Display order")
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon name or identifier (optional)"
    )
    is_active = models.BooleanField(default=True, help_text="Whether this objective is active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Objective'
        verbose_name_plural = 'Objectives'

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    """
    Model for Team Members
    """
    name = models.CharField(max_length=200, help_text="Full name of the team member")
    title = models.CharField(max_length=200, help_text="Job title or position")
    bio = models.TextField(blank=True, help_text="Short biography")
    photo = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Team member photo")
    email = models.EmailField(blank=True, help_text="Email address")
    phone = models.CharField(max_length=20, blank=True, help_text="Phone number")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    facebook_url = models.URLField(blank=True, help_text="Facebook profile URL")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Whether this team member is active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return f"{self.name} - {self.title}"
