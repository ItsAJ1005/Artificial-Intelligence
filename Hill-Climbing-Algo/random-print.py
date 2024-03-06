import random
import string

target = input("Enter the string you wish to generate using Hill Climbing Algorithm: ")     # setting goal state
len_of_target = len(target)

def generate_random_sol(length=len_of_target):
    return [random.choice(string.printable) for _ in range(length)]                         #initial state 

def evaluate(solution, target):
    diff = sum(abs(ord(s) - ord(t)) for s, t in zip(solution, target))                      #Evaluation function
    return diff

def mutate_solution(solution):
    index = random.randint(0, len(solution) - 1)                                            
    solution[index] = random.choice(string.printable)

best = generate_random_sol()
best_score = evaluate(best, target)

iteration_limit = 1000000
iteration_count = 0

while best_score > 0 and iteration_count < iteration_limit:
    print('Best solution so far:', best_score, 'Solution:', "".join(best))

    new_solution = list(best)
    mutate_solution(new_solution)

    score = evaluate(new_solution, target)

    if score < best_score:
        best = new_solution
        best_score = score

    iteration_count += 1

if best_score == 0:
    print('Target string successfully generated in ', iteration_count , ' iterations:', "".join(best))
else:
    print('Algorithm did not converge within the iteration limit.')
