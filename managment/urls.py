from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('course.urls')),
    path('/', include('student.urls')),
    path('/', include('teacher.urls')),
    path('/', include('classroom.urls')),
]
