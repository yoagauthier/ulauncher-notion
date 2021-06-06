from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from notion_api import NotionClient


class NotionExtension(Extension):

    def __init__(self):
        super(NotionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        data = {
            'item_title': event.get_argument()
        }
        items = [
            ExtensionResultItem(
                icon='images/icon.png',
                name='Create Task',
                description='Enter to create the task',
                on_enter=ExtensionCustomAction(data)
            )
        ]

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()

        notion_client = NotionClient(
            api_key=extension.preferences["notion-api-key"],
            database_id=extension.preferences["notion-db-id"]
        )
        notion_client.create_item(
            data['item_title'],
            extension.preferences["notion-db-options"]
        )


if __name__ == '__main__':
    NotionExtension().run()
