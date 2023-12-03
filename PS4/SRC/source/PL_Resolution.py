from itertools import combinations

from source.Clause import Clause

def is_child_of(setA, setB):
    child = setA.difference(setB)
    if not (child):
        return True
    return False

def PL_Resolution(kb, alpha):
    result = False
    clauses = set(kb.KB)

    if len(alpha.literal_list) > 1:  # alpha is a disjunction
        for literal in alpha.literal_list:
            negated_literal = literal.clone()
            negated_literal.negate()
            negated_clause = Clause()
            negated_clause.add_literal(negated_literal)
            clauses.add(negated_clause)
    else:
        # If alpha is not a disjunction, negate it and add to clauses
        alpha.negate()
        clauses.add(alpha)

    step_clauses = []
    while (True):
        new = set()
        for (ci, cj) in combinations(sorted(clauses), 2):
            resolvents, is_empty = Clause.PLResolve(ci, cj)
            new.update(resolvents)
            result |= is_empty

        is_child = is_child_of(new, clauses)
        different_clause = sorted(new.difference(clauses))
        step_clauses.append(different_clause)

        clauses.update(new)
        if is_child:
            return step_clauses, False
        elif result:
            return step_clauses, True
