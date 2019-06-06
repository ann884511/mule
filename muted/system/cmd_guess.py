
from __future__ import annotations

from typing import List
from typing import Type

from component.name import Name
from component.role import Role

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat

class CmdGuess:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_GUESS, self._on_cmd_guess)

    @LogCat.log_func
    def _on_cmd_guess(
        self, e: Event, entity: str = '', args: List[str] = []
    ) -> None:
        temp = input("心裡所想數字:  ")
        guess = int(temp)
        if guess == 8:
                 print("你猜對了")
                 print("猜對也沒用")
        else:        
                 print("猜錯了，偷偷告訴你我想的是8")
        print("遊戲結束，不玩拉")         
        Channel.to_role(entity, Message.TEXT, text)

# cmd_echo.py
