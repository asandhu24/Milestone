
from reminder import Reminder

class EventService:
    def __init__(self):
        self.reminders = {}

    def add_reminder(self, event_id, event_type="general", reminder_type="email", time_before_event="1 hour", frequency="single"):
        reminder = Reminder(event_id, event_type, reminder_type, time_before_event, frequency)
        self.reminders[event_id] = reminder
        return reminder

    def get_reminder(self, event_id):
        return self.reminders.get(event_id)

    def update_reminder(self, event_id, **kwargs):
        reminder = self.reminders.get(event_id)
        if reminder:
            reminder.update_reminder(**kwargs)
            return reminder
        return None
