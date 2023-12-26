from django.urls import path

from project_app import views

urlpatterns = [
    # path('',views.front,name='test1'),
    path('',views.homepage,name='test2'),
    path('page2',views.dashboard,name='page2'),
    path('test4',views.Login12,name='test4'),
    path('log',views.customer_reg,name='log'),
    path('work',views.work_manager_reg,name='work'),
    path('log_view',views.login_view,name='log_view'),
    path('adm',views.admin,name='adm'),
    path('custom',views.custom,name='custom'),
    path('manager',views.manager,name='manager')

]