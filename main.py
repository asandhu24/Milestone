from event_service import EventService

def main():
    event_service = EventService()
    while True:
        print("\n--- Event Reminder Customization ---")
        print("This feature allows you to set, view, and customize reminders for your events.")
        print("You can choose reminder type, timing, and frequency to help you stay organized.\n")
        
        print("1. Add Reminder")
        print("2. View Reminder")
        print("3. Update Reminder")
        print("4. Help (View Benefits & Costs)")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            print("Adding a reminder helps ensure you’re notified before an event. Let’s set one up!")
            event_id = input("Enter Event ID: ")
            event_type = input("Enter Event Type (e.g., meeting, appointment, birthday): ")
            reminder_type = input("Enter Reminder Type (email/sms/app): ")
            time_before_event = input("Enter Time Before Event (e.g., '1 hour', '1 day'): ")
            frequency = input("Enter Frequency (single/daily/weekly): ")
            reminder = event_service.add_reminder(event_id, event_type, reminder_type, time_before_event, frequency)
            print("Reminder Added:\n", reminder)

        elif choice == "2":
            event_id = input("Enter Event ID to view: ")
            reminder = event_service.get_reminder(event_id)
            if reminder:
                print("Reminder Details:\n", reminder)
            else:
                print("No reminder found for this Event ID.")

        elif choice == "3":
            event_id = input("Enter Event ID to update: ")
            reminder = event_service.get_reminder(event_id)
            if reminder:
                print("Updating a reminder allows you to refine your notifications.")
                event_type = input("Enter new Event Type (or leave blank to keep current): ")
                reminder_type = input("Enter new Reminder Type (or leave blank to keep current): ")
                time_before_event = input("Enter new Time Before Event (or leave blank): ")
                frequency = input("Enter new Frequency (or leave blank): ")

                # Confirm changes before applying
                confirm = input("Do you want to save these changes? (yes/no): ")
                if confirm.lower() == "yes":
                    updated_reminder = event_service.update_reminder(
                        event_id,
                        event_type=event_type or None,
                        reminder_type=reminder_type or None,
                        time_before_event=time_before_event or None,
                        frequency=frequency or None
                    )
                    print("Updated Reminder:\n", updated_reminder)
                else:
                    print("Changes discarded.")
            else:
                print("No reminder found for this Event ID.")

        elif choice == "4":
            print("\n--- Benefits and Costs of Using Event Reminders ---")
            print("Benefits: Reminders help you stay organized and ensure you don’t miss important events.")
            print("Costs: Not setting a reminder could mean missing out on notifications.")
            print("You can choose the reminder type, timing, and frequency to fit your preferences.\n")

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()