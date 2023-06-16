from django.urls import path
from django.contrib import admin
from restorantbar import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('tab',views.tab),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
    path('reserver',views.reserver),
    path('select',views.select),
    path('selection',views.selectionernumtab),
    path('updatereservation',views.updatereservation),
    path('editreservation',views.editreservation),
]