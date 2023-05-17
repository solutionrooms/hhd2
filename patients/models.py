from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class Patient(models.Model):
    patient_name = models.TextField(unique=True)
    finder_name = models.TextField(unique=False,blank=True)
    sex = models.TextField(unique=False,blank=True,choices=[('Male','Male'),
                                                            ('Femail','Femail'),
                                                            ('Unknown','Unknown')])
    age_years = models.FloatField(unique=False, blank=True)
    wants_back = models.BooleanField(unique=False,default=False)
    current_weather = models.TextField(unique=False, blank=True)
    comments = models.TextField(unique=False, blank=True)
    cold_flag = models.BooleanField(unique=False,default=False)
    fly_strike_flag = models.BooleanField(unique=False,default=False)
    wounds_flag = models.BooleanField(unique=False,default=False)
    sneezing_flag = models.BooleanField(unique=False,default=False)
    dehydrated_flag = models.BooleanField(unique=False,default=False)
    maggots_flag = models.BooleanField(unique=False,default=False)
    limping_flag = models.BooleanField(unique=False,default=False)
    snotty_flag = models.BooleanField(unique=False,default=False)
    underweight_flag = models.BooleanField(unique=False,default=False)
    ticks_flag = models.BooleanField(unique=False,default=False)
    smell_flag = models.BooleanField(unique=False,default=False)
    limp_flag = models.BooleanField(unique=False,default=False)
    fleas_flag = models.BooleanField(unique=False,default=False)
    pus_or_infection = models.BooleanField(unique=False,default=False)
    course_of_action = models.TextField(unique=False, blank=True)
    microchip = models.TextField(unique=False, blank=True)
    poo_sample = models.BooleanField(unique=False,default=False)
    poo_parasites = models.TextField(unique=False, blank=True)
    fluids_given = models.BooleanField(unique=False,default=False)
    fluid_amount = models.FloatField(unique=False, blank=True)
    vet_needed = models.BooleanField(unique=False,default=False)
    incubator_flag = models.BooleanField(unique=False,default=False)
    incubator_starting_temp_c = models.FloatField(unique=False, blank=True)

    description = models.TextField(blank=True, null=True)
    patient_status = models.TextField()
    inserted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.patient_name}"


class CarerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Carer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.TextField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number_home = models.TextField(blank=True, null=True)
    phone_number_mobile = models.TextField(blank=True, null=True)
    opted_out = models.BooleanField(default=False)
    carer_status_id = models.IntegerField()
    inserted_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CarerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="carer_set",
        related_query_name="carer",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="carer_set",
        related_query_name="carer",
    )
    def __str__(self):
        return self.email

class Measurement(models.Model):
    measurement_timestamp = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    carer = models.ForeignKey(Carer, on_delete=models.CASCADE)
    weight_grams = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)

