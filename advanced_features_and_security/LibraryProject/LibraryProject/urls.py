from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Library Project</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view), 
    path('bookshelf/', include('bookshelf.urls')),  
]
