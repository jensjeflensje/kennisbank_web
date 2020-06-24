from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("app.urls")),
    path('auth/', include("user_auth.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('api/', include("api.urls")),
    path('admin/', admin.site.urls),
]
