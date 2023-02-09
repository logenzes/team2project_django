from django.db import models
from django.utils.timezone import now

# Create your models here.

class Users(models.Model):
    userid      = models.CharField("아이디", max_length=50, unique=True)
    passwrd     = models.CharField("비밀번호", max_length=256)
    email       = models.EmailField("이메일", max_length=100, unique=True)
    tracking    = models.BooleanField("회원상태", default=True)
    insert_date = models.DateTimeField("insert date")
    update_date = models.DateTimeField("update date")

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
        ordering = ["-insert_date"]

    def save(self, *arg, **kwargs):
        if not self.id:
            self.insert_date = now()
        self.update_date = now()
        super(Users, self).save(*arg, **kwargs)