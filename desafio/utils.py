import uuid
from django.db import models
from django.utils.translation import gettext as _


class CommonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at")
    )

    class Meta:
        abstract = True
        ordering = ("-created_at",)
