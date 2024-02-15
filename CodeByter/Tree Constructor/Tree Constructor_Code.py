def ArrayChallenge(strArr):
    parent_map = {}

    for pair in strArr:
        child, parent = map(int, pair.strip("()").split(","))
        if parent in parent_map:
            return "false"
        else:
            parent_map[parent] = child

    root_count = sum(1 for parent in parent_map if parent not in parent_map.values())
    return "true" if root_count == 1 else "false"

# Keep this function call here
print(ArrayChallenge(raw_input()))
