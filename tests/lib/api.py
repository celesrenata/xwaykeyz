from evdev.ecodes import EV_KEY, EV_SYN
from evdev.events import InputEvent

from xkeysnail.key import Action
from xkeysnail.transform import on_event

from lib.xorg_mock import set_window

_kb = "generic keyboard"

PRESS = Action.PRESS
RELEASE = Action.RELEASE

def using_keyboard(name):
    global _kb
    _kb = name

def window(name):
    set_window(name)

def press(key):
    ev = InputEvent(0, 0, EV_KEY, key, Action.PRESS)
    on_event(ev, _kb, quiet = False)

def release(key):
    ev = InputEvent(0, 0, EV_KEY, key, Action.RELEASE)
    on_event(ev, _kb, quiet = False)

def hit(key):
    press(key)
    release(key)