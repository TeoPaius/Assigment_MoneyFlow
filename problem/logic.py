from preproc import skills_to_nr
from preproc import has_skills
import math

def my_operator(a, b):
    if a == 1 and b == 0:
        return 1
    return 0

def check_redundancy(sol, target_hash):
    """
    This redundancy check works arround the ideea that if there is at least one target skill unique for each participant
    in a possible solution then there doesn't exist redundacies

    To achieve this i have designed an n^2 algorithm combining the skills for each participant leaving one of the out and then
    xor-ing the result with the skills of the one left out, if the resulted number doesnt have any bit set, then it means that person is redundant
    :param sol:
    :param target_hash:
    :return: boolean
    """
    combination = 0
    for i in range(0, len(sol)):
        combination = 0
        for j in range(0, len(sol)):
            if j == i:
                continue
            combination |= (sol[j][1] & target_hash)
        code = sol[i][1] & target_hash
        mask = code ^ combination
        if mask & code == 0:
            return True

    return False




def group(employes, idx,target_hash, partial_hash, partial_sol):
    """
    This is a simple backtracking backbone, checking each possible combination of workers

    :param employes: list of employes
    :param idx: parameter for backtracking
    :param target_hash: target skills hash number
    :param partial_hash: the hash number of skills from a certain combination of workers
    :param partial_sol: possible solution of workers
    :return: generator for each correct combination of workers
    """
    if partial_hash & target_hash == target_hash:
        #this checks if we got all the needed skills
        #print([i[0] for i in partial_sol])
        if not check_redundancy(partial_sol,target_hash):
            yield [i[0][0] for i in partial_sol]
        return []

    #stop condition
    if idx > len(employes):
        return []

    for i in range(idx, len(employes)):
        code = employes[i][1] & target_hash # we are interested just in the target skills from the workers so we isolate those bits
        if has_skills(code, target_hash): # if the worker doesent have any of the target skills we skip him

            #else we add it to the solution, update the partial hash and continue

            partial_sol.append(employes[i])
            tmp = partial_hash
            partial_hash |= code
            for i in group(employes,i+1,target_hash,partial_hash,partial_sol):
                yield i
            partial_hash = tmp
            partial_sol.pop(len(partial_sol)-1)