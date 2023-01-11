from django.db import models
from common.models import CommonModel

class Post(CommonModel):
    title = models.CharField(max_length=150)
    content = models.TextField()
    # writer = models.ForeignKey(to='users.user', null=True, blank=True,
    #                            on_delete=models.SET_NULL)