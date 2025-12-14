"""
Utility functions for the main app
"""
from django.conf import settings
from decouple import config


def get_full_media_url(relative_url):
    """
    Convert a relative media URL to a full backend URL.
    
    Args:
        relative_url: Relative URL from media folder (e.g., '/media/news/image.jpg' or 'news/image.jpg')
    
    Returns:
        Full backend URL (e.g., 'https://backend.example.com/media/news/image.jpg')
    """
    if not relative_url:
        return None
    
    # Remove leading /media/ if present
    if relative_url.startswith('/media/'):
        relative_url = relative_url[7:]  # Remove '/media/'
    elif relative_url.startswith('media/'):
        relative_url = relative_url[6:]  # Remove 'media/'
    
    # Get full media URL from settings
    full_media_url = getattr(settings, 'FULL_MEDIA_URL', None)
    if full_media_url:
        # Remove trailing slash if present
        full_media_url = full_media_url.rstrip('/')
        return f"{full_media_url}/{relative_url}"
    
    # Fallback: construct from MEDIA_URL
    if settings.DEBUG:
        return f"http://localhost:8000{settings.MEDIA_URL}{relative_url}"
    else:
        # In production, try to get from environment or use default
        backend_domain = config('BACKEND_DOMAIN', default='https://pwatch-backend-production.up.railway.app')
        return f"{backend_domain}{settings.MEDIA_URL}{relative_url}"

