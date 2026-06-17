class DataValidationError(ValueError):
    pass


class DataValidator:
    REQUIRED_CHARACTER_FIELDS = {
        "name": str,
        "symbol": str,
        "position": dict,
        "level": int,
        "role": str,
        "entity_type": str,
        "stats": dict,
    }
    REQUIRED_ITEM_FIELDS = {
        "name": str,
        "slot": str,
        "tags": list,
        "description": str,
    }
    REQUIRED_ANNOUNCEMENT_FIELDS = {"text": str}
    REQUIRED_QUEST_FIELDS = {
        "id": str,
        "title": str,
        "description": str,
        "objectives": list,
    }
    REQUIRED_RECIPE_FIELDS = {
        "id": str,
        "ingredients": list,
        "result": str,
    }
    REQUIRED_OBJECT_FIELDS = {
        "id": str,
        "name": str,
        "symbol": str,
        "position": dict,
        "object_type": str,
        "blocks_movement": bool,
    }
    REQUIRED_HAZARD_FIELDS = {
        "id": str,
        "name": str,
        "symbol": str,
        "position": dict,
        "effect": str,
    }

    def validate_all(self, data):
        self.validate_characters(data["characters"])
        self.validate_items(data["items"])
        self.validate_announcements(data["announcements"])
        self.validate_dialogue(data["dialogue"])
        self.validate_quests(data["quests"])
        self.validate_recipes(data["recipes"], data["items"])
        self.validate_objects(data["objects"])
        self.validate_hazards(data["hazards"])
        self.validate_map(data["map_rows"])

    def validate_characters(self, characters):
        for entity_id, character in characters.items():
            self._require(character, self.REQUIRED_CHARACTER_FIELDS, f"characters.{entity_id}")
            self._require_position(character["position"], f"characters.{entity_id}.position")
            self._require_resource_block(character, f"characters.{entity_id}")

    def validate_items(self, items):
        for item_id, item in items.items():
            self._require(item, self.REQUIRED_ITEM_FIELDS, f"items.{item_id}")

    def validate_announcements(self, announcements):
        for announcement_id, announcement in announcements.items():
            self._require(announcement, self.REQUIRED_ANNOUNCEMENT_FIELDS, f"announcements.{announcement_id}")

    def validate_dialogue(self, dialogue):
        for speaker_id, lines in dialogue.items():
            if not isinstance(lines, list) or not lines:
                raise DataValidationError(f"dialogue.{speaker_id} must be a non-empty list")
            for index, line in enumerate(lines):
                self._require(line, {"text": str}, f"dialogue.{speaker_id}[{index}]")

    def validate_quests(self, quests):
        ids = set()
        for index, quest in enumerate(quests):
            self._require(quest, self.REQUIRED_QUEST_FIELDS, f"quests[{index}]")
            if quest["id"] in ids:
                raise DataValidationError(f"Duplicate quest id: {quest['id']}")
            ids.add(quest["id"])
            for obj_index, objective in enumerate(quest["objectives"]):
                self._require(
                    objective,
                    {"id": str, "description": str, "target": int, "event_type": str},
                    f"quests[{index}].objectives[{obj_index}]",
                )

    def validate_recipes(self, recipes, items):
        for recipe_id, recipe in recipes.items():
            self._require(recipe, self.REQUIRED_RECIPE_FIELDS, f"recipes.{recipe_id}")
            for item_id in recipe["ingredients"] + [recipe["result"]]:
                if item_id not in items:
                    raise DataValidationError(f"recipes.{recipe_id} references unknown item: {item_id}")

    def validate_objects(self, objects):
        for object_id, obj in objects.items():
            self._require(obj, self.REQUIRED_OBJECT_FIELDS, f"objects.{object_id}")
            self._require_position(obj["position"], f"objects.{object_id}.position")

    def validate_hazards(self, hazards):
        for hazard_id, hazard in hazards.items():
            self._require(hazard, self.REQUIRED_HAZARD_FIELDS, f"hazards.{hazard_id}")
            self._require_position(hazard["position"], f"hazards.{hazard_id}.position")

    def validate_map(self, map_rows):
        if not map_rows:
            raise DataValidationError("Map cannot be empty")
        width = len(map_rows[0])
        for index, row in enumerate(map_rows):
            if len(row) != width:
                raise DataValidationError(f"Map row {index} has inconsistent width")

    def _require(self, data, schema, path):
        for field, expected_type in schema.items():
            if field not in data:
                raise DataValidationError(f"{path} missing required field: {field}")
            if not isinstance(data[field], expected_type):
                raise DataValidationError(
                    f"{path}.{field} must be {expected_type.__name__}, got {type(data[field]).__name__}"
                )

    def _require_position(self, position, path):
        self._require(position, {"x": int, "y": int}, path)

    def _require_resource_block(self, character, path):
        resources = character.get("resources")
        if not isinstance(resources, dict):
            raise DataValidationError(f"{path}.resources must be an object")
        self._require(resources, {"health": int, "max_health": int, "stamina": int, "max_stamina": int, "armor": int}, f"{path}.resources")
