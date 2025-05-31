from django.db import models
import json
from var_dump import var_dump

class BaseModel(models.Model):
    def hydrate(self, data):
        fields = {field.name: field for field in self._meta.fields}

        for key, value in data.items():
            if key in fields:
                field = fields[key]
                if isinstance(field, models.JSONField):
                    try:
                        setattr(self, key, value)
                    except TypeError:
                        setattr(self, key, {})  # or {} as fallback
                else:
                    setattr(self, key, value)

    @classmethod
    def fromApi(cls, data):
        if "id" in data:
            del data["id"]

        model = cls()
        model.hydrate(data)

        return model

    class Meta:
        abstract = True  # Ensures this model doesn't create its own table