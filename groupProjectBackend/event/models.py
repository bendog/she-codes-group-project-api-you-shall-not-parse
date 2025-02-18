from django.contrib.auth import get_user_model
from django.db import models

from users.models import CustomUser

# Create your models here.
User = get_user_model()


class BaseModel(models.Model):
    """base model for fields to be added to all child models"""

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(BaseModel):
    """the event, used to categorise and group for management"""

    name = models.SlugField(max_length=64)
    description = models.TextField()
    image = models.URLField(null=True)
    published = models.BooleanField(default=False)
    signup_opens = models.DateTimeField()
    signup_closes = models.DateTimeField()
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Role(BaseModel):
    """the roles required for a module"""

    name = models.SlugField(max_length=64)
    capable_mentors = models.ManyToManyField(
        User, related_name="capabilities", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Module(BaseModel):
    """the learning module"""

    name = models.SlugField(max_length=64)
    required_roles = models.ManyToManyField(Role, related_name="modules")

    def __str__(self):
        return self.name


class EventModule(BaseModel):
    """the learning module being taught at the event"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_modules")
    module = models.ForeignKey(Module, on_delete=models.PROTECT, related_name="event_modules")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.event}:{self.module}"

    def populate_roles(self):
        for rec_role in self.module.required_roles.all():
            self.required_roles.create(role=rec_role)


class EventModuleRole(BaseModel):
    event_module = models.ForeignKey(EventModule, models.CASCADE, related_name="required_roles")
    role = models.ForeignKey(Role, models.PROTECT, related_name="event_roles")
    mentor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="registered_roles",
    )
    gift_back = models.BooleanField(default=False)
    sign_up = models.BooleanField(default=False)
    confirmation = models.BooleanField(default=False)
    send_contract = models.BooleanField(default=False)
    received_contract = models.BooleanField(default=False)
    calendar_invites = models.BooleanField(default=False)
    onboarding = models.BooleanField(default=False)
    mentoring = models.BooleanField(default=False)
    invoice_sent = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.mentor}:{self.role}"


