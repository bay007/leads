import json
import os

import boto3
from botocore.exceptions import BotoCoreError

from . import exceptions as e

QUEUE_NAME = os.getenv("QUEUE_NAME", "sqs_leads_generator")
REGION = os.getenv("REGION", 'us-east-1')


class LeadQueue:
    def __init__(self, name: str, email: str, subject: str, message: str) -> None:
        self._name = name
        self._email = email
        self._subject = subject
        self._message = message

    def queue(self,):
        try:
            sqs = boto3.resource('sqs', region_name=REGION)
            queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
            data = json.dumps({
                "name": self._name,
                "email": self._email,
                "subject": self._subject,
                "message": self._message
            })
            queue.send_message(MessageBody=data)
        except Exception as ex:
            raise e.RoleNotInitialized(detail=str(ex))
