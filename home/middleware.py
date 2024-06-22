from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class Redirect404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            # Redirect all non-existing URLs under /settings/ to /settings
            if request.path.startswith('/settings/'):
                return redirect('settings')
            if request.path.startswith('/profile/'):
                return redirect('profile') 
            if request.path.startswith('/contests/'):
                return redirect('contests') 
            if request.path.startswith('/ratings/'):
                return redirect('ratings')
            if request.path.startswith("/contest/"):
                return redirect("contests")
            if request.path.startswith(""):
                return redirect('home')
        return response
