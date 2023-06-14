from django.db import models


class table(models.Model):
    # category_name = models.CharField(max_length=45, null=True),
    numero_table=models.CharField(max_length=45)
    capacite_table=models.CharField(max_length=45)
    description_table=models.TextField()
    status=models.BooleanField(default=True)
    
    
    class Meta:
        db_table = 'tab'
