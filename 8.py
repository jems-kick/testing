class Solution:
    def myAtoi(self, s) -> int:
        gotnumbers = False
        value = []
        for i in s:
            if i == " " and gotnumbers == True:
                break
            elif i == "-":
                value.append(i)
                next
            elif '0' <= i <= '9':
                gotnumbers = True
                value.append(int(i))
            elif i is not i.isdigit() and i != " ":
                break
        if len(value) > 0:
            final =  int(''.join(map(str, value)))
            return final
		
s = Solution()
value = str(input("Enter value : "))
print(s.myAtoi(value))