import logging

from modis import main

from . import _flipcheck

logger = logging.getLogger(__name__)


async def on_message(msgobj):
    """The on_message event handler for this module

    Args:
        msgobj (discord.Message): Input message
    """

    # TODO work out how to make this conform to new activation

    # Ignore PMs and don't reply to self
    if msgobj.guild is None or msgobj.author == main.client.user:
        return

    # Do a flip check
    flipchecked = _flipcheck.check(msgobj.content)
    if flipchecked:
        await msgobj.channel.trigger_typing()
        await msgobj.channel.send(flipchecked)
