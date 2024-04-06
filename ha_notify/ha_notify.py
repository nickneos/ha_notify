from requests import post
import os
import logging

logger = logging.getLogger(__name__)


class HomeAssistantNotify:
    """
    A class to represent a `HomeAssistantNotify` object.

    Attributes:
        url (str): The url and endpoint to send the request to.
        headers (dict): headers to include in the http post request.
    """

    def __init__(
        self,
        ha_url="http://127.0.0.1:8123",
        endpoint="/api/services/notify/notify",
        token=None
    ):
        """Initialize `HomeAssistantNotify` class.

        Args:
            ha_url (str): The URL of your Home Assistant server. Defaults to `http://127.0.0.1:8123`.
            endpoint (str): The endpoint to send the api request.
            token (str): Your home assistant api token.
        """
        self.url = os.path.join(ha_url, endpoint)
        self.headers = {"Authorization": f"Bearer {token}"}

    def send_msg(self, message, **kwargs):
        """Sends a message via home assistants notify service.

        Args:
            message (str): The message to send in the notification
            **kwargs: Additional key value pairs to include in the payload.
                        Refer to https://www.home-assistant.io/integrations/notify#service
                        for additional optional keys.
        """
        payload = {"message": message, **kwargs}
        response = post(self.url, headers=self.headers, json=payload)
        if response.status_code == 200:
            logger.info("Sent notification via HA")
        else:
            logger.error(
                f"Couldn't send notification via HA: {response.status_code} - {response.text}"
            )
