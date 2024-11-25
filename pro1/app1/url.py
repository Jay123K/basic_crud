from django.urls import path
from app1 import views
from .views import UpdateStudent,studentList,DeleteStudent
urlpatterns = [
   
    path('',views.StudentData,name=''),
    path('Login',views.Login_page,name='Login'),
    path('Logout',views.Logout_page,name='Logout'),
    path('Register',views.Register_page,name='Register'),
    path('Student_list',studentList.as_view(),name='Student_list'),
    path('Student_list/<pk>/update_stu',UpdateStudent.as_view(),name='update_stu'),
    path('Student_list/<pk>/delete_stu',DeleteStudent.as_view(),name='Delete'),
    
]
