"""Signal handling module"""
import os
import signal
import gettext
from gi.repository import GLib
from lutris.util.log import logger

PID_HANDLERS = {}


def sigchld_handler(_signum, _frame):
    """This handler uses SIGCHLD as a trigger to check on the runner process
    in order to detect the monitoredcommand's complete exit asynchronously."""
    try:
        pid, returncode, _ = os.wait3(os.WNOHANG)
    except ChildProcessError as ex:  # already handled by someone else
        logger.debug(gettext.gettext("Wait call failed: %s"), ex)
        return
    try:
        handler = PID_HANDLERS.pop(pid)
    except KeyError:
        return
    GLib.timeout_add(0, handler, returncode)


def register_handler(pid, handler):
    """Attaches a callback to a pid, called when the process stops"""
    logger.debug(gettext.gettext("Registering %s to %s"), handler, pid)
    PID_HANDLERS[pid] = handler


signal.signal(signal.SIGCHLD, sigchld_handler)
