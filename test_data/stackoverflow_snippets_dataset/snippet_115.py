# Extracted from https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
X = [1.5, 2.3, 4.4, 5.4, 'n', 1.5, 5.1, 'a']     # Original list

# Extract non-strings from X to new list
X_non_str = [el for el in X if not isinstance(el, str)]  # When using only 'if', put 'for' in the beginning

# Change all strings in X to 'b', preserve everything else as is
X_str_changed = ['b' if isinstance(el, str) else el for el in X]  # When using 'if' and 'else', put 'for' in the end

