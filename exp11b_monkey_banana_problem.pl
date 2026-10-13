% Exp No: 11 (b) - Prolog Program for Monkey Banana Problem

% Spatial & entity facts
on(floor, monkey).
on(floor, chair).
in(room, monkey).
in(room, chair).
in(room, banana).
at(ceiling, banana).

% Capability facts
strong(monkey).
grasp(monkey).
climb(monkey, chair).

% Action rules (Horn clauses)
push(monkey, chair) :- 
    strong(monkey).

under(banana, chair) :- 
    push(monkey, chair).

canreach(banana, monkey) :-
    at(floor, banana);
    (at(ceiling, banana), under(banana, chair), climb(monkey, chair)).

canget(banana, monkey) :-
    canreach(banana, monkey), 
    grasp(monkey).
