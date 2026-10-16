
class MinStack:



    def __init__(self):

        self._stack = []

        #guarda los números para comparar
        self._min = []

    def push(self, val: int) -> None:

        # si self._min está vacía, ejecuta append(val)
        if not self._min:

            self._min.append(val)

        #si val es menor q min => append min[-1] es el numero menor
        elif val < self._min[-1]:
         
            self._min.append(val)

        #si no todo, manetiene el número original    
        else:
            self._min.append(self._min[-1])

        self._stack.append(val)



    def pop(self) -> None:
        
            self._stack.pop()
            self._min.pop()

    def top(self) -> int:

        return self._stack[-1]

    def getMin(self) -> int:       

       return self._min[-1]


if __name__ == '__main__':

    s = MinStack()

    s.push(-2)
    s.push(0)
    s.push(-3)

    print(s._stack)
    print(s.getMin())   # retorna -3
    s.pop()
    print(s.top())      # retorna 0
    print(s.getMin())   # retorna -2