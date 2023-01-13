from django.urls import path

from studentapp import views

urlpatterns=[
    path("",views.login_fun, name="login"),
    path("reg",views.register_fun, name="register"),
    path("reddata",views.regdata_fun),
    path("home", views.home_fun , name='home'),
    path("add", views.add_fun , name='add'),
    path("logout", views.logout_fun , name='logout'),
    path("display",views.disp_fun, name="display" ),#it will display student data in display.html
    path("update/<int:id>",views.update_fun,name='update'),#it will update student data based on id
    path("delete/<int:id>",views.delete_fun,name='delete')#itwill delete student data based on id

]