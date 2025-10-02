"""Helper classes and utilities for Picamera2 core."""

from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class classproperty(property, Generic[T]):
    """
    A decorator that allows creating class-level properties.
    
    This is used in Picamera2 for the deprecated logging level properties
    (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    
    Example:
        >>> class MyClass:
        ...     @classproperty
        ...     def my_property(cls):
        ...         return "class property value"
        ...
        >>> MyClass.my_property
        'class property value'
    """
    
    def __init__(self, fget: Callable[[type], T]) -> None:
        """
        Initialize the classproperty.
        
        :param fget: The getter function that takes a class as argument
        :type fget: Callable[[type], T]
        """
        super().__init__(fget)

    def __get__(self, obj, cls=None) -> T:
        """
        Get the property value.
        
        :param obj: The instance (unused for class properties)
        :param cls: The class
        :return: The property value
        :rtype: T
        """
        if cls is None:
            cls = type(obj)
        assert self.fget is not None
        return self.fget(cls)
