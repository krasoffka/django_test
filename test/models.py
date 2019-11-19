from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=16)
    friends = models.ManyToManyField('self', symmetrical=False, blank=True)

    # def get_friends(self):
    #     return "\n".join([p.name for p in self.friends.all()])
    class Meta:
        ordering = ['id']
