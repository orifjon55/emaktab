from django.urls import path,include

urlpatterns = [
    path('student/',include('main.student.urls')), #oquvchi
    path('principal/',include('main.principal.urls')), #zamdirektor
    path('teachers/',include('main.teachers.urls')), #oqituvchi 
    path('work/', include('main.work.urls')), #uyvazifa
    path('family/',include('main.family.urls')), #ota-ona
    path('payment/',include('main.payment.urls')) #tolov
]