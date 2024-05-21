from django.db import models
from account.models import User


class Client(User):

    class Meta:
        ordering = ['username']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

# class User(AbstractUser):
#     date_joined = models.DateTimeField(auto_now_add=True)

#     @property
#     def created_at(self):
#         return self.date_joined


# class Hotel(models.)
