from aima3.utils import expr
from aima3.logic import FolKB, fol_fc_ask
from .models import Sign, Problem

# Define the knowledge base
kb = FolKB()


def populate_kb():
    # Iterate over all Sign objects and add each to the knowledge base
    for sign in Sign.objects.all():
        kb.tell(expr(f"Sign('{sign.name}')"))

    # Iterate over all Problem objects and add each to the knowledge base
    for problem in Problem.objects.all():
        kb.tell(expr(f"Problem('{problem.name}')"))

    # Iterate over all Problem objects, retrieve associated signs, and add each problem-sign pair to the knowledge base
    for problem in Problem.objects.all():
        signs = list(problem.signs.all())
        for sign in signs:
            kb.tell(expr(f"HasSign('{problem.name}', '{sign.name}')"))

    # Add a rule to the knowledge base that allows diagnosing a problem based on its signs
    kb.tell(
        expr("forall_p(Problem(p) & forall_s(Sign(s) & HasSign(p, s)), Diagnose(p))")
    )


def diagnose_problem(signs):
    # Define the agenda and memory
    agenda = []
    memory = {}

    # Add patient symptoms to the agenda
    for sign in signs:
        agenda.append(expr(f"Sign('{sign}')"))

    # Run the expert system
    seen = set()  # Keep track of the conditions already processed
    while agenda:
        sign = agenda.pop(0)
        if sign in seen:
            continue  # Skip the condition if it has already been processed
        seen.add(sign)
        if fol_fc_ask(kb, sign):
            memory[sign] = True
        else:
            memory[sign] = False
        print(memory)

    # Calculate scores for each problem based on the number of matching signs
    problem_scores = {}
    for problem in Problem.objects.all():
        matching_signs_count = sum(
            memory.get(expr(f"Sign('{sign.name}')"), False)
            for sign in problem.signs.all()
        )
        problem_scores[problem.name] = matching_signs_count
    print(problem_scores)
    # Identify the problem with the highest score
    result_problem = max(problem_scores, key=problem_scores.get)

    # Return the problem name
    return result_problem


# Call the populate_kb function to populate the knowledge base with the data from the database
populate_kb()
