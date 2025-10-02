"""
Camera Manager - Manages libcamera camera instances and request handling

This module handles the lifecycle of camera instances and processes incoming requests
from the libcamera framework.
"""

import os
import selectors
import threading
from typing import Optional, Dict

import libcamera

# Import CompletedRequest directly - no circular dependency issue
from ..request import CompletedRequest


class CameraManager:
    """
    Manages libcamera camera instances and handles request processing.
    
    This class coordinates multiple camera instances and processes their
    requests through a background thread with event-driven architecture.
    """
    
    def __init__(self):
        self.running = False
        self.cameras: Dict[int, any] = {}
        self._lock = threading.Lock()
        self._cms: Optional[libcamera.CameraManager] = None

    def setup(self) -> None:
        """Start the background thread for handling camera requests."""
        self.thread = threading.Thread(target=self.listen, daemon=True)
        self.running = True
        self.thread.start()

    @property
    def cms(self) -> libcamera.CameraManager:
        """Get or create the libcamera CameraManager singleton."""
        if self._cms is None:
            self._cms = libcamera.CameraManager.singleton()
        return self._cms

    def reset(self) -> None:
        """Reset the camera manager by recreating the singleton."""
        with self._lock:
            self._cms = None
            self._cms = libcamera.CameraManager.singleton()

    def add(self, index: int, camera) -> None:
        """
        Add a camera instance to be managed.
        
        :param index: Camera index
        :param camera: Picamera2 instance
        """
        with self._lock:
            self.cameras[index] = camera
            if not self.running:
                self.setup()

    def cleanup(self, index: int) -> None:
        """
        Remove a camera instance and cleanup if no cameras remain.
        
        :param index: Camera index to remove
        """
        flag = False
        with self._lock:
            del self.cameras[index]
            if self.cameras == {}:
                self.running = False
                flag = True
        if flag:
            self.thread.join()
            self._cms = None

    def listen(self) -> None:
        """Background thread that listens for and processes camera events."""
        sel = selectors.DefaultSelector()
        sel.register(self.cms.event_fd, selectors.EVENT_READ, self.handle_request)

        while self.running:
            events = sel.select(0.2)
            for key, _ in events:
                callback = key.data
                callback()

        sel.unregister(self.cms.event_fd)
        self._cms = None

    def handle_request(self, flushid=None) -> None:
        """
        Handle incoming requests from cameras.
        
        :param flushid: Optional flush ID to filter requests
        """
        with self._lock:
            cams = set()
            for req in self.cms.get_ready_requests():
                if req.status == libcamera.Request.Status.Complete and req.cookie != flushid:
                    cams.add(req.cookie)
                    with self.cameras[req.cookie]._requestslock:
                        self.cameras[req.cookie]._requests += [
                            CompletedRequest(req, self.cameras[req.cookie])
                        ]
            for c in cams:
                os.write(self.cameras[c].notifyme_w, b"\x00")


__all__ = ['CameraManager']
