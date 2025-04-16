import os
import uuid
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible


@deconstructible
class RenameFileImage:
    def __init__(self, sub_path, name_attr="name"):
        self.sub_path = sub_path
        self.name_attr = name_attr  # tên trường dùng để slug tên file

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        name_value = getattr(instance, self.name_attr, "file")
        slug_name = slugify(name_value)
        filename = f"{slug_name}-{uuid.uuid4().hex}.{ext}"
        return os.path.join(self.sub_path, filename)
