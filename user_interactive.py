import time
from automaton import machines
import keyboard


# Function to display the current state
def print_state(old_state, triggered_event):
    print(f"State changed: {old_state} -> {m.current_state} due to event '{triggered_event}'")


# Create the finite machine with states and transitionsoodd
m = machines.FiniteMachine()

# States for the linear axis and drill tool (using acronyms)
m.add_state('S1_OFF', on_enter=print_state, on_exit=print_state)
m.add_state('S1_ON', on_enter=print_state, on_exit=print_state)
m.add_state('S2_OFF', on_enter=print_state, on_exit=print_state)
m.add_state('S2_ON', on_enter=print_state, on_exit=print_state)
m.add_state('S3_OFF', on_enter=print_state, on_exit=print_state)
m.add_state('S3_ON', on_enter=print_state, on_exit=print_state)
m.add_state('S4_OFF', on_enter=print_state, on_exit=print_state)
m.add_state('S4_ON', on_enter=print_state, on_exit=print_state)
m.add_state('DANGER_OFF', on_enter=print_state, on_exit=print_state)
m.add_state('DANGER_ON', on_enter=print_state, on_exit=print_state)

# Transitions (event -> from state -> to state)
m.add_transition('S1_OFF', 'S2_OFF', '↓')  # linear axis down
m.add_transition('S2_OFF', 'S3_OFF', '↓')  # linear axis down
m.add_transition('S3_OFF', 'S4_OFF', '↓')  # linear axis down
m.add_transition('S4_OFF', 'DANGER_OFF', '↓')  # linear axis down

m.add_transition('S1_ON', 'S2_ON', '↓')  # linear axis down
m.add_transition('S2_ON', 'S3_ON', '↓')  # linear axis down
m.add_transition('S3_ON', 'S4_ON', '↓')  # linear axis down
m.add_transition('S4_ON', 'DANGER_ON', '↓')  # linear axis down

# For moving UP (↑), reverse the order
m.add_transition('S2_OFF', 'S1_OFF', '↑')  # linear axis up
m.add_transition('S3_OFF', 'S2_OFF', '↑')  # linear axis up
m.add_transition('S4_OFF', 'S3_OFF', '↑')  # linear axis up
m.add_transition('DANGER_OFF', 'S4_OFF', '↑')  # linear axis up

m.add_transition('S2_ON', 'S1_ON', '↑')  # linear axis up
m.add_transition('S3_ON', 'S2_ON', '↑')  # linear axis up
m.add_transition('S4_ON', 'S3_ON', '↑')  # linear axis up
m.add_transition('DANGER_ON', 'S4_ON', '↑')  # linear axis up

# Drill transitions
m.add_transition('S1_OFF', 'S1_ON', 'D')  # drill on
m.add_transition('S1_ON', 'S1_OFF', 'O')  # drill off
m.add_transition('S2_OFF', 'S2_ON', 'D')  # drill on
m.add_transition('S2_ON', 'S2_OFF', 'O')  # drill off
m.add_transition('S3_OFF', 'S3_ON', 'D')  # drill on
m.add_transition('S3_ON', 'S3_OFF', 'O')  # drill off
m.add_transition('S4_OFF', 'S4_ON', 'D')  # drill on
m.add_transition('S4_ON', 'S4_OFF', 'O')  # drill off
m.add_transition('DANGER_OFF', 'DANGER_ON', 'D')  # drill on
m.add_transition('DANGER_ON', 'DANGER_OFF', 'O')  # drill off

# Set the initial state
m.default_start_state = 'S1_OFF'
m.initialize()

# Display the initial state
print("Initial State: S1_OFF")

# Loop to wait for user input
while True:
    event = None

    # Capture key presses for the required eventsd
    if keyboard.is_pressed('down'):  # Linear axis down (↓)
        event = '↑'
    elif keyboard.is_pressed('up'):  # Linear axis up (↑)
        event = '↓'
    elif keyboard.is_pressed('D'):  # Drill on
        event = 'D'
    elif keyboard.is_pressed('O'):  # Drill off
        event = 'O'

    if event:
        print(f"Event triggered: {event}")
        m.process_event(event)
        time.sleep(.2)# Prevent multiple triggers for a single press

    # Print current state after each event
    print("Current state:", m.current_state)
    time.sleep(0.5)  # Wait a bit before checking again
