

# My first solution:
def is_anagram_1(self, s: str, t: str) -> bool:

    """
        Given two strings s and t, return true if the two strings are anagrams of each other,
        otherwise return false.
        An anagram is a string that contains the exact same characters as another string,
        but the order of the characters can be different.
    """

    if len(s) != len(t):
        return False
    else:
        for letter in s:
            if letter in t:
                t = t.replace(letter, "", 1)
            else:
                return False
    return True
    # time complexity of my solution: O(n^2) memory complexity: O(n) since t = t.replace()



# My second solution:
def is_anagram_2(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            s = ''.join(sorted(s))
            t = ''.join(sorted(t))
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
        return True

    # O(n log n) — for each sort
    # O(n) — each sort returns a new list of characters
    # total time: O(nlog(n) + mlog(m))   space: O(n)

# My third solution:

def is_anagram_3(self, s: str, t: str) -> bool:
    s_dict = dict() # space: O(1)  time: O(1)
    t_dict = dict() # space: O(1)  time: O(1)

    if len(s) != len(t): # space: O(1) time: O(1)
        return False
    else:
        for i in range(len(s)): # space: O(1) time: O(n)
            if s[i] in s_dict:
                s_dict[s[i]] = s_dict[s[i]] + 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] = t_dict[t[i]] + 1
            else:
                t_dict[t[i]] = 1
        for l in s:  # time: O(n)
            if l in s_dict and l in t_dict:
                if s_dict[l] != t_dict[l]:
                    return False
            else:
                return False
    return True
    # Total space: O(1) time: O(n)




# --------------------Other solutions:------------- #

def is_anagram_1o(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        # Total space: O(1) or O(n+m) depending on sorting algorithm
        # time: O(nlog(n) + mlog(m))


def is_anagram_2o(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
    # Total space: O(1)
    # time: O(n + m)


def is_anagram_3o(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True
    # Total space: O(1)
    # time: O(n + m)

