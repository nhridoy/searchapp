from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email is Required!!!')
        if not username:
            raise ValueError('Username is Required!!!')
        if not password:
            raise ValueError('Password is Required!!!')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False, verbose_name='Email Address', max_length=264)
    username = models.CharField(unique=True, blank=False, verbose_name='Username', max_length=264)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')

    is_superuser = models.BooleanField(default=False, help_text="Designate the superuser status",
                                       verbose_name="Superuser Status")
    is_staff = models.BooleanField(default=False, help_text="Designate the staff status", verbose_name="Staff Status")
    is_active = models.BooleanField(default=True, help_text="Designate the active status", verbose_name="Active Status")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


def get_profile_images_filepath(self, filename):
    return f"users/{self.pk}/{'profile-pic.png'}"


def default_profile_image():
    return f"face1.jpg"


# User Basic Info Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to=get_profile_images_filepath, default=default_profile_image,
                                    verbose_name="Profile Picture")
    full_name = models.CharField(verbose_name="Full Name", max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()
