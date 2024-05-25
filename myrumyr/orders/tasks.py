from celery import shared_task
from django.core.mail import send_mail

from orders.models import Order, OrderInstance


@shared_task
def order_create_send_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr {order_id}'
    message = (f'Dear{order.first_name}'
               f'You created order {order_id}')

    mail_sent = send_mail(subject, message, 'yaroslawsh04@gmail.com', [order.email])

    return mail_sent


@shared_task
def order_send_pdf_order(order_id):
    order = Order.objects.get(id=order_id)
    order_instances = order.orderinstance_set.all()
    order_text = ''
    subject = 'haalo'
    total_order_sum = 0
    for i in order_instances:
        order_text += f'{i.quantity} {i.product.name}  \n'
        total_order_sum += i.get_cost()
    message = (f'Client {order.first_name} {order.last_name} \n'
               f' Ordered {order_text}: \n '
               f' On total sum {total_order_sum}')
    mail_sent = send_mail(subject, message, 'yaroslawsh04@gmail.com', 'owner@gmail.com')

    return mail_sent


@shared_task
def test_task():
    return 'AAAAAAAAAA'
