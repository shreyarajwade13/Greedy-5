"""
4 pointers solution (Backtracking) Refer notes in the book for details/dry run -
TC = O(min(m, s)) ==> avg
TC worst case - O(m*n)
SC = O(1)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p: return True

        # initialize 4 pointers
        sstar = -1
        pstar = -1
        sp = 0
        pp = 0

        m = len(p)
        n = len(s)

        while sp < n:
            # pp < m ==> to check if we are within bounds
            if pp < m and (p[pp] == s[sp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < m and p[pp] == '*':
                pstar = pp
                sstar = sp
                pp += 1
            elif pstar == -1: return False
            else:
                sp = sstar + 1
                pp = pstar
                sstar = sp
        # this is for cases like ==> s = acdceb p = *a*b***a
        while pp < m:
            if p[pp] != '*':
                return False
            pp += 1
        return True