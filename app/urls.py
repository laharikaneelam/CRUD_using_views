from django.urls import path
from app.views import templateViewClass,listViewClass,detailViewClass,createViewClass,updateViewClass,deleteViewClass
urlpatterns=[
    path('',templateViewClass.as_view(),name="template"),
    path('list/',listViewClass.as_view(),name="list"),
    path('list/<int:pk>/',detailViewClass.as_view(),name='detail'),
    path('list/create/',createViewClass.as_view(),name="create"),
    path('list/<int:pk>/update',updateViewClass.as_view(),name="update"),
    path('list/<int:pk>/delete',deleteViewClass.as_view(),name="delete"),

]
