from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('launcher/admin/', admin.site.urls),
    path('launcher/accounts/', include('accounts.urls')),
    path('launcher/accounts/', include('django.contrib.auth.urls')),
    path('launcher/api/', include('api.urls'))
]
