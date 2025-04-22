# Define variables to store movie information
movie_info = ("The Shawshank Redemption", "Frank Darabont")
cast = ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]
new_actor = "William Sadler"

# 1. Accessing Movie Data
# Access and print individual elements from the movie_info tuple
print("Movie Information:")
print("Title:", movie_info[0])
print("Director:", movie_info[1])

# Access and print individual elements from the cast list
print("\nOriginal Cast:")
print("Lead Actor:", cast[0])
print("Supporting Actor:", cast[1])
print("Antagonist:", cast[2])

# Print the entire cast list
print("\nComplete Original Cast:", cast)

# 2. Modifying Cast List
# Add the new actor to the cast
cast.append(new_actor)

# Print the updated cast list
print("\nUpdated Cast after adding", new_actor + ":")
print(cast)

# Demonstrating that tuples are immutable (cannot be modified)
print("\nDemonstrating tuple immutability:")
try:
    print("Attempting to modify the movie's title...")
    movie_info[0] = "The Shawshank Redemption (1994)"
except TypeError as e:
    print("Error:", e)
    print("This demonstrates that tuples cannot be modified once created.")

# Demonstrating additional list operations
print("\nAdditional List Operations:")
# Sort the cast alphabetically
cast.sort()
print("Alphabetically sorted cast:", cast)

# Remove an actor from the cast
removed_actor = cast.pop(0)  # Removes and returns the first actor
print("After removing", removed_actor + ":")
print(cast)

# Insert an actor at a specific position
cast.insert(1, "James Whitmore")
print("After inserting James Whitmore at position 1:")
print(cast)

print("\nThis project demonstrates the key differences between tuples (immutable) and lists (mutable).")