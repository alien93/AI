__author__ = 'Anders'
from Module1.aStarProgram import aStarAlgorithm
from Module2.state import State

def aStarGAC(variables, constraints, GAC_init, GAC_domain_filter, GAC_gen_new_states, GAC_rerun, aStarH, paintSol):
    def AStar_generate_successors(currentState):
        mNewStates = GAC_gen_new_states(currentState)
        for state in mNewStates:
            GAC_rerun(state, constraints)
            if state.isError():
                mNewStates.remove(state)

        return mNewStates

    queue = GAC_init(variables, constraints)
    GAC_domain_filter(queue,variables, constraints)
    currentState = State(variables)
    aStarAlgorithm(AStar_generate_successors, aStarH, currentState, paintSol)