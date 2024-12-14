from graphviz import Digraph

# Create a new directed graph
dot = Digraph(format='png')

# Define states for the linear axis and drill tool (using acronyms)
states = [
    "S1_OFF", "S1_ON",  # S1 + Drill OFF, S1 + Drill ON
    "S2_OFF", "S2_ON",  # S2 + Drill OFF, S2 + Drill ON
    "S3_OFF", "S3_ON",  # S3 + Drill OFF, S3 + Drill ON
    "S4_OFF", "S4_ON",  # S4 + Drill OFF, S4 + Drill ON
    "DANGER_OFF", "DANGER_ON"  # Danger + Drill OFF, Danger + Drill ON
]

# Add states to the graph
for state in states:
    dot.node(state)

# Define transitions (current state -> input -> next state)
transitions = [
    # From S1 to S2
    ("S1_OFF", "v = 1", "S2_OFF"),
    ("S1_OFF", "Drill ON", "S1_ON"),
    ("S1_ON", "v = 1", "S2_ON"),
    ("S1_ON", "Drill OFF", "S1_OFF"),

    # From S2 to S3
    ("S2_OFF", "v = 1", "S3_OFF"),
    ("S2_OFF", "v = -1", "S1_OFF"),
    ("S2_ON", "v = 1", "S3_ON"),
    ("S2_ON", "Drill OFF", "S2_OFF"),

    # From S3 to S4
    ("S3_OFF", "v = 1", "S4_OFF"),
    ("S3_OFF", "v = -1", "S2_OFF"),
    ("S3_ON", "v = 1", "S4_ON"),
    ("S3_ON", "Drill OFF", "S3_OFF"),

    # From S4 to Danger
    ("S4_OFF", "v = 1", "DANGER_OFF"),
    ("S4_ON", "v = 1", "DANGER_ON"),

    # From Danger to S4
    ("DANGER_OFF", "v = -1", "S4_OFF"),
    ("DANGER_ON", "v = -1", "S4_ON"),

    # Adding transition from S1 to Danger when velocity is -1
    ("S1_OFF", "v = -1", "DANGER_OFF"),
    ("S1_ON", "v = -1", "DANGER_ON"),

    # Adding transition from S4 (Drill ON/OFF) to each other
    ("S4_ON", "Drill OFF", "S4_OFF"),
    ("S4_OFF", "Drill ON", "S4_ON")
]

# Add transitions (edges) to the graph
for transition in transitions:
    dot.edge(transition[0], transition[2], label=transition[1])

# Render the graph to a PNG image
dot.render('linear_axis_drill_tool_state_diagram')

# Display the image path
print("State diagram generated and saved as 'linear_axis_drill_tool_state_diagram.png'")
