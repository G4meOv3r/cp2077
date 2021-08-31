from Core.Snippets.Singletone import SingletonMeta

class EventCallback:
    def __init__(self, event, callback, *args, **kwargs):
        self.event = event
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.callback(*self.args, **self.kwargs)

class EventsController(metaclass=SingletonMeta):
    def __init__(self):
        self._subscribers_by_event = {}
        self._subscribers = []
    
    def dispatch(self, e) -> None:
        try:
            subscribers_numbers = self._subscribers_by_event[e]
            for subscriber_number in subscribers_numbers:
                self._subscribers[subscriber_number]()
        except Exception as e:
            pass
    
    def subscribe(self, event, callback, *args, **kwargs) -> int:
        subscriber_number = len(self._subscribers)
        self._subscribers.append(EventCallback(event, callback, *args, **kwargs))
        try:
            self._subscribers_by_event[event].append(subscriber_number)
        except:
            self._subscribers_by_event[event] = [subscriber_number]
        return subscriber_number

    def unsubscribe(self, subscribe_number : int) -> None:
        try:
            subscribe_callback = self._subscribers.pop(subscribe_number)
            subscribers_by_event = self._subscribers_by_event[subscribe_callback]
            subscribers_by_event.pop(subscribers_by_event.index(subscribe_number))
        except:
            pass