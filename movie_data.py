'''FUNCTION MovieDataManagement
    // Define variables to store movie information
    SET movie_info to TUPLE ("The Shawshank Redemption", "Frank Darabont")
    SET cast to LIST ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]
    SET new_actor to "William Sadler"
    
    // 1. Accessing Movie Data
    DISPLAY "Movie Information:"
    DISPLAY "Title: " + movie_info[0]
    DISPLAY "Director: " + movie_info[1]
    
    DISPLAY "Original Cast:"
    DISPLAY "Lead Actor: " + cast[0]
    DISPLAY "Supporting Actor: " + cast[1]
    DISPLAY "Antagonist: " + cast[2]
    
    DISPLAY "Complete Original Cast: " + cast
    
    // 2. Modifying Cast List
    // Add the new actor to the cast
    APPEND new_actor to cast
    
    DISPLAY "Updated Cast after adding " + new_actor + ":"
    DISPLAY cast
    
    // Demonstrating tuple immutability
    DISPLAY "Demonstrating tuple immutability:"
    TRY
        DISPLAY "Attempting to modify the movie's title..."
        SET movie_info[0] to "The Shawshank Redemption (1994)"
    CATCH TypeError as e
        DISPLAY "Error: " + e
        DISPLAY "This demonstrates that tuples cannot be modified once created."
    END TRY
    
    // Demonstrating additional list operations
    DISPLAY "Additional List Operations:"
    
    // Sort the cast alphabetically
    SORT cast
    DISPLAY "Alphabetically sorted cast: " + cast
    
    // Remove an actor from the cast
    SET removed_actor to REMOVE first element from cast
    DISPLAY "After removing " + removed_actor + ":"
    DISPLAY cast
    
    // Insert an actor at a specific position
    INSERT "James Whitmore" at position 1 in cast
    DISPLAY "After inserting James Whitmore at position 1:"
    DISPLAY cast
    
    DISPLAY "This project demonstrates the key differences between tuples (immutable) and lists (mutable)."
END FUNCTION

CALL MovieDataManagement'''

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
