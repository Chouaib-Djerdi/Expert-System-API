from aima3.logic import FolKB, expr
from .models import Sign, Problem


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
    # Extract sign names from the input dictionary
    print(signs)

    # Initialize a dictionary to hold the scores for each problem
    problem_scores = {}

    # Iterate over all Problem objects
    # for problem in Problem.objects.all():
    # Use the knowledge base to infer whether the problem can be diagnosed based on the signs
    # if all(kb.ask(expr(f"HasSign('{problem.name}', '{sign}')")) for sign in signs):
    # If all signs are associated with the problem, add the problem to the diagnosed problems
    # diagnosed_problems.append(problem.name)
    # Iterate over all Problem objects

    for problem in Problem.objects.all():
        # Calculate the score for each problem based on the number of matching signs
        score = sum(
            1 for sign in signs if kb.ask(expr(f"HasSign('{problem.name}', '{sign}')"))
        )
        # Store the score for each problem in the problem_scores dictionary
        problem_scores[problem] = score

    # Identify the problem with the highest score (returns a Problem object)
    result_problem = max(problem_scores, key=problem_scores.get)

    # Return the string definition of the problem instance with the highest score
    return str(result_problem)


# Call the populate_kb function to populate the knowledge base with the data from the database
populate_kb()
