from automaton import machines

# Define functions to print on entering and exiting a state
def print_on_enter(new_state, triggered_event):
    print(f"Entered '{new_state}' due to '{triggered_event}'")

def print_on_exit(old_state, triggered_event):
    print(f"Exiting '{old_state}' due to '{triggered_event}'")

# Create the finite machine
m = machines.FiniteMachine()

# Define the states for the linear axis and drill tool
m.add_state('S1_OFF', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S1_ON', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S2_OFF', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S2_ON', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S3_OFF', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S3_ON', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S4_OFF', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('S4_ON', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('DANGER_OFF', on_enter=print_on_enter, on_exit=print_on_exit)
m.add_state('DANGER_ON', on_enter=print_on_enter, on_exit=print_on_exit)

# Define transitions between states based on events
m.add_transition('S1_OFF', 'S2_OFF', 'v = 1')
m.add_transition('S1_OFF', 'S1_ON', 'Drill ON')
m.add_transition('S1_ON', 'S2_ON', 'v = 1')
m.add_transition('S1_ON', 'S1_OFF', 'Drill OFF')

m.add_transition('S2_OFF', 'S3_OFF', 'v = 1')
m.add_transition('S2_OFF', 'S1_OFF', 'v = -1')
m.add_transition('S2_ON', 'S3_ON', 'v = 1')
m.add_transition('S2_ON', 'S2_OFF', 'Drill OFF')

m.add_transition('S3_OFF', 'S4_OFF', 'v = 1')
m.add_transition('S3_OFF', 'S2_OFF', 'v = -1')
m.add_transition('S3_ON', 'S4_ON', 'v = 1')
m.add_transition('S3_ON', 'S3_OFF', 'Drill OFF')

m.add_transition('S4_OFF', 'DANGER_OFF', 'v = 1')
m.add_transition('S4_ON', 'DANGER_ON', 'v = 1')

m.add_transition('DANGER_OFF', 'S4_OFF', 'v = -1')
m.add_transition('DANGER_ON', 'S4_ON', 'v = -1')

# Transition from S1 to DANGER when v = -1
m.add_transition('S1_OFF', 'DANGER_OFF', 'v = -1')
m.add_transition('S1_ON', 'DANGER_ON', 'v = -1')

# Transition from S4 (Drill ON/OFF) to each other
m.add_transition('S4_ON', 'S4_OFF', 'Drill OFF')
m.add_transition('S4_OFF', 'S4_ON', 'Drill ON')

# Set default start state
m.default_start_state = 'S1_OFF'

# Initialize the machine
m.initialize()

# Print the current state after each event
print(m.pformat())

# Define a list of events to trigger transitions
events = ['v = 1', 'Drill ON', 'v = 1', 'Drill OFF', 'v = -1', 'v = 1', 'Drill ON']

# Process each event and show state transitions using `advance`
for event in events:
    print(f"\nProcessing event: {event}")
    print(m.pformat())
    print(f"=============")
    print(f"Current state => {m.current_state}")
    print(f"=============")
