from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class Redirect404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            # Redirect all non-existing URLs under /settings/ to /settings
            if request.path.startswith('/settings/'):
                return redirect('settings')  # Name of the URL pattern for the settings page
            if request.path.startswith('/profile/'):
                return redirect('profile')  # Name of the URL pattern for the settings page
            if request.path.startswith('/contests/'):
                return redirect('contests')  # Name of the URL pattern for the settings page
            if request.path.startswith('/ratings/'):
                return redirect('ratings')
            if request.path.startswith(""):
                return redirect('home')  # Name of the URL pattern for the settings page
        return response
    