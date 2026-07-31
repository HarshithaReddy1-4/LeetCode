class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        dd = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        s = ''.join(sorted(word, key = lambda x: d[x], reverse = True))
        ch = 1
        key = 2
        for i in s:
            if dd[i] == 0:
                dd[i] = ch
                key += 1
                if key == 10:
                    ch += 1
                    key = 2
        count = 0
        for k, v in dd.items():
            count += v * d[k]
        
        return count


            

        