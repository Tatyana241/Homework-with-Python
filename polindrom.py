if Solution.all_same(palindrome):
        while end < len(s) - 1:
            if s[end+1] == s[start]:
                end += 1
                palindrome += s[end]
            else:
                break
