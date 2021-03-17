from django.urls import path
from .views import HomePageView,RevistaPageView,MangaPageView,Descrip_libPageView,AutoresPageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
     path('mangas',RevistaPageView.as_view(),name='mangas'),
      path('revistas',MangaPageView.as_view(),name='revistas'),
      path('descrip',Descrip_libPageView.as_view(),name='descrip'),
      path('Autor',AutoresPageView.as_view(),name='Autores'),
]
