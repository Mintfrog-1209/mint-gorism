s = "aabbaccc"
for n in range(len(s)):
        new_s = ''
        cnt = 0
        idx = 0
        while idx < len(s):
            if s[idx:(idx+n)] == s[(idx+n):(idx+2*n)]:
                print(s[idx:(idx+n)], s[(idx+n):(idx+2*n)])
                idx += n
                cnt += 1
            else:
                if cnt > 1:
                    new_s += str(cnt)
                new_s += s[idx:(idx+n)]
                idx += n
            print(n)