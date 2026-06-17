from dataclasses import dataclass, field
from typing import Any


@dataclass
class GameEvent:
    event_type: str
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)


class EventQueue:
    def __init__(self):
        self._events: list[GameEvent] = []

    def push(self, event_type, message="", **data):
        event = GameEvent(event_type=event_type, message=message, data=data)
        self._events.append(event)
        return event

    def drain(self):
        events = self._events
        self._events = []
        return events

    def peek_all(self):
        return list(self._events)
