from django.db import models


class table(models.Model):
    # category_name = models.CharField(max_length=45, null=True),
    numero_table=models.CharField(max_length=45)
    capacite_table=models.CharField(max_length=45)
    description_table=models.TextField()
    status=models.BooleanField(default=True)
    
    
    class Meta:
        db_table = 'tab'
        
        
class reservation(models.Model):
    nom_client=models.CharField(max_length=45) 
    table_reserver=models.CharField(max_length=45)
    nombre_personne=models.CharField(max_length=45)   
    date_reservation=models.CharField(max_length=45)
    
    class Meta:
        db_table = 'reservation' 
        
# class selectiontab(models.Model):
#     numero_table=models.CharField(max_length=45)
#     class Meta:
#         db_table='tab'               
