"""
Security Middleware
Custom security headers and rate limiting
"""

from django.http import HttpResponse
from django.core.cache import cache
from django.conf import settings
import time

class SecurityHeadersMiddleware:
    """
    Add security headers to all responses
    Protects against common web vulnerabilities
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Content Security Policy - allows Bootstrap Icons and fonts
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; "
            "font-src 'self' https://cdn.jsdelivr.net https://fonts.gstatic.com data:; "
            "img-src 'self' data: https:; "
            "connect-src 'self';"
        )
        
        # Prevent clickjacking
        response['X-Frame-Options'] = 'DENY'
        
        # Prevent MIME type sniffing
        response['X-Content-Type-Options'] = 'nosniff'
        
        # Enable XSS protection in browsers
        response['X-XSS-Protection'] = '1; mode=block'
        
        # Force HTTPS in production
        if not settings.DEBUG:
            response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        
        # Control referrer information
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        # Prevent browsers from using certain features
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
        
        return response


class RateLimitMiddleware:
    """
    Rate limiting for authentication endpoints
    Prevents brute force attacks on login
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 5  # attempts
        self.time_window = 300  # 5 minutes in seconds
    
    def __call__(self, request):
        # Only apply to auth endpoints
        if request.path in ['/login/', '/signup/']:
            if request.method == 'POST':
                # Use IP address as identifier
                identifier = self.get_client_ip(request)
                cache_key = f'rate_limit_{identifier}_{request.path}'
                
                # Get current attempt count
                attempts = cache.get(cache_key, 0)
                
                if attempts >= self.rate_limit:
                    return HttpResponse(
                        'Too many attempts. Please try again in 5 minutes.',
                        status=429
                    )
                
                # Increment attempts
                cache.set(cache_key, attempts + 1, self.time_window)
        
        return self.get_response(request)
    
    def get_client_ip(self, request):
        """Get real client IP even behind proxy"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
