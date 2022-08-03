from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
def otp_mail(email):
    subject = "Please verify"
    otp = random.randint(1000,9999)
    message = f'otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()