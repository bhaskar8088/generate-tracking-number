from django.db import models
import uuid

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TrackingNumber(BaseModel):
    tracking_no = models.CharField(max_length=16, unique=True)
    origin_country_id = models.CharField(max_length=2)
    destination_country_id = models.CharField(max_length=2)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=255)
    customer_slug = models.SlugField(max_length=255)
    
    class Meta:  
        indexes = [
            models.Index(fields=['tracking_no']),
        ]
    
    def __str__(self):
        return self.tracking_no

