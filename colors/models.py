from django.db import models


class Generation(models.Model):
    secret_key = models.CharField(max_length=100, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    before_url = models.URLField(blank=False, null=True)
    after_url = models.URLField(blank=False, null=True)
    status = models.CharField(max_length=20, default="created")

    def __str__(self):
        return f"Generation {self.id} | {self.status}"
