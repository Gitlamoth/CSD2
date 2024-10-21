import random

def generate_lists(n, mod_value):
    # Step 1: Generate the initial list of numbers from 0 to n
    original_list = list(range(n + 1))
    
    # Step 2: Apply modulo operation
    mod_list = [x % mod_value for x in original_list]
    
    # Step 3: Generate two separate lists of random numbers (1 to 2)
    random_list_1 = [random.randint(1, 2) for _ in original_list]
    random_list_2 = [random.randint(1, 2) for _ in original_list]
    
    # Step 4: Multiply each number in mod_list by the corresponding random number, separately
    result_list_1 = [mod_list[i] * random_list_1[i] for i in range(len(mod_list))]
    result_list_2 = [mod_list[i] * random_list_2[i] for i in range(len(mod_list))]

    return result_list_1, result_list_2

# Example usage:
n = 10   # Upper limit of the range
mod_value = 4   # Modulo divisor
result_list_1, result_list_2 = generate_lists(n, mod_value)

# Print the results
print("First result list:", result_list_1)
print("Second result list:", result_list_2)
