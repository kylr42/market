import os
from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}'
    message = f'Дорогой {order.first_name},\n\n' \
              f'Вы успешно разместили заказ.' \
              f'Ваш идентификатор заказа - {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          os.environ.get('EMAIL'),
                          [order.email])
    return mail_sent
