from django.shortcuts import redirect

def api_router_view(request):
    return redirect('api-root')