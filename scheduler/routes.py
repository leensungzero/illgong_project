from django.urls import(
    include,
    path,
)

from member.routes import user_router


urlpatterns = [
    path('user/', include(user_router.urls)),
]