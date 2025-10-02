# Picamera2 Restructured

A fully restructured and modular version of the Picamera2 library with 100% API compatibility.

## Features

✅ **100% API Compatible** - All 88 public methods work identically to original  
✅ **Self-Contained** - No external picamera2 dependencies  
✅ **Modular Architecture** - Clean separation of concerns  
✅ **Type Hints** - Comprehensive type annotations  
✅ **Well Organized** - Logical folder structure

## Structure

```
picamera2_restructured/
├── core/                   # Core camera functionality
│   ├── picamera2_core.py  # Main Picamera2 class (2,574 lines)
│   ├── camera_manager.py  # Camera instance management
│   ├── helpers.py         # Helper utilities
│   └── utils.py           # Core utilities
├── encoders/              # Video/image encoders
├── outputs/               # Output handlers
├── previews/              # Preview windows
├── allocators/            # Memory allocators
├── devices/               # Device-specific modules
├── camera_types/          # Type definitions
└── [Supporting modules]   # formats, platform, configuration, etc.
```

## Usage

```python
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
# ... capture images ...
camera.stop()
camera.close()
```

## API Methods (88 total)

All methods from original Picamera2 are available:

- Configuration: `create_preview_configuration()`, `create_still_configuration()`, `create_video_configuration()`
- Capture: `capture_file()`, `capture_array()`, `capture_image()`, `capture_buffer()`
- Recording: `start_recording()`, `stop_recording()`, `start_encoder()`, `stop_encoder()`
- Preview: `start_preview()`, `stop_preview()`, `attach_preview()`, `detach_preview()`
- Control: `start()`, `stop()`, `configure()`, `set_controls()`, `switch_mode()`
- And 70+ more methods...

## Differences from Original

**Structure Only** - The only difference is the modular organization:

- Original: Single 2,665-line `picamera2.py` + separate module folders
- Restructured: Organized into logical packages, all self-contained

**API Identical** - Every method, property, and behavior is preserved.

## Requirements

Same as original Picamera2:

- libcamera
- numpy
- PIL/Pillow
- And other Raspberry Pi camera dependencies

## Version

**1.0.0-restructured** - Based on Picamera2 v0.3.20

## Credits

Original: Raspberry Pi Foundation  
Restructured by: URLAB Team
