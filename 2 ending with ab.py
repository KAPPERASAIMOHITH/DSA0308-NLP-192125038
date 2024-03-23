def match_pattern(input_string):
    
    transitions = {'q0': {'a': 'q1', 'b': 'q0'}, 'q1': {'a': 'q1', 'b': 'q2'}, 'q2': {'a': 'q1', 'b': 'q0'}}
    state = 'q0'
    
    
    for char in input_string:
        
        state = transitions.get(state, {}).get(char, 'q0')
    
    
    return state == 'q0'


test_strings = ['ab', 'aab', 'abb', 'aabb', 'abab', 'b', 'aba']


for test_string in test_strings:
    if match_pattern(test_string):
        print(f"'{test_string}' is not accepted.")
    else:
        print(f"'{test_string}' is accepted.")
