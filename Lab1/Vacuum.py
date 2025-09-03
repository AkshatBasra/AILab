import random
def reflex_agent(state):
    location, statusA, statusB = state

    if location == 'A':
        if statusA == 'Dirty':
            return 'Clean'
        else:
            return 'Right'
    elif location == 'B':
        if statusB == 'Dirty':
            return 'Clean'
        else:
            return 'Left'
def vacuum_environment():
    state = random.choice([
        ('A', 'Dirty', 'Dirty'),
        ('A', 'Dirty', 'Clean'),
        ('A', 'Clean', 'Dirty'),
        ('A', 'Clean', 'Clean'),
        ('B', 'Dirty', 'Dirty'),
        ('B', 'Dirty', 'Clean'),
        ('B', 'Clean', 'Dirty'),
        ('B', 'Clean', 'Clean')
    ])
    print("Initial state:", state)
    for step in range(10):
        location, statusA, statusB = state
        action = reflex_agent(state)
        print(f"Step {step+1}: Location={location}, Action={action}")
        if action == 'Clean':
            if location == 'A':
                state = (location, 'Clean', statusB)
            else:
                state = (location, statusA, 'Clean')
        elif action == 'Right':
            state = ('B', statusA, statusB)
        elif action == 'Left':
            state = ('A', statusA, statusB)

        print("New state:", state)
vacuum_environment()