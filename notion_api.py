import requests
import json
import logging
from gi.repository import Notify
from os.path import dirname, join, realpath


class NotionClient():
    """Notion API client"""

    def __init__(self, api_key=None, database_id=None):
        self.__api_key = api_key
        self.__database_id = database_id
        self.__logger = logging.getLogger(__name__)
        Notify.init('Notion')

    def create_item(self, item_title, item_options=None):

        json_item_options = self.__parse_json(item_options)

        url = 'https://api.notion.com/v1/pages'
        headers = {
            'Authorization': f'Bearer {self.__api_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2021-05-13'
        }

        payload = {
            'parent': {
                'type': 'database_id',
                'database_id': self.__database_id
            },
            'properties': {
                'Title': {
                    'title':  [{'type': 'text', 'text': {'content': item_title}}]
                },
                **json_item_options
            }
        }

        req = requests.post(url, headers=headers, data=json.dumps(payload))
        if (req.status_code != 200):
            self.__logger.warning(f'Could not create item: {req.json()}')
        else:
            notif = Notify.Notification.new(
                "Notion",
                "Task Created",
                join(dirname(realpath(__file__)), 'images/icon.png')
            )
            notif.show()

    def __parse_json(self, json_candidate):
        if (json_candidate == ''):
            return {}

        try:
            json_parsed = json.loads(json_candidate)
            return json_parsed
        except ValueError as e:
            self.__logger.warning(
                "Invalid DB options JSON : %s", json_candidate)
            return {}
        except:
            self.__logger.error("Unknown error")
