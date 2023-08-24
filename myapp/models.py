from django.db import models
from accounts.models import Client,User
class Problems_section(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff_involved = models.ManyToManyField(
        User,related_name='staff_involved_problems',limit_choices_to={'staff_is': True}
    )

    def __str__(self):
        return self.title
