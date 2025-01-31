class Dfa:
    allStates = {}
    alphabet = {}
    transitionFunction = {}
    startState = ''
    acceptStates = {}

    def __init__(self, allStates, alphabet, transitionFunction, startState, acceptStates):
        self.allStates = allStates
        self.alphabet = alphabet
        self.transitionFunction = transitionFunction
        self.startState = startState
        self.acceptStates = acceptStates

    def recognize(self, w_):
        currentState = self.startState
        for character in w_:
            currentState = self.transitionFunction.get(currentState).get(character)
        if currentState in self.acceptStates:
            return True
        else:
            return False


def run_tests(M_, tests_):
    """Do not modify this function. This runs tests
    for a given DFA instance. We're not using Python's
    unittest framework because this isn't a course on
    software engineering and because we wish to avoid
    complexity of parameterization of tests. """
    for w, expected in tests_:
        actual = M_.recognize(w)
        print(f"Reported: {actual}. "
              f"{'Correct!' if actual == expected else 'Incorrect!'} "
              f"'{w}' is {'' if expected else 'not '}in the language of M.")


if __name__ == "__main__":
    Q = {'A', 'B'}
    Sigma = {'0', '1'}
    delta = {'A': {'0': 'B',
                   '1': 'A'},
             'B': {'0': 'A',
                   '1': 'B'}}
    q_0 = 'A'
    F = {'A'}
    # instantiate the DFA
    M_1 = Dfa(Q, Sigma, delta, q_0, F)
    tests = [('', True),  # Remember: 0 is even!
             ('0', False),
             ('00', True),
             ('100', True),
             ('101', False),
             ('01010101', True),
             ('010101010', False)]
    print()
    print("L_1 = {w | w contains an even number of 0s}")
    run_tests(M_1, tests)

    Q = {'A', 'B', 'C', 'D'}
    Sigma = {'0', '1'}
    delta = {'A': {'0': 'A',
                   '1': 'B'},
             'B': {'0': 'C',
                   '1': 'A'},
             'C': {'0': 'A',
                   '1': 'D'},
             'D': {'0': 'D',
                   '1': 'D'}}
    q_0 = 'A'
    F = {'D'}
    # instantiate the DFA
    M_2 = Dfa(Q, Sigma, delta, q_0, F)
    tests = [('', False),
             ('0', False),
             ('00', False),
             ('100', False),
             ('101', True),
             ('01010101', True),
             ('000101000', True),
             ('1000101', True),
             ('1001001', False)]
    print()
    print("L_2 = {w | w contains 101 as substring}")
    run_tests(M_2, tests)

    Q = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    Sigma = {'0', '1'}
    delta = {'A': {'0': 'B',
                   '1': 'C'},
             'B': {'0': 'D',
                   '1': 'E'},
             'C': {'0': 'G',
                   '1': 'F'},
             'D': {'0': 'D',
                   '1': 'E'},
             'E': {'0': 'D',
                   '1': 'E'},
             'F': {'0': 'G',
                   '1': 'F'},
             'G': {'0': 'G',
                   '1': 'F'}}
    q_0 = 'A'
    F = {'E', 'G'}
    M_3 = Dfa(Q, Sigma, delta, q_0, F)
    tests = [('', False),
             ('0', False),
             ('00', False),
             ('100', True),
             ('101', False),
             ('01010101', True),
             ('10', True),
             ('1000101', False),
             ('0001001', True),
             ('1', False),
             ('11', False)]
    print()
    print("L_3 = {w | w begins and ends with a different symbol}")
    run_tests(M_3, tests)

    Q = {'A', 'B', 'C', 'D', 'E', 'F'}
    Sigma = {'0', '1'}
    delta = {'A': {'0': 'B',
                   '1': 'C'},
             'B': {'0': 'D',
                   '1': 'E'},
             'C': {'0': 'D',
                   '1': 'E'},
             'D': {'0': 'F',
                   '1': 'F'},
             'E': {'0': 'F',
                   '1': 'F'},
             'F': {'0': 'B',
                   '1': 'C'}}
    q_0 = 'A'
    F = {'B', 'D', 'F'}
    M_4 = Dfa(Q, Sigma, delta, q_0, F)
    tests = [('', True),  # 0 is a multiple of three
             ('0', True),
             ('00', True),
             ('000', True),
             ('0000', True),
             ('00000', True),
             ('000000', True),
             ('1', False),
             ('11', False),
             ('111', True),
             ('1111', False),
             ('11111', False),
             ('111111', True),
             ('1000', True),
             ('0111', False),
             ('01010', True),
             ('10101', False),
             ('10', True),
             ('01', False),
             ('1101', False)]
    print()
    print("L_4 = {w | w ends in 0 or the length of w is a multiple of three}")
