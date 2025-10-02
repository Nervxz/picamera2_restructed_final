"""
Picamera2 Restructured - Modular Camera Control Library

A fully restructured and self-contained version of the Picamera2 library.
All modules are organized into logical components for improved maintainability.

Architecture:
- core/: Core camera functionality (Picamera2 class, CameraManager, utilities)
- encoders/: Video/image encoders (H264, MJPEG, JPEG)
- outputs/: Output handlers (File, FFmpeg)
- previews/: Preview windows (DRM, Qt, QtGL, Null)
- allocators/: Memory allocators (DMA, Libcamera)
- devices/: Device-specific modules (IMX500, etc.)
- camera_types/: Type definitions and enums
- Supporting modules: formats, platform, configuration, controls, etc.

Usage:
    from picamera2_restructured import Picamera2, Preview
    
    # Simple capture
    with Picamera2() as camera:
        camera.start()
        camera.capture_file("image.jpg")
        camera.stop()
    
    # With preview
    camera = Picamera2()
    camera.start_preview(Preview.QT)
    config = camera.create_preview_configuration()
    camera.configure(config)
    camera.start()
    # ... do work ...
    camera.stop()
    camera.close()

Features:
- 100% API compatibility with original Picamera2
- Self-contained module (no external picamera2 dependencies)
- Clean modular structure
- 88 public methods fully functional
- Comprehensive type hints

Author: Restructured from raspberrypi/picamera2
Version: 1.0.0-restructured
"""

# Import core classes
from .core.camera_manager import CameraManager
from .core.picamera2_core import Picamera2

# Import camera types
from .camera_types import Preview, GlobalCameraInfo

# Import commonly used classes (optional convenience imports)
from .configuration import CameraConfiguration
from .controls import Controls
from .request import MappedArray, CompletedRequest

__version__ = "1.0.0-restructured"
__author__ = "Raspberry Pi Foundation (Restructured by URLAB Team)"

__all__ = [
    'Picamera2',
    'CameraManager',
    'Preview',
    'GlobalCameraInfo',
    'CameraConfiguration',
    'Controls',
    'MappedArray',
    'CompletedRequest',
]
