# Django
from django.contrib import admin
from django.urls import path

# mis utilities
from clonestagram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hellow-world/', local_views.hellow_world),
    path('sorted/', local_views.sorted_numeros),
    path('hi/<str:name>/<int:age>/', local_views.hi),

    # posts HTML 
    path('posts', posts_views.list_posts),
]
