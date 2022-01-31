"""5 question 6 sprint"""
import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = {"module": json, "mode": "w"}
    BYTE = {"module": pickle, "mode": "bw"}


class SerializeManager:
    def __init__(self, filename, fileType):
        self._filename = filename
        self._fileType = fileType

    def __enter__(self):
        self.__file = open(self._filename, self._fileType.value["mode"])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

    def serialize(self, object):
        self._fileType.value["module"].dump(object, self.__file)


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


if __name__ == '__main__':
    user_dict = {'name': 'Roman', 'id': 8}
    f = "string.json"
    serialize(user_dict, f, FileType.JSON)
    serialize(user_dict, "2", FileType.BYTE)
