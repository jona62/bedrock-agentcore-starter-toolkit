from typing import Any, Dict

from .DictWrapper import DictWrapper


class Memory(DictWrapper):
    """ A class representing a memory """
    def __init__(self, memory: Dict[str, Any]):
        super().__init__(memory)