"""Create a file `primes.txt` containing the prime numbers up to 10^9."""

from sympy import primerange


def generate_primes_sympy(limit: int, output_file: str = "./src/primes.txt"):
    """
    Generate all primes up to limit using sympy's optimized primerange.
    Sympy uses highly optimized algorithms and is very efficient.
    """
    print(f"Generating primes up to {limit:,}...")
    
    count = 0
    with open(output_file, "w") as f:
        for prime in primerange(2, limit + 1):
            f.write(f"{prime}\n")
            count += 1
            if count % 1_000_000 == 0:
                print(f"  Generated {count:,} primes...")
    
    print(f"✓ Generated {count:,} primes up to {limit:,}")
    print(f"✓ Saved to {output_file}")


if __name__ == "__main__":
    limit = 10**9
    generate_primes_sympy(limit)


