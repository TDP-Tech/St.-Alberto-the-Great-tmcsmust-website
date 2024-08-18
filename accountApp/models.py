from django.db import models
from django.conf import settings
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=50, null=True, blank=True)
    carrier = models.TextField(null=True, blank=True) 
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        return self.displayname if self.displayname else self.user.first_name
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        else:
            return static('images/avatar.JPG')
