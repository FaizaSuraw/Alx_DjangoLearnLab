from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("API is live!")
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home), 
    path("accounts/", include("accounts.urls")),
    path("api/", include("posts.urls")),
]
