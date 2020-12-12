import json
import os

import boto3
from botocore.exceptions import BotoCoreError

from . import exceptions as e

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", None)
REGION = os.getenv("REGION", 'us-east-1')


class LeadSNS:
    def __init__(self, name: str, email: str, subject: str, message: str) -> None:
        self._name = name
        self._email = email
        self._subject = subject
        self._message = message

    def send(self,):
        if SNS_TOPIC_ARN is None:
            return None

        try:
            sns =boto3.resource('sns', region_name=REGION)
            topic = sns.Topic(SNS_TOPIC_ARN)
            message = f"Nuevo lead registrado con email {self._email}"

            topic.publish(
                Message=message
            )

        except Exception as ex:
            raise e.RoleNotInitialized(detail=str(ex))
