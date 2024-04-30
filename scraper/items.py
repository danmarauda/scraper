```python
from scrapy.item import Item, Field

class RedditItem(Item):
    title = Field()
    url = Field()
    author = Field()
    upvotes = Field()
    comments = Field()
```