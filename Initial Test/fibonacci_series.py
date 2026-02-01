#!/usr/bin/env python3
"""
Fibonacci Series Generator
Generates Fibonacci series from initial 0 up to 100.
"""

def generate_fibonacci_series(limit=100):
    """
    Generate Fibonacci series up to a given limit.
    
    Args:
        limit (int): Maximum value in the Fibonacci series (default: 100)
    
    Returns:
        list: Fibonacci series up to the limit
    """
    fibonacci = [0, 1]
    
    while True:
        next_value = fibonacci[-1] + fibonacci[-2]
        if next_value > limit:
            break
        fibonacci.append(next_value)
    
    return fibonacci

def print_fibonacci_series(limit=100):
    """Generate and print Fibonacci series up to a given limit."""
    fibonacci = generate_fibonacci_series(limit)
    
    print(f"Fibonacci Series (up to {limit})")
    print("=" * 40)
    
    print("Sequence:", end=" ")
    for i, num in enumerate(fibonacci):
        print(num, end="")
        if i < len(fibonacci) - 1:
            print(", ", end="")
    
    print(f"\n\nTotal numbers in sequence: {len(fibonacci)}")
    print(f"Last Fibonacci number: {fibonacci[-1]}")
    print("=" * 40)

if __name__ == "__main__":
    print_fibonacci_series()