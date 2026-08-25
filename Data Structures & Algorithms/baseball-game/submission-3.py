class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res =[]

        for op in operations:
            if op == 'D':
                res.append(2*res[-1])
                print(res)
            elif op == 'C':
                res.pop()
                print(res)
            elif op == '+':
                res.append(sum(res[-2:]))
                print(res)
            else: 
                res.append(int(float(op)))
                print(res)
        return sum(res)