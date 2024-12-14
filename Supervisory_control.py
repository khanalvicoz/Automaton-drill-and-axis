class SupervisorControl:
    def __init__(self):
        # Initial state setup
        self.state = 'S1_OFF'
        self.linear_axis_position = 50  # Initial position in mm
        self.drill_state = 'OFF'  # Drill is initially off

    def transition(self, event):
        """Transition logic based on the event and current state."""
        print(f"Current state: {self.state}")

        if self.state == 'S1_OFF':
            if event == 'Drill ON' and self.linear_axis_position >= 100:
                print(f"Event recognized: {event}")
                self.drill_state = 'ON'
                print("Drill is now ON.")
                self.state = 'S1_ON'  # Change state to S1_ON after turning the drill on
            elif event == 'Drill ON':
                print(f"Warning: Cannot turn on drill in {self.state} state (linear axis is below 100mm).")
            else:
                print("No valid event or event rejected by supervisor.")
        elif self.state == 'S1_ON':
            if event == 'Drill OFF':
                print(f"Event recognized: {event}")
                self.drill_state = 'OFF'
                print("Drill is now OFF.")
                self.state = 'S1_OFF'  # Change state back to S1_OFF after turning the drill off
            else:
                print("No valid event or event rejected by supervisor.")
        else:
            print(f"Unrecognized state: {self.state}")

    def update_position(self, position):
        """Update the linear axis position."""
        self.linear_axis_position = position
        print(f"Linear axis position updated to {self.linear_axis_position}mm")

    def display_state(self):
        """Display the current state."""
        print(
            f"Current state: {self.state}, Linear axis position: {self.linear_axis_position}mm, Drill state: {self.drill_state}")


# Example usage:
supervisor = SupervisorControl()

# Display initial state
supervisor.display_state()

# Interactive loop
while True:
    print("\nOptions: ")
    print("1: Update position")
    print("2: Turn drill ON")
    print("3: Turn drill OFF")
    print("4: Display state")
    print("5: Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        new_position = float(input("Enter new position for linear axis (mm): "))
        supervisor.update_position(new_position)
    elif choice == '2':
        supervisor.transition('Drill ON')
    elif choice == '3':
        supervisor.transition('Drill OFF')
    elif choice == '4':
        supervisor.display_state()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
