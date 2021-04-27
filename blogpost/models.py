from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    blog = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
