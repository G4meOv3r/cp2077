from Core.Snippets.Singletone import SingletonMeta

from Core.Input.Input import Input
from Core.Events.Events import Events
from Core.Events.EventsController import EventsController

class InputController(metaclass=SingletonMeta):
    def input(self, key):
        event = None
        
        if key == Input.UP:
            event = Events.KEY_UP_PRESSED
        elif key == Input.RIGHT:
            event = Events.KEY_RIGHT_PRESSED
        elif key == Input.DOWN:
            event = Events.KEY_DOWN_PRESSED
        elif key == Input.LEFT:
            event = Events.KEY_LEFT_PRESSED
        elif key == Input.TAB:
            event = Events.KEY_TAB_PRESSED
        elif key == Input.H:
            event = Events.KEY_H_PRESSED

        EventsController().dispatch(event)
