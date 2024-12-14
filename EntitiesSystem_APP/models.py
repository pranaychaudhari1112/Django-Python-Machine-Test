from django.db import models



class Client(models.Model):
    client_name = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    def __str__(self):
        return self.client_name

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.JSONField()  # Storing users as a JSON array
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name


