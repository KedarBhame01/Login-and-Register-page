from django.db import models


class MyappRegistermodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'myapp_registermodel'