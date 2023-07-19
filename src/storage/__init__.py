import json
import os
import typing as t
import uuid

import aiofiles

import config as conf
import constants as const


class FileStorage:
    def __init__(self, source_name: str = const.SOURCE_NAME):
        self.source_name = source_name

    async def store(self, resource_data: t.Iterable, to: t.Annotated[str, "Filename"]) -> None:
        async with aiofiles.open(os.path.join(conf.OUTPUT_DIR, to), "w") as out:
            await out.write(json.dumps({"id": str(uuid.uuid4()), "metadata": self.source_name, "raw_data": list(resource_data)}))
            await out.flush()
