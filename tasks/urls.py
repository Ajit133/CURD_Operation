from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('student_form/',views.student_form,name='student_form'),
    path('students/<int:pk>/',views.Student_Information,name='students'),
    path('student/<int:pk>/edit/',views.Student_Edit,name='s_edit'),
    path('delete/<int:pk>/delete/',views.Student_Delete,name='delete')
    # path('student/<int:pk>/',views.Student_Edit,name='s_edit')
    
]
# <int:pk>/edit/
