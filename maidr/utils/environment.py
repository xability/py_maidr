class Environment:
    @staticmethod
    def is_interactive_shell() -> bool:
        """Return True if the environment is an interactive shell."""
        try:
            from IPython.core.interactiveshell import InteractiveShell

            return (
                InteractiveShell.initialized()
                and InteractiveShell.instance() is not None
            )
        except ImportError:
            return False
