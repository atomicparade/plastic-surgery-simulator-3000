"""Classes and functions used by multiple command modules."""
from typing import Any, Optional


class StrOptions:
    "A set of string options for a command."
    _options: list[str]
    _getattr_dict: dict[str, str]
    _default: str

    def __init__(self, *args: Any, default: Optional[Any] = None):
        if len(args) == 0:
            raise ValueError("No options provided")

        self._options = [str(arg) for arg in args]

        self._getattr_dict = {}
        for option in self._options:
            self._getattr_dict[option.strip().lower().replace(" ", "_")] = option

        if default is None:
            self._default = self._options[0]
        else:
            default_str = str(default)

            if default_str not in self._options:
                raise ValueError("Default must be in options")

            self._default = default_str

        self.__iter__ = self._options.__iter__

    @property
    def default(self) -> str:
        """The default option."""
        return self._default

    def __len__(self) -> int:
        return len(self._options)

    def __getitem__(self, key: int) -> str:
        return self._options[key]

    def __getattr__(self, name: str) -> str:
        if not name in self._getattr_dict:
            raise IndexError(f"Option {name} not found")

        return self._getattr_dict[name]
