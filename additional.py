import keyboard  # To handle keyboard input for velocity control
from graphviz import Digraph


class SupervisorControl:
    def __init__(self):
        # Initial state setup
        self.state = 'S1_OFF'
        self.linear_axis_position = 50  # Initial position in mm
        self.drill_state = 'OFF'  # Drill is initially off
        self.velocity = 1  # Default slow velocity in mm/s (1 mm/s)
        self.state_transitions = []

    def transition(self, event):
        """Transition logic based on the event and current state."""
        print(f"Current state: {self.state}")

        if self.state == 'S1_OFF':
            if event == 'Drill ON' and self.linear_axis_position >= 100:
                print(f"Event recognized: {event}")
                self.drill_state = 'ON'
                print("Drill is now ON.")
                self.state = 'S1_ON'  # Change state to S1_ON after turning the drill on
                self.state_transitions.append(('S1_OFF', 'Drill ON', 'S1_ON'))
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
                self.state_transitions.append(('S1_ON', 'Drill OFF', 'S1_OFF'))
            else:
                print("No valid event or event rejected by supervisor.")
        else:
            print(f"Unrecognized state: {self.state}")

    def update_position(self, direction):
        """Update the linear axis position based on the velocity and direction."""
        if direction == 'up':
            self.linear_axis_position += self.velocity
        elif direction == 'down':
            self.linear_axis_position -= self.velocity

        # Ensure the position stays within bounds
        if self.linear_axis_position < 50:
            self.linear_axis_position = 50
        elif self.linear_axis_position > 550:
            self.linear_axis_position = 550

        print(f"Linear axis position updated to {self.linear_axis_position}mm")

    def display_state(self):
        """Display the current state."""
        print(
            f"Current state: {self.state}, Linear axis position: {self.linear_axis_position}mm, Drill state: {self.drill_state}")

    def generate_state_diagram(self):
        """Generate a state diagram based on the state transitions."""
        dot = Digraph(comment='Supervisor Control State Diagram')

        # Add states
        dot.node('S1_OFF', 'S1_OFF')
        dot.node('S1_ON', 'S1_ON')

        # Add transitions based on the state transitions history
        for transition in self.state_transitions:
            dot.edge(transition[0], transition[2], label=transition[1])

        # Render the state diagram to a file
        dot.render('state_diagram', format='png', cleanup=True)
        print("State diagram has been generated and saved as 'state_diagram.png'.")

    def handle_key_input(self):
        """Handle key presses for controlling the linear axis movement and state transitions."""
        while True:
            if keyboard.is_pressed('down'):  # Fast down movement (↓ key mapped as 'down')
                print("Fast down movement triggered.")
                self.update_position('down')
            elif keyboard.is_pressed('up'):  # Fast up movement (↑ key mapped as 'up')
                print("Fast up movement triggered.")
                self.update_position('up')
            elif keyboard.is_pressed('s'):  # Slow down movement (S key mapped as 's')
                print("Slow down movement triggered.")
                self.update_position('down')
            elif keyboard.is_pressed('w'):  # Slow up movement (W key mapped as 'w')
                print("Slow up movement triggered.")
                self.update_position('up')
            elif keyboard.is_pressed('q'):  # Quit the program
                print("Exiting program...")
                break

    def set_velocity(self, velocity):
        """Set the current velocity (1 mm/s for slow, 5 mm/s for fast)."""
        self.velocity = velocity


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
    print("5: Generate State Diagram")
    print("6: Set to Slow Velocity")
    print("7: Set to Fast Velocity")
    print("8: Exit")

    choice = input("Enter choice (1-8): ")

    if choice == '1':
        new_position = float(input("Enter new position for linear axis (mm): "))
        supervisor.linear_axis_position = new_position
        supervisor.display_state()
    elif choice == '2':
        supervisor.transition('Drill ON')
    elif choice == '3':
        supervisor.transition('Drill OFF')
    elif choice == '4':
        supervisor.display_state()
    elif choice == '5':
        supervisor.generate_state_diagram()
    elif choice == '6':
        supervisor.set_velocity(1)  # Set to slow velocity (1 mm/s)
        print("Velocity set to slow (1 mm/s).")
    elif choice == '7':
        supervisor.set_velocity(5)  # Set to fast velocity (5 mm/s)
        print("Velocity set to fast (5 mm/s).")
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select a valid option.")

    # Check for key inputs for controlling axis movement
    supervisor.handle_key_input()
