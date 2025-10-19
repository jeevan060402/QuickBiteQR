from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def healthz(request):
    return JsonResponse({'status': 'ok'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/restaurant/', include('restaurant.urls')),
    path('healthz/', healthz),
]
