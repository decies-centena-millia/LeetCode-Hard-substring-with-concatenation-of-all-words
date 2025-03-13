# Background
This is a solution to a LeetCode Hard problem, getting 23ms runtime using python

# Intuition
The key here is to use a sliding window approach with a word frequency counter to efficiently check for valid substrings in the main string.

# Approach
1. Create a frequency counter for the words we need to find
2. Use a sliding window approach with an offset mechanism to handle word boundaries
3. For each possible starting position:
* Add words to our current window and track their frequency
* If we encounter an invalid word, reset the window
* If we have too many occurrences of a valid word, slide the window from the left
* When we find exactly the right number of words, record the starting position
* Continue sliding the window to find more matches
# Complexity
## Time complexity:
O(N × M × L) where N is the length of string s, M is the length of each word, and L is the number of words
## Space complexity:
O(L) for storing the word frequency counters
