from dataclasses import dataclass, field


@dataclass
class Resources:
    health: int
    max_health: int
    stamina: int
    max_stamina: int
    armor: int

    @classmethod
    def from_data(cls, data):
        return cls(
            health=data["health"],
            max_health=data["max_health"],
            stamina=data["stamina"],
            max_stamina=data["max_stamina"],
            armor=data["armor"],
        )


@dataclass
class Entity:
    entity_id: str
    name: str
    symbol: str
    x: int
    y: int
    level: int
    role: str
    entity_type: str
    resources: Resources
    tags: list[str] = field(default_factory=list)
    stats: dict[str, int] = field(default_factory=dict)
    inventory: list[str] = field(default_factory=list)
    equipment: dict[str, str] = field(default_factory=dict)
    debuffs: list[str] = field(default_factory=list)
    buffs: list[str] = field(default_factory=list)
    status_effects: list[str] = field(default_factory=list)
    state: dict = field(default_factory=dict)

    @classmethod
    def from_data(cls, entity_id, data):
        return cls(
            entity_id=entity_id,
            name=data["name"],
            symbol=data["symbol"],
            x=data["position"]["x"],
            y=data["position"]["y"],
            level=data["level"],
            role=data["role"],
            entity_type=data["entity_type"],
            resources=Resources.from_data(data["resources"]),
            tags=data.get("tags", []),
            stats=data.get("stats", {}),
            inventory=data.get("inventory", []),
            equipment=data.get("equipment", {}),
            debuffs=data.get("debuffs", []),
            buffs=data.get("buffs", []),
            status_effects=data.get("status_effects", []),
            state=data.get("state", {}),
        )


@dataclass
class WorldObject:
    object_id: str
    name: str
    symbol: str
    x: int
    y: int
    object_type: str
    blocks_movement: bool
    state: dict = field(default_factory=dict)
    shop_inventory: list[str] = field(default_factory=list)

    @classmethod
    def from_data(cls, object_id, data):
        return cls(
            object_id=object_id,
            name=data["name"],
            symbol=data["symbol"],
            x=data["position"]["x"],
            y=data["position"]["y"],
            object_type=data["object_type"],
            blocks_movement=data["blocks_movement"],
            state=data.get("state", {}),
            shop_inventory=data.get("shop_inventory", []),
        )


@dataclass
class Hazard:
    hazard_id: str
    name: str
    symbol: str
    x: int
    y: int
    effect: str
    severity: int = 0
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_data(cls, hazard_id, data):
        return cls(
            hazard_id=hazard_id,
            name=data["name"],
            symbol=data["symbol"],
            x=data["position"]["x"],
            y=data["position"]["y"],
            effect=data["effect"],
            severity=data.get("severity", 0),
            tags=data.get("tags", []),
        )
