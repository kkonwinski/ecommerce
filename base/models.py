from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Base model for other models to inherit from.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
        ordering = ['-updated_at']
