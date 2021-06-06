# Ulauncher Notion

## Setup

1. Create a [Notion extension](https://developers.notion.com/docs/getting-started) in your workspace.
2. Generate a secret API key, and set it up in the Ulauncher panel.
3. Find the id of the database you want to create an item in, and set it up in the Ulauncher panel.

## Options

The text you enter will be the title of the page (or database entry).

If you want to setup other fields on that page / entry, you can do it by providing a JSON like the one below.

See [Notion doc](https://developers.notion.com/reference/page#page-property-value) for the availables fields.

```json
{
  "Status": {
    "type": "select",
    "select": {
      "name": "Inbox"
    }
  }
}
```
