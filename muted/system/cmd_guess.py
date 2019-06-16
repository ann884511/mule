
from __future__ import annotations

from typing import List
from typing import Type

from component.name import Name
from component.role import Role

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat
import random
class CmdGuess:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_GUESS, self._on_cmd_guess)

    @LogCat.log_func
    def _on_cmd_guess(
        self, e: Event, entity: str = '', args: List[str] = []
    ) -> None:
        if not args:
            text = f'張三 說:請猜一個數字(1~10)'
            #Channel.to_role(entity, Message.TEXT, text)
        else:
            s = args[0]
            if s != '1':
                text = f'張三 說：猜錯囉，在猜一次'
            else:
                text = f'Echo 說: {"答對了"}'
            role = Role.instance(entity)
        Channel.to_role(entity, Message.TEXT, text)

# cmd_echo.py
