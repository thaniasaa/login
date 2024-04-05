from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('', LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('account/', include('account.urls')),
    path('', include('account.urls')),
]