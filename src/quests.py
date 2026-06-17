class QuestLog:
    def __init__(self, quest_data):
        self.quests = {
            quest["id"]: {
                **quest,
                "completed": False,
                "objectives": [
                    {
                        **objective,
                        "current": 0,
                        "completed": False,
                    }
                    for objective in quest.get("objectives", [])
                ],
            }
            for quest in quest_data
        }

    def complete(self, quest_id):
        quest = self.quests.get(quest_id)
        if not quest or quest["completed"]:
            return ""
        quest["completed"] = True
        for objective in quest["objectives"]:
            objective["completed"] = True
            objective["current"] = objective["target"]
        return f"Quest complete: {quest['title']}"

    def record_event(self, event_type, amount=1):
        completed = []
        for quest_id, quest in self.quests.items():
            if quest["completed"]:
                continue
            for objective in quest["objectives"]:
                if objective["completed"] or objective["event_type"] != event_type:
                    continue
                objective["current"] = min(objective["target"], objective["current"] + amount)
                if objective["current"] >= objective["target"]:
                    objective["completed"] = True
            if quest["objectives"] and all(objective["completed"] for objective in quest["objectives"]):
                quest["completed"] = True
                completed.append(f"Quest complete: {quest['title']}")
        return completed

    def active_lines(self):
        lines = []
        for quest in self.quests.values():
            marker = "done" if quest["completed"] else "open"
            objective_text = ", ".join(
                f"{objective['current']}/{objective['target']}" for objective in quest["objectives"]
            )
            suffix = f" ({objective_text})" if objective_text else ""
            lines.append(f"[{marker}] {quest['title']} - {quest['description']}{suffix}")
        return lines
