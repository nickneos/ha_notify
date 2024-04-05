from requests import post
import os
import logging

logger = logging.getLogger(__name__)


class HomeAssistantNotify:

    def __init__(
        self,
        ha_url="http://127.0.0.1:8123",
        token=None,
        endpoint=None,
    ):
        self.url = os.path.join(ha_url, endpoint)
        self.headers = {"Authorization": f"Bearer {token}"}

    def send_msg(self, **kvargs):
        response = post(self.url, headers=self.headers, json=kvargs)
        if response.status_code == 200:
            logger.info("Sent notification via HA")
        else:
            logger.error(
                f"Couldn't send notification via HA: {response.status_code} - {response.text}"
            )
