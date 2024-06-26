# # products/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Product
# from .tasks import scrape_product_url_task

# @receiver(post_save, sender=Product)
# def scrape_product_after_save(sender, instance, created, **kwargs):
#     if created and instance.url:
#         scrape_product_url_task.delay(instance.url)
