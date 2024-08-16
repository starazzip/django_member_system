from django.contrib.auth.models import AbstractUser
from django.db import models


class MembershipLevel(models.TextChoices):
    REGULAR = 'regular', '一般會員'
    PAID = 'paid', '付費會員'
    AGENT = 'agent', '代理'
    ADMIN = 'admin', '管理者'
    GOD = 'god', '神'


class CustomUser(AbstractUser):
    membership_level = models.CharField(
        max_length=10,
        choices=MembershipLevel.choices,
        default=MembershipLevel.REGULAR,
    )
    token = models.CharField(max_length=255, blank=True, null=True)
    token_expiry = models.DateTimeField(blank=True, null=True)
    # 可以擴展其他會員屬性
