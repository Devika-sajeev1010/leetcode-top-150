from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)
        ans = []

        for i in range(word_len):
            left = i
            current = Counter()
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    current[word] += 1
                    count += 1

                    while current[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    current.clear()
                    count = 0
                    left = right + word_len

        return ans