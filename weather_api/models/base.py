from django.db import models
import json
from var_dump import var_dump

class BaseModel(models.Model):
    def hydrate(self, data):
        # this "just works": get all fields from our CHILD model
        fields = {field.name for field in self._meta.fields}

        for key, value in data.items():
            if key in fields:
                if isinstance(value, (dict, list)):
                    # Convert dicts and lists to JSON strings
                    setattr(self, key, json.dumps(value))
                else:
                    try:
                        json.dumps(value)  # Check if serializable
                        setattr(self, key, value)
                    except TypeError:
                        # Fallback: Convert non-serializable objects to string
                        setattr(self, key, str(value))

    @classmethod
    def fromApi(cls, data):
        book = cls()
        book.hydrate(data)

        return book

    class Meta:
        abstract = True  # Ensures this model doesn't create its own table