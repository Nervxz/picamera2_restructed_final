"""
Camera Types - Type definitions and enums for Picamera2

This module provides TypedDict, Enum, and other type definitions used throughout Picamera2.
"""

from enum import Enum
from typing import TypedDict, Any

# Import preview classes
from ..previews.null_preview import NullPreview
from ..previews.drm_preview import DrmPreview
from ..previews.qt_previews import QtPreview, QtGlPreview


class Preview(Enum):
    """Enum that applications can pass to the start_preview method."""
    NULL = NullPreview
    DRM = DrmPreview
    QT = QtPreview
    QTGL = QtGlPreview


class GlobalCameraInfo(TypedDict):
    """
    TypedDict for camera information fields.

    Fields:
        Model: The model name of the camera, as advertised by the camera driver.
        Location: A number reporting how the camera is mounted, as reported by libcamera.
        Rotation: How the camera is rotated for normal operation, as reported by libcamera.
        Id: An identifier string for the camera, indicating how the camera is connected.
        Num: A camera index.
    """
    Model: str
    Location: int
    Rotation: int
    Id: str
    Num: int


__all__ = [
    'Preview',
    'GlobalCameraInfo'
]
