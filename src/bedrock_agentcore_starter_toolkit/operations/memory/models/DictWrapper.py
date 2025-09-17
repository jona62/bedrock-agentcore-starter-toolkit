from typing import Any, Dict


class DictWrapper:
    def __init__(self, data: Dict[str, Any]):
        self._data = data if data is not None else {}

    def __getattr__(self, name: str) -> Any:
        """Provides direct access to data fields as attributes"""
        return self._data.get(name)

    def __getitem__(self, key: str) -> Any:
        """Provides dictionary-style access to data fields"""
        return self._data[key]

    def get(self, key: str, default: Any = None) -> Any:
        """Provides dict.get() style access to data fields"""
        return self._data.get(key, default)

    def __contains__(self, key: str) -> bool:
        """Support 'in' operator for checking if key exists"""
        return key in self._data

    def keys(self):
        """Return keys from the underlying dictionary"""
        return self._data.keys()

    def values(self):
        """Return values from the underlying dictionary"""
        return self._data.values()

    def items(self):
        """Return items from the underlying dictionary"""
        return self._data.items()

    def __dir__(self):
        """Enable tab completion and introspection of available attributes"""
        return list(self._data.keys()) + ['get']

    def __repr__(self):
        return self._data.__repr__()
