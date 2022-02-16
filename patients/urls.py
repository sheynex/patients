
from django.contrib import admin
from django.urls import path, include
from Demo import views
urlpatterns = [
    # path to access the admin page
    path('admin/', admin.site.urls),

    # Path to render the Homepage
    path('', views.frontend, name="frontend"),

    # Path Login/Logout
    path('login/', include('django.contrib.auth.urls')),

    #================
    # BACKEND SECTION
    #================

    path('backend', views.backend, name="backend")
]
