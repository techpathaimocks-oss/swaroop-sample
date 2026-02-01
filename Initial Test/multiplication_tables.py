#!/usr/bin/env python3
"""
Multiplication Tables Generator
Generates multiplication tables from 2 to 10, up to multiple of 10.
"""

def generate_multiplication_tables():
    """Generate and print multiplication tables from 2 to 10."""
    print("Multiplication Tables (2 to 10)")
    print("=" * 50)
    
    for table in range(2, 11):
        print(f"\nTable of {table}:")
        print("-" * 20)
        for multiplier in range(1, 11):
            product = table * multiplier
            print(f"{table} × {multiplier:2} = {product:3}")
    
    print("\n" + "=" * 50)
    print("All tables generated successfully!")

if __name__ == "__main__":
    generate_multiplication_tables()