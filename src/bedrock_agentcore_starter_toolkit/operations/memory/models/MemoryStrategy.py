from typing import Any, Dict

from .DictWrapper import DictWrapper

class MemoryStrategy(DictWrapper):
    """ A class representing a memory strategy """
    def __init__(self, memory_strategy: Dict[str, Any]):
        super().__init__(memory_strategy)