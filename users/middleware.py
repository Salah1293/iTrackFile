from django.utils import timezone
from datetime import timedelta
from django.shortcuts import redirect

class SessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_expiry_time = request.session.get('session_expiry')
        if session_expiry_time:
            if timezone.now() > session_expiry_time:
                request.session.flush()  
                return redirect('login')  

        response = self.get_response(request)
        return response

    def process_request(self, request):
        request.session['session_expiry'] = timezone.now() + timedelta(hours=2)