import re


def evaluate_fol(statement, facts):
    # Parse predicate name and argument terms: Predicate(arg1, arg2)
    pred_name, args_str = re.findall(r'(\w+)\(([^)]*)\)', statement)[0]
    query_args = [a.strip() for a in args_str.split(',')]

    # Search knowledge base for known facts sharing the same predicate
    for fact in list(facts.keys()):
        fact_pred, fact_args_str = re.findall(r'(\w+)\(([^)]*)\)', fact)[0]
        if fact_pred == pred_name:
            fact_args = [a.strip() for a in fact_args_str.split(',')]

            # Unify variables (lowercase like 'x') with ground constants
            subst = {q: f for q, f in zip(query_args, fact_args) if q.islower()}
            inferred_args = [subst.get(q, q) for q in query_args]
            inferred_fact = f"{pred_name}({', '.join(inferred_args)})"

            if inferred_fact not in facts:
                facts[inferred_fact] = []


# Knowledge base
facts = {
    'Person(John)': [],
    'Person(Mary)': [],
    'Likes(John, IceCream)': [],
    'Likes(Mary, Chocolate)': []
}

statement = 'Likes(x, IceCream)'
evaluate_fol(statement, facts)
print(facts)
