import unittest
import numpy as np
from classicToQuantum import marbles, classic_slit, quantum_slit, graphical_propabilities

class TestExperiments(unittest.TestCase):

    def test_marbles(self):
        probability_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        inicial_state = np.array([1, 0, 0])
        result = marbles(probability_matrix, inicial_state)
        expected_result = np.array([0, 1, 0])
        np.testing.assert_array_equal(result, expected_result)

    def test_classic_slit(self):
        transition_matrix = np.array([[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5]])
        inicial_state = np.array([1, 0, 0])
        clicks = 3
        result = classic_slit(transition_matrix, inicial_state, clicks)
        excepted_result = np.array([0.4375, 0.375, 0.1875])
        np.testing.assert_allclose(result, excepted_result)

    def test_quantum_slit(self):
        transition_matrix = np.array([[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5]])
        inicial_state = np.array([1, 0, 0])
        result = quantum_slit(transition_matrix, inicial_state)
        excepted_result = np.array([0.5, 0.25, 0.25])
        np.testing.assert_allclose(result, excepted_result)

    def test_graphical_probabilities(self):
        state_vector = np.array([0.5, 0.25, 0.25])
        states_names = ['Estado 1', 'Estado 2', 'Estado 3']
        tittle = 'Gráficos'
        file_name = 'graficos.png'
        try:
            graphical_propabilities(state_vector, states_names, tittle, file_name)
        except Exception as e:
            self.fail(f"La función de gráficos generó un error: {e}")

if __name__ == '__main__':
    unittest.main()
