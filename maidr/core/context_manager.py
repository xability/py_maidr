import contextlib
import contextvars
import threading

import wrapt


class ContextManager:
    _instance = None
    _lock = threading.Lock()

    _internal_context = contextvars.ContextVar("internal_context", default=False)

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ContextManager, cls).__new__()
        return cls._instance

    @classmethod
    @contextlib.contextmanager
    def set_internal_context(cls):
        token_internal_context = cls._internal_context.set(True)
        try:
            yield
        finally:
            cls._internal_context.reset(token_internal_context)

    @classmethod
    def is_internal_context(cls):
        return cls._internal_context.get()


@wrapt.decorator
def manage_context(wrapped=None, _=None, args=None, kwargs=None):
    # Don't proceed if the call is made internally by the patched function.
    if ContextManager.is_internal_context():
        return wrapped(*args, **kwargs)

    # Set the internal context to avoid cyclic processing.
    with ContextManager.set_internal_context():
        return wrapped(*args, **kwargs)
