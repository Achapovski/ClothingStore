from abc import ABC, abstractmethod


class AbstractModel(ABC):
    # Base abstract model, from which any domain model should be inherited.
    @abstractmethod
    def model_dump(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def model_validate(self, *args, **kwargs):
        raise NotImplementedError
