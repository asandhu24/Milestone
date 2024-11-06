
class Reminder:
    def __init__(self, event_id, event_type="general", reminder_type="email", time_before_event="1 hour", frequency="single"):
        self.event_id = event_id
        self.event_type = event_type
        self.reminder_type = reminder_type
        self.time_before_event = time_before_event
        self.frequency = frequency

    def update_reminder(self, event_type=None, reminder_type=None, time_before_event=None, frequency=None):
        if event_type:
            self.event_type = event_type
        if reminder_type:
            self.reminder_type = reminder_type
        if time_before_event:
            self.time_before_event = time_before_event
        if frequency:
            self.frequency = frequency

    def __str__(self):
        return (f"Event ID: {self.event_id}\n"
                f"Event Type: {self.event_type}\n"
                f"Reminder Type: {self.reminder_type}\n"
                f"Time Before Event: {self.time_before_event}\n"
                f"Frequency: {self.frequency}\n")