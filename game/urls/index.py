from django.urls import path, include
from game.views.index import index


urlpatterns = [
    path("", index, name="index"), # 如果是空的，那就回访问import进来的index
    path("menu/", include("game.urls.menu.index")), # 同理，去game.urls.menu.index
    path("settings/",include("game.urls.settings.index")),
    path("playground/", include("game.urls.playground.index")),
]
