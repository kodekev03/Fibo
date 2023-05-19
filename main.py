def generate_fibonacci_sequence(n):
    sequence = []
    explanation = []
    a, b = 0, 1
    explanation.append(f"Starting with 0 and 1 as the first two terms.")
    while len(sequence) < n:
        sequence.append(a)
        explanation.append(f"Adding {a} to the sequence.")
        a, b = b, a + b
        explanation.append(f"The next number is the sum of the previous two numbers: {b} = {a} + {b-a}.")

    return sequence, explanation

def main():
    print("Welcome to Fibo - Fibonacci Sequence Generator")
    while True:
        try:
            num_terms = int(input("Enter the number of terms: "))
            if num_terms <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    fibonacci_sequence, explanation = generate_fibonacci_sequence(num_terms)
    print("Fibonacci Sequence:")
    for term in fibonacci_sequence:
        print(term)
    print("\nStep-by-Step Explanation:")
    for step in explanation:
        print(step)

if __name__ == "__main__":
    main()
