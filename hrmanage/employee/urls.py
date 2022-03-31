from django.urls import path
from . import views

urlpatterns = [
    path('add',views.add,name='add'),
    path('insertEmp',views.insertEmp,name='insertEmp'),
    path('get',views.get,name='get'),
    path('editEmp/<int:eid>',views.editEmp,name="editEmp"),
    path('updateEmp/<int:eid>',views.updateEmp,name="updateEmp"),
    path('deleteEmp/<int:eid>',views.deleteEmp,name="deleteEmp"),
    
]