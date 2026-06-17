class AnnouncementManager:
    def __init__(self, templates):
        self.templates = templates
        self.history = []

    def emit(self, event_id, **values):
        template = self.templates.get(event_id)
        if not template:
            return ""

        text = template["text"].format(**values)
        line = f"SYSTEM: {text}"
        self.history.append(line)
        return line
