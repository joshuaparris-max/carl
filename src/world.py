from src.entity import Entity, Hazard, WorldObject


BLOCKED_TILES = {"#", "="}
TERRAIN_EFFECTS = {
    "~": "filth",
    "!": "trap",
    "^": "rough",
}


class GameWorld:
    def __init__(self, map_rows, characters, objects=None, hazards=None):
        self.grid = [list(row) for row in map_rows]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.entities = {
            entity_id: Entity.from_data(entity_id, data)
            for entity_id, data in characters.items()
        }
        self.objects = {
            object_id: WorldObject.from_data(object_id, data)
            for object_id, data in (objects or {}).items()
        }
        self.hazards = {
            hazard_id: Hazard.from_data(hazard_id, data)
            for hazard_id, data in (hazards or {}).items()
        }

    @property
    def carl(self):
        return self.entities["carl"]

    @property
    def donut(self):
        return self.entities["donut"]

    @property
    def mordecai(self):
        return self.entities["mordecai"]

    def tile_at(self, x, y):
        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return "#"
        return self.grid[y][x]

    def is_blocked(self, x, y, ignore_entities=None):
        ignore_entities = set(ignore_entities or [])
        if self.tile_at(x, y) in BLOCKED_TILES:
            return True
        if any(obj.x == x and obj.y == y and obj.blocks_movement for obj in self.objects.values()):
            return True
        return any(
            entity.x == x
            and entity.y == y
            and entity.entity_id not in ignore_entities
            and entity.resources.health > 0
            for entity in self.entities.values()
        )

    def move_entity(self, entity_id, dx, dy):
        entity = self.entities[entity_id]
        new_x = entity.x + dx
        new_y = entity.y + dy
        if self.is_blocked(new_x, new_y, ignore_entities={entity_id}):
            return False

        entity.state["previous_position"] = {"x": entity.x, "y": entity.y}
        entity.x = new_x
        entity.y = new_y
        return True

    def move_carl(self, dx, dy):
        old_x, old_y = self.carl.x, self.carl.y
        moved = self.move_entity("carl", dx, dy)
        if moved:
            self.donut.x = old_x
            self.donut.y = old_y
        return moved

    def follow_entity(self, follower_id, leader_id):
        follower = self.entities[follower_id]
        leader = self.entities[leader_id]
        previous = leader.state.get("previous_position")
        if not previous:
            return False
        if self.is_blocked(previous["x"], previous["y"], ignore_entities={follower_id, leader_id}):
            return self.step_toward(follower_id, leader.x, leader.y)
        follower.x = previous["x"]
        follower.y = previous["y"]
        return True

    def step_toward(self, entity_id, target_x, target_y):
        entity = self.entities[entity_id]
        options = []
        if target_x != entity.x:
            options.append((1 if target_x > entity.x else -1, 0))
        if target_y != entity.y:
            options.append((0, 1 if target_y > entity.y else -1))
        options.extend([(0, -1), (1, 0), (0, 1), (-1, 0)])
        for dx, dy in options:
            new_x = entity.x + dx
            new_y = entity.y + dy
            if not self.is_blocked(new_x, new_y, ignore_entities={entity_id}):
                entity.state["previous_position"] = {"x": entity.x, "y": entity.y}
                entity.x = new_x
                entity.y = new_y
                return True
        return False

    def near(self, entity_id, distance=1):
        entity = self.entities[entity_id]
        return abs(self.carl.x - entity.x) <= distance and abs(self.carl.y - entity.y) <= distance

    def near_entity(self, entity_type=None, distance=1):
        for entity in self.entities.values():
            if entity.entity_id == "carl" or entity.resources.health <= 0:
                continue
            if entity_type and entity.entity_type != entity_type:
                continue
            if abs(self.carl.x - entity.x) <= distance and abs(self.carl.y - entity.y) <= distance:
                return entity
        return None

    def near_tile(self, tile, distance=1):
        for y in range(max(0, self.carl.y - distance), min(self.height, self.carl.y + distance + 1)):
            for x in range(max(0, self.carl.x - distance), min(self.width, self.carl.x + distance + 1)):
                if self.grid[y][x] == tile:
                    return x, y
        return None

    def near_object(self, object_type=None, distance=1):
        for obj in self.objects.values():
            if object_type and obj.object_type != object_type:
                continue
            if abs(self.carl.x - obj.x) <= distance and abs(self.carl.y - obj.y) <= distance:
                return obj
        return None

    def object_at(self, x, y):
        for obj in self.objects.values():
            if obj.x == x and obj.y == y:
                return obj
        return None

    def hazard_at(self, x, y):
        for hazard in self.hazards.values():
            if hazard.x == x and hazard.y == y:
                return hazard
        return None

    def terrain_effect_at(self, x, y):
        hazard = self.hazard_at(x, y)
        if hazard:
            return hazard.effect
        return TERRAIN_EFFECTS.get(self.tile_at(x, y))

    def living_enemies_near(self, entity_id, distance=1):
        origin = self.entities[entity_id]
        return [
            enemy
            for enemy in self.entities_by_type("monster")
            if enemy.resources.health > 0
            and abs(origin.x - enemy.x) <= distance
            and abs(origin.y - enemy.y) <= distance
        ]

    def entities_by_type(self, entity_type):
        return [entity for entity in self.entities.values() if entity.entity_type == entity_type]

    def replace_tile(self, x, y, tile):
        self.grid[y][x] = tile

    def render(self):
        rows = []
        for y in range(self.height):
            chars = []
            for x in range(self.width):
                symbol = self.grid[y][x]
                hazard = self.hazard_at(x, y)
                if hazard:
                    symbol = hazard.symbol
                obj = self.object_at(x, y)
                if obj:
                    symbol = obj.symbol
                for entity in self.entities.values():
                    if entity.x == x and entity.y == y:
                        symbol = entity.symbol
                        break
                chars.append(symbol)
            rows.append(" ".join(chars))
        return "\n".join(rows)
