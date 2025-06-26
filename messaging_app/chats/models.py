from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid  # Import uuid for unique user_id


class User(AbstractUser):
    # Add custom fields here
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)  # Unique identifier
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Optional phone number
    bio = models.TextField(null=True, blank=True)  # Example custom field
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid conflict with auth.User.groups
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Avoid conflict with auth.User.user_permissions
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


class Conversation(models.Model):
    participants = models.ManyToManyField("User", related_name="conversations")  # Use string reference for User
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name="messages")  # Use string reference for User
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender.username}"