from celery import shared_task
from django.core.mail import send_mail

from orders.models import Order

@shared_task
def order_create_send_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr {order_id}'
    message = (f'Dear{order.first_name}'
               f'You created order {order_id}')

    mail_sent=send_mail(subject, message, 'yaroslawsh04@gmail.com', [order.email])

    return mail_sent