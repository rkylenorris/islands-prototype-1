from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name: str, desc: str, examine_txt: str) -> None:
        self.name = name
        self.description = desc
        self.examine_text = examine_txt
        self.is_takeable = False
        self.affected_stats = []
        self.available_actions = ["examine", "touch"]
    
    @abstractmethod
    def can_perform_action(self, action: str) -> bool:
        """Check if the item can perform a specific action."""
        pass
    
    @abstractmethod
    def perform_action(self, action: str) -> str:
        """Perform a specific action with the item."""
        pass
    
    def add_stats(self, stats: list) -> None:
        """Add stats to the item."""
        self.affected_stats.extend(stats)

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
    def __repr__(self) -> str:
        return f"Item(name={self.name}, description={self.description})"
    

class SimpleItem(Item):
    
    def can_perform_action(self, action: str) -> bool:
        return action in self.available_actions
    
    def perform_action(self, action: str) -> str:
        if self.can_perform_action(action):
            return f"Performed action '{action}' on {self.name}."
        else:
            return f"Action '{action}' cannot be performed on {self.name}."


class TakeableItem(Item):
    def __init__(self, name: str, desc: str, examine_txt: str) -> None:
        super().__init__(name, desc, examine_txt)
        self.is_takeable = True
        self.available_actions.append("take")
    
    def can_perform_action(self, action: str) -> bool:
        return action in self.available_actions
    
    def perform_action(self, action: str) -> str:
        if self.can_perform_action(action):
            return f"Performed action '{action}' on {self.name}."
        else:
            return f"Action '{action}' cannot be performed on {self.name}."


class ComplexItem(Item):
    def __init__(self, name: str, desc: str, examine_txt: str) -> None:
        super().__init__(name, desc, examine_txt)
        self.is_takeable = True
        self.affected_stats = []
    
    def can_perform_action(self, action: str) -> bool:
        return action in self.available_actions
    
    def perform_action(self, action: str) -> str:
        if self.can_perform_action(action):
            return f"Performed complex action '{action}' on {self.name}."
        else:
            return f"Action '{action}' cannot be performed on {self.name}."