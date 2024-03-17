**Objective:**

Find the maximum value of \( f(x) = x^2 \) within the range 0 to 31. 🎯

**Solution Representation:**

Each potential solution (x) is encoded as a binary string of length 5, representing values from 0 (00000) to 31 (11111). 🔢

**Genetic Algorithm Components:**

1. **Objective Function:**
   - Defined as `objective_function(x) = x**2`. This calculates the fitness score of a solution (x). 🧬

2. **Input Parameters:**
   - **Population Size (p):** Number of individuals in the population (solutions).
   - **Crossover Type (c):**
     - 0: One-point crossover - Swaps genetic material at a single crossover point between parents.
     - 1: Two-point crossover - Swaps genetic material between two crossover points.
   - **Mutation Type (m):**
     - 0: Bit flip mutation - Flips a random bit in the binary string.
     - 1: Swap mutation - Swaps two randomly chosen bits in the string.
   - **Termination Condition (t):**
     - 0: No improvement for x iterations - Stops when there's no improvement in fitness for a set number of iterations (x).
     - 1: Predefined iterations - Stops after a predefined number of iterations (i).
   - **Iterations (i):** Used for termination condition (t = 1).
   - **No Improvement Iterations (x):** Used for termination condition (t = 0). ⏳

3. **Output:**
   - The algorithm returns the best solution (binary string) found along with its corresponding fitness value (f(x)). 📈

**Usage Examples:**

The provided examples demonstrate how to use the genetic algorithm with different parameter settings. 📝

**Note:**

The GA results can vary due to the randomness involved in its core operations. 🔄

**Credits:**

This implementation is credited to AJ Harsh Vardhan on March 12, 2024. 🙌
