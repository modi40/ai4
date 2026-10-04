def forall(domain, predicate):
    return all(predicate(x) for x in domain)

def exists(domain, predicate):
    return any(predicate(x) for x in domain)

def implies(p, q):
    return (not p) or q

def main():
    entities = ['Socrates', 'Plato', 'Aristotle', 'Newton']
    mixed_domain = ['Socrates', 'Dog', 'Cat', 'Robot']
    
    def is_human(x):
        return x in ['Socrates', 'Plato', 'Aristotle', 'Newton']
        
    def is_mortal(x):
        return x in ['Socrates', 'Plato', 'Aristotle', 'Newton', 'Dog', 'Cat']
        
    def rule_human_mortal(x):
        return implies(is_human(x), is_mortal(x))

    print("Predicate Logic Implementation")
    print("Entities Domain:", entities)
    print("Mixed Domain:", mixed_domain)
    
    statement1 = forall(entities, is_human)
    print("Statement 1: Forall x in entities, is_human(x):", statement1)
    
    statement2 = forall(mixed_domain, is_human)
    print("Statement 2: Forall x in mixed_domain, is_human(x):", statement2)
    
    statement3 = exists(mixed_domain, is_human)
    print("Statement 3: Exists x in mixed_domain, is_human(x):", statement3)
    
    statement4 = forall(mixed_domain, rule_human_mortal)
    print("Statement 4: Forall x in mixed_domain, is_human(x) -> is_mortal(x):", statement4)
    
    numbers = [2, 4, 6, 8, 10]
    
    def is_even(n):
        return n % 2 == 0
        
    def is_greater_than_five(n):
        return n > 5

    print("Numerical Domain:", numbers)
    print("Forall n, is_even(n):", forall(numbers, is_even))
    print("Exists n, is_greater_than_five(n):", exists(numbers, is_greater_than_five))

if __name__ == '__main__':
    main()
