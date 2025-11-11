from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict

@dataclass
class Node:
    type: str
    value: Optional[Union[str, int, float, bool]] = None
    children: List["Node"] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)

    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "children": [c.to_dict() for c in self.children],
            "metadata": self.metadata,
        }

    @staticmethod
    def from_dict(data):
        return Node(
            type=data["type"],
            value=data.get("value"),
            children=[Node.from_dict(c) for c in data.get("children", [])],
            metadata=data.get("metadata", {}),
        )
