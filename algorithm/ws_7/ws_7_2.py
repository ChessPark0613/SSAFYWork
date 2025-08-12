T = int(input())

save = {'(', ')', '{', '}', '[', ']'}
pair = {')': '(', ']': '[', '}': '{'}

for test_case in range(1, T + 1):
    base = [ch for ch in input() if ch in save]

    st = []
    for ch in base:
        if ch in '([{':
            st.append(ch)
        else:
            if st and st[-1] == pair[ch]:
                st.pop()
            else:
                st.append(ch)


    if st:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} 1")