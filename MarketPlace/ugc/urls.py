from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
]

# router = routers.DefaultRouter()
# router.register('api/task', TaskViewSet, 'task')
# urlpatterns = router.urls