from django.contrib.auth.models import AbstractUser, UserManager

from django.utils import timezone

from django.db import models

# Create your models here.


class AccountUserManager (UserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        """creates and saves a user with the given username, email and password"""

        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractUser):
    #Now that we've abstracted this class we can add any number of customer attribute to our user class.
    #In later units we'll be adding things like payment details.
    objects = AccountUserManager()

    #stripe_id field is added as a CharField, so when the registration form is saved, we'll also retain our new token/id.
    stripe_id = models.CharField(max_length=40, default='')

    subscription_end = models.DateTimeField(default=timezone.now)

    def is_subscribed(self, magazine):
        try:
            purchase = self.purchase.get(magazine__pk=magazine.pk)
        except Exception:
            return False

        if purchase.subscription_end > timezone.now():
            return False

        return True