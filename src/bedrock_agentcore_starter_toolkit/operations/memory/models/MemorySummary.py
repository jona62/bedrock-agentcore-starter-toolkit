from typing import Any, Dict

from .DictWrapper import DictWrapper


class MemorySummary(DictWrapper):
    """ A class representing a memory summary """
    def __init__(self, memory_summary: Dict[str, Any]):
        super().__init__(memory_summary)