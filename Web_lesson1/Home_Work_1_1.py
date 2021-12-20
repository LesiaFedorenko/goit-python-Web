from abc import abstractmethod, ABC
import pickle
import json


class SerializationInterface(ABC):
    @abstractmethod
    def __init__(self, some_data, file_name):
        self.some_data = some_data
        self.file_name = file_name

    @abstractmethod
    def serializate(self):
        pass


class SerializationPickle(SerializationInterface):
    def __init__(self, some_data, file_name):
        super(SerializationPickle, self).__init__(some_data, file_name)

    def serializate(self):
        byte_string = pickle.dumps(self.some_data)
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.some_data, fh)
        return byte_string


class SerializationJson(SerializationInterface):
    def __init__(self, some_data, file_name):
        super(SerializationJson, self).__init__(some_data, file_name)

    def serializate(self):
        byte_string = json.dumps(self.some_data)
        with open(self.file_name, "w") as fh:
            json.dump(self.some_data, fh)
        return byte_string


some_data = {
    1: 'class',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}
a = SerializationJson(some_data, 'data.bin')
print(a.serializate())

b = SerializationPickle(some_data, 'data.json')
print(b.serializate())


