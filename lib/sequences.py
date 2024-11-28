def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return

    if length == 1:
        print("[0]")
        return

    if length == 2:
        print("[0, 1]")
        return

    # Initialize the Fibonacci sequence
    fibonacci = [0, 1]

    # Generate the Fibonacci sequence
    for _ in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    # Print the final sequence as a single line
    print(f"[{', '.join(map(str, fibonacci))}]")
