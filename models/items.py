from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name: str, desc: str, examine_txt: str) -> None:
        self.name = name
        self.description = desc
        self.examine_text = examine_txt
        self.is_takeable = False
        self.affected_stats = []
        self.available_actions = []
    
    @abstractmethod
    def can_perform_action(self, action: str) -> bool:
        """Check if the item can perform a specific action."""
        pass
    
    @abstractmethod
    def perform_action(self, action: str) -> str:
        """Perform a specific action with the item."""
        pass