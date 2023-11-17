from apiapp import views
from django.urls import path

urlpatterns = [
    path('studentapi/', views.StudentListView.as_view(), name="student")
]
