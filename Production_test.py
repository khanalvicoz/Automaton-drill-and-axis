from graphviz import Digraph

# Create a new directed graph
dot = Digraph(format='png')

# Define states for Production lines P1, P2 and Robot, R
states = [
    "E.E.E",  #Initial
    "P.E.E",  #Charge1
    "E.E.1",  # Discharge 1
    "E.P.E",  # Charge 2
    "P.E.1", #Charge 1
    "E.E.2",  #Discharge 2
    "P.P.E",  #Charge 1 and Charge 2
    "P.E.2", #Discharge 2
    "E.P.1",  #Discharge 1
    "P.P.1", # Charge 1
    "E.P.2", "P.P.2" #cannont be reached
]

# Add states to the graph
for state in states:
    dot.node(state)

# Define transitions (current state -> input -> next state)
transitions = [

    ("E.E.E", "charge 1", "P.E.E"),
    ("P.E.E", "discharge 1", "E.E.1"),
    ("E.E.1", "charge 2", "E.P.E"),
    ("E.E.1", "charge 1", "P.E.1"),
    ("P.E.1", "charge 2", "P.P.E"),
    ("E.P.E", "charge 1", "P.P.E"),
    ("E.P.E", "discharge 2", "E.E.2"),
    ("P.P.E", "discharge 2", "P.E.2"),
    ("E.E.2", "charge 1", "P.E.2"),
    ("P.P.E", "discharge 1", "E.P.1"),
    ("E.P.1", "charge 1", "P.P.1"),
    ("P.E.2", "store", "P.E.E"),
    ("E.E.2", "store", "E.E.E"),

]
# Add transitions (edges) to the graph
for transition in transitions:
    dot.edge(transition[0], transition[2], label=transition[1])

# Render the graph to a PNG image
dot.render('Production_test_state_diagram')

# Display the image path
print("State diagram generated and saved as 'Production_test_state_diagram.png'")
