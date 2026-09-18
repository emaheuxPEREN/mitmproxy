from __future__ import annotations

import typing
from contextvars import ContextVar

if typing.TYPE_CHECKING:
    import mitmproxy.log
    import mitmproxy.master
    import mitmproxy.options

_master: ContextVar[mitmproxy.master.Master] = ContextVar("mitmproxy.ctx.master")
_options: ContextVar[mitmproxy.options.Options] = ContextVar("mitmproxy.ctx.options")
_log: ContextVar[mitmproxy.log.Log] = ContextVar("mitmproxy.ctx.log")


class ContextProxy:
    """Task-safe context proxy"""

    @property
    def master(self) -> mitmproxy.master.Master:
        return _master.get()

    @master.setter
    def master(self, master: mitmproxy.master.Master) -> None:
        _master.set(master)

    @property
    def options(self) -> mitmproxy.options.Options:
        return _options.get()

    @options.setter
    def options(self, options: mitmproxy.options.Options) -> None:
        _options.set(options)

    @property
    def log(self) -> mitmproxy.log.Log:
        """Deprecated: Use Python's builtin `logging` module instead."""
        return _log.get()

    @log.setter
    def log(self, log: mitmproxy.log.Log) -> None:
        _log.set(log)


ctx: typing.Final = ContextProxy()
