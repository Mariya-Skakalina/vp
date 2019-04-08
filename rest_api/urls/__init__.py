from .urls_comment import urlpatterns as comm
from .urls_user import urlpatterns as user
from rest_framework import routers
routers.SimpleRouter()
urlpatterns = comm
urlpatterns += user