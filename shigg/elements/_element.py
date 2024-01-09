from abc import ABC


class Element(ABC):
    def __init__(self) -> None:
        pass

    def step(self, mouse_position, mouse_pressed):
        """Step the element, and return an event if there is one."""
        raise NotImplementedError()
