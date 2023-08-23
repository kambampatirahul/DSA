class Solution:
    def calculate(s):
        n, st, sign = '', [], '+'
        s = s.replace(' ','')
        for i in s+'+':
            if i.isdigit():
                n += i
            elif sign == '+':
                st.append(int(n))
                n = ''
                sign = i
            elif sign == '-':
                st.append(-int(n))
                n = ''
                sign = i
            elif sign == '*':
                st.append(st.pop() * int(n))
                n = ''
                sign = i
            elif sign == '/':
                st.append(int(st.pop() / int(n)))
                n = ''
                sign = i
        return sum(st)
    print(calculate('14-3/2'))