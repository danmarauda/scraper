```python
import json
from scrapy.exporters import JsonItemExporter
from .utils.webhook_sender import WebhookSender

class JsonExportPipeline(object):
    def __init__(self):
        self.file = open("items.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        self.send_data_to_webhook()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def send_data_to_webhook(self):
        with open("items.json", 'r') as file:
            data = json.load(file)
        WebhookSender.send(data)
```