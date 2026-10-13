# Define the rules
rules = [
    {'name': 'Rule 1', 'conditions': ['A'], 'conclusion': 'B'},
    {'name': 'Rule 2', 'conditions': ['B'], 'conclusion': 'C'},
    {'name': 'Rule 3', 'conditions': ['C'], 'conclusion': 'D'},
    {'name': 'Rule 4', 'conditions': ['E', 'F'], 'conclusion': 'A'}
]

# Initial facts
facts = ['E', 'F']


def forward_chaining(rules, facts):
    facts_set = set(facts)

    while True:
        new_fact_added = False
        for rule in rules:
            # Check if all conditions are satisfied and conclusion is new
            if set(rule['conditions']).issubset(facts_set) and rule['conclusion'] not in facts_set:
                facts_set.add(rule['conclusion'])
                print(f"Applied rule: {rule['name']}")
                print(f"Facts: {sorted(list(facts_set))}")
                new_fact_added = True

        # Stop when no new facts can be deduced
        if not new_fact_added:
            break


# Run forward chaining inference engine
forward_chaining(rules, facts)
