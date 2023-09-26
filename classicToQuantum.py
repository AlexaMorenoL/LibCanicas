import numpy as np
import matplotlib.pyplot as plot

def marbles(probability_matrix, inicial_state):
    result = np.dot(probability_matrix, inicial_state)
    return result

def classic_slit(transition_matrix, inicial_state, clicks):
    actual_state = inicial_state
    for _ in range(clicks):
        actual_state = np.dot(transition_matrix, actual_state)
    return actual_state

def quantum_slit(transition_matrix, inicial_state):
    result = np.dot(transition_matrix, inicial_state)
    return result

def graphical_propabilities(state_vector, states_names, tittle, file_name):
    plot.bar(range(len(state_vector)), state_vector)
    plot.xticks(range(len(state_vector)), states_names)
    plot.xlabel('Estados')
    plot.ylabel('Probabilidad')
    plot.title(tittle)
    plot.savefig(file_name)
    plot.show()

if __name__ == '__main__':
    unittest.main()
