from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarietie(models.Model):
    CHAI_TYPES = [
        ('BL', 'Black'),
        ('GN', 'Green'),
        ('HB', 'Herbal'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='chai_images/', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50, choices=CHAI_TYPES, default='BL')

    def __str__(self):
        return self.name + " - " + str(self.price)

# one to many
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarietie, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chai_reviews')

    def __str__(self):
        return f"{self.user.username} - {self.chai.name} - {self.rating}"  # pylint: disable=no-member


# many to many
class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVarietie, related_name='stores')

    def __str__(self):
            return f"{self.name}"


# one to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarietie, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.chai.name} - {self.certificate_number}"  # pylint: disable=no-member