# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem



def print_rangoli(size):
    # your code goes here
    import string
    alphabet = string.ascii_lowercase
    lines = []
    
    # Generate lines from the center row down to the top row
    for i in range(size):
        sub = alphabet[i:size]
        # Create the symmetric string for the row joined by hyphens
        row = "-".join(sub[::-1] + sub[1:])
        # Center the row with '-' to match the total width (4 * size - 3)
        lines.append(row.center(4 * size - 3, "-"))
        
    # Combine the reversed lines (top half) with the remaining lines (bottom half)
    full_rangoli = lines[::-1] + lines[1:]
    
    # Print each line separated by a newline
    print("\n".join(full_rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
