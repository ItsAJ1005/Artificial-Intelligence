# Topic: Genetic Algorithm based on objective function f(x) = x^2

# Finding the maximum F(x) = x^2 over the interval 0-31 using a Genetic Algorithm (GA). Representing each possible solution as a binary string of 5 bits.
# We are not using PyGad library in this.
# Input:
# 1) Population size [p]
# 2) Crossover type [c] (Default: one point crossover (c=0) or two point crossover (c=1) )
# 3) Mutation type [m] (Default: Bit flip (m=0) or swap mutation (m=1))
# 4) GA termination condition [t] ( Default: No improvement for x iteration (t=0) or predefined iterations (t=1) )
# 5) if t = 0 No improvement for x iteration [x]
# 6) if t =1 Predefined iterations for termination [i]

# Input example: p=10, c=0 (default), m=1(swap mutation), t=1 (predefined iterations then i=100)

# Another example: p=5, c=1 ( two point crossover ), m=0( Default ), t=0 ( No improvement for x iteration then x=10)

# Output: Highest fitness value solution when termination condition met.


# Code:

import numpy as np

def objective_function(x):      # Our function f(x) = x^2 which should be maximized
    return x**2

def binary_to_decimal(binary_str):
    return int(''.join(map(str, binary_str)), 2)
# Using map to ensure that the binary_str provided is a string and convert otherwise
# In next step we get int(binary_str, 2) which converts this base 10 str to base 2 integer

def initialize_population(population_size, chromosome_length):
    return np.random.randint(2, size=(population_size, chromosome_length))

# Sample Initial Population:
# [[0 1 1 0 1]
#  [1 0 1 1 0]
#  [0 1 1 1 1]
#  [0 0 1 0 1]
#  [1 0 0 0 1]]     - Initializes population like this.


def one_point_crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1)-1)                              # Chosing a random crossover single point
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))     # Concatenating parent1 upto point and parent2 after point 
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))     # Concatenating parent2 upto point and parent1 after point [Crossover]
    return child1, child2

def two_point_crossover(parent1, parent2):
    crossover_points = np.sort(np.random.choice(len(parent1)-1, 2, replace=False))      # Choosing 2 random crossover points (not same)
    child1 = np.concatenate((parent1[:crossover_points[0]], parent2[crossover_points[0]:crossover_points[1]], parent1[crossover_points[1]:]))
    child2 = np.concatenate((parent2[:crossover_points[0]], parent1[crossover_points[0]:crossover_points[1]], parent2[crossover_points[1]:]))
    return child1, child2

def bit_flip_mutation(chromosome):
    mutation_point = np.random.randint(len(chromosome))                                 # Random mutation point
    chromosome[mutation_point] = 1 - chromosome[mutation_point]                         # Flip that point
    return chromosome

def swap_mutation(chromosome):
    mutation_points = np.sort(np.random.choice(len(chromosome), 2, replace=False))     # 2 random points from chromosome 
    chromosome[mutation_points[0]], chromosome[mutation_points[1]] = chromosome[mutation_points[1]], chromosome[mutation_points[0]]    #Swap
    return chromosome

def genetic_algorithm(population_size, crossover_type=0, mutation_type=0, termination_condition=0, x_iterations=10, predefined_iterations=100):
    chromosome_length = 5
    population = initialize_population(population_size, chromosome_length)

    best_solution = None                        # Initializing a best solution
    best_fitness = -float('inf')                # Initializing fitness to -infinite in float 
    iterations = 0                              # Iteration counter

    while True:
        fitness_values = [objective_function(binary_to_decimal(individual)) for individual in population]  # f(x) values stored in array

        if max(fitness_values) > best_fitness:              # Finding best fitness which is currently -inf
            best_index = np.argmax(fitness_values)          # Storing idx of highest fitness 
            best_solution = population[best_index]          # Best sol found till now from population
            best_fitness = fitness_values[best_index]       # Updating best fitness
            iterations = 0                                  # Reseting counter after new best is found
        else:
            iterations += 1                                 

        if termination_condition == 0 and iterations >= x_iterations:                   # Checking Termination case for t=0
            break
        elif termination_condition == 1 and iterations >= predefined_iterations:        # Checking termination case for t=1
            break
        
        # Roulette Wheel Selection
        fitness_summation = np.sum(fitness_values)                                      # Summation f(x)
        fitness_probs = fitness_values / fitness_summation                              # probability = fi / (summation fi)
        parents_indices = np.random.choice(population_size, size=2, replace=False, p=fitness_probs)
        parent1, parent2 = population[parents_indices]                                  # chosing best parents

        if crossover_type == 0:
            child1, child2 = one_point_crossover(parent1, parent2)                      # new offsprings by one point crossover
        else:
            child1, child2 = two_point_crossover(parent1, parent2)                      # new offsprings by two point crossover          

        if mutation_type == 0:
            child1 = bit_flip_mutation(child1)                                          # new mutation by bit flip
            child2 = bit_flip_mutation(child2)                                          # new mutation by bit flip
        else:   
            child1 = swap_mutation(child1)                                              # new mutation by swapping 2 bits
            child2 = swap_mutation(child2)                                              # new mutation by swapping 2 bits

        population[parents_indices] = child1, child2                                    # Repeat till one of the termination conditions is achieved

    return best_solution, best_fitness

# Example 1
population_size1 = 10
crossover_type1 = 0  # One-point crossover
mutation_type1 = 1   # Swap mutation
termination_condition1 = 1  # Predefined iterations
predefined_iters1 = 100

best_solution_1, best_fitness_1 = genetic_algorithm(population_size1, crossover_type1, mutation_type1, termination_condition1, predefined_iterations=predefined_iters1)

print("Example 1 Results:")
print(f"Best Solution: {best_solution_1}")              # f gives the solution in between { }
print(f"Best Fitness Value: {best_fitness_1}\n")

# Example 2
population_size2 = 5
crossover_type2 = 1  # Two-point crossover
mutation_type2 = 0   # Bit flip mutation
termination_condition2 = 0  # No improvement for x iterations
x_iterations_2 = 10

best_solution_2, best_fitness_2 = genetic_algorithm(population_size2, crossover_type2, mutation_type2, termination_condition2, x_iterations=x_iterations_2)

print("Example 2 Results:")
print(f"Best Solution: {best_solution_2}")              
print(f"Best Fitness Value: {best_fitness_2}")

# Genetic algo produces different values each time due to different crossovers, mutations and random populations 

# Some of the outputs recieved by this algorithm: [Subject to differ for each run]
# Example 1 Results:
# Best Solution: [1 1 0 1 1]
# Best Fitness Value: 961

# Example 2 Results:
# Best Solution: [1 1 1 1 1]
# Best Fitness Value: 961
# PS D:\AI\Genetic ALgo> python -u "d:\AI\Genetic ALgo\S20220010011_GA1.py"
# Example 1 Results:
# Best Solution: [0 0 1 1 1]
# Best Fitness Value: 961

# Example 2 Results:
# Best Solution: [1 1 1 1 0]
# Best Fitness Value: 961 

# © AJ Harsh Vardhan - 12th March 24
