print("🎉 Welcome to the Power Set Maker Quiz!")

# Step 1: Ask the user for a list
input_string = input("👉 Enter 3 numbers separated by commas (like 1,2,3): ")

#Step 2: Convert input to a list
items = input_string.split(",")

# Remove spaces and keep clean items
items = [item.strip() for item in items]

# Start with just the empty set
power_set = [[]]

print("\n🔍 Let's build the power set step by step!")

# Step 3: Build power set
for item in items:
    print(f"\n✨ Adding item: {item}")
    new_subsets = []

    for subset in power_set:
        new_subset = subset + [item]
        print(f"  ➕ Adding {item} to {subset} ➡ {new_subset}")
        new_subsets.append(new_subset)

    power_set.extend(new_subsets)

# Step 4: Show final result
print("\n🎯 Final Power Set:")
for subset in power_set:
    print(subset)

print("\n 🎊 Yay! You made a Power Set!")