from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # Get key dimensions
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        # If the total length is greater than the string, no solution exists
        if len(s) < total_len:
            return []
        
        # Create a word frequency map
        word_freq = Counter(words)
        result = []
        
        # Check all possible starting positions for each "offset"
        for offset in range(word_len):
            left = offset
            right = left
            current_counter = Counter()
            words_found = 0
            
            # Sliding window approach
            while right + word_len <= len(s):
                # Get the next word
                word = s[right:right + word_len]
                right += word_len
                
                # If this word isn't in our dictionary, reset the window
                if word not in word_freq:
                    left = right
                    current_counter.clear()
                    words_found = 0
                    continue
                
                # Add this word to our current window
                current_counter[word] += 1
                words_found += 1
                
                # If we've found too many occurrences of this word
                while current_counter[word] > word_freq[word]:
                    # Remove words from the left until we have the right count
                    left_word = s[left:left + word_len]
                    current_counter[left_word] -= 1
                    left += word_len
                    words_found -= 1
                
                # If we've found exactly the right number of words
                if words_found == word_count:
                    result.append(left)
                    
                    # Slide the window by removing the leftmost word
                    left_word = s[left:left + word_len]
                    current_counter[left_word] -= 1
                    left += word_len
                    words_found -= 1
        
        return result