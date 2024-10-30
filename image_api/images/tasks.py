from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def image_event_log(event_type, image_id):
    message = f"Event: {event_type}, Image ID: {image_id}"
    logger.info(message)
    print(message)
