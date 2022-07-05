from django.contrib import admin
from django.urls import path
from .views import TodolarAPIView, TodoAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolar/', TodolarAPIView.as_view(), name="todolar"),
    path('qoshiqchi/<int:pk>/', TodoAPIView.as_view(), name="todo"),
]
