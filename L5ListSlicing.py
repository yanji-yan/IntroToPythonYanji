 # [Start : End ]

# Create a list
fam = ["yanji", 1.73, "jagi", 1.68, "ebike", 1.71, "mamaaa", 1.89]

# Slice elements from index 3 up to (but not including) index 5
print(fam[3:5])  # Output: [1.68, 'jagi']

# Slice elements from index 1 up to (but not including) index 4
print(fam[1:4])  # Output: [1.73, 'jagi', 1.68]


# Slices from the start up to (but not including) index 4
print(fam[:4])
# Output: ['yanji', 1.73, 'jagi', 1.68]

# Slices from index 5 to the end of the list
print(fam[5:])
# Output: [1.71, 'mamaaa', 1.89]
