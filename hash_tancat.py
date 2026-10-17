# Estats d'una posició de la taula (hash tancat). NO canvieu aquests valors.
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:

    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [None, None, LLIURE]   # m posicions, inicialment buides
        self._n = 0                                # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)              # h(x) = x % m

    def put(self, key: int, value: int) -> None:

        reminder = None

        m = len(self._table)
        start = self._hash_function(key)
        
        for i in range(m):

            j = (start + i) % m
            slot = self._table[j]

            if slot[2] == OCUPAT:
                if slot[0] == key:
                    self._table[j][1] = value
                    break
                else:
                    continue
            elif slot[2] == ESBORRAT:
                if reminder is None:
                    reminder = j
                continue
            elif slot[2] == LLIURE:
                if reminder is not None:
                    self._table[reminder] = [key, value, OCUPAT]
                else:
                    self._table[j] = [key, value, OCUPAT]
                self._n += 1
                break
        else:
            if reminder is not None:
                self._table[reminder] = [key, value, OCUPAT]
                self._n += 1


        if self._n > len(self._table) // 2:
            self._resize(2*len(self._table)-1)




        # j = self._hash_function(key)
        # if self._table[j] is None:                 # posició lliure
        #     self._table[j] = [key, value]
        #     self._n += 1
        # elif self._table[j][0] == key:             # mateixa clau: actualitzem
        #     self._table[j][1] = value
        # else:                                      # una altra clau: COL·LISIÓ
        #     raise KeyError(f"COL·LISIÓ: {key} amb {self._table[j][0]}")

    def get(self, key: int) -> int:

        ubi = self._find(key)
        if ubi is None:
            return -1
        else:
            return self._table[ubi][1]
        # j = self._hash_function(key)
        # if self._table[j] is not None and self._table[j][0] == key:
        #     return self._table[j][1]
        # return -1

    def remove(self, key: int) -> None:
        ubi = self._find(key)

        if ubi is not None:
            self._table[ubi] = [None, None, ESBORRAT]
            self._n -= 1

    def __len__(self):
        return self._n

    def _find(self,key):
        m = len(self._table)
        start = self._hash_function(key)

        for i in range(m):
            j = (start + i) % m
            slot = self._table[j]
            if slot[2] is LLIURE :
                return None
            if slot[2] is ESBORRAT :
                continue
            if slot[2] is OCUPAT and key == slot[0]:
                return j

        return None
    
    def _resize(self, c):

        old = self._table
        self._table = c * [None, None, LLIURE]
        self._n = 0


if __name__ == '__main__':

    hm = MyHashMap()
    
    hm.put(40, 7)
    hm.put(14, 3)        # h(14) = h(40) = 1: va a la posició 2
    hm.put(27, 1)        # h(27) = 1: va a la posició 3
    hm._table[1:4]       # → [[40, 7, 'O'], [14, 3, 'O'], [27, 1, 'O']]
    hm.remove(14)
    hm._table[2]         # → [None, None, 'B']
    hm.get(27)           # → 1   (salta la posició ESBORRAT 2)
    hm.get(14)           # → -1
    hm.put(53, 9)        # h(53) = 1: reutilitza la posició ESBORRAT 
    hm._table[2]         # → [53, 9, 'O']
    len(hm)              # → 3

    # Part 2
    hm = MyHashMap()

    for k in [23, 45, 16, 26, 40, 14, 5, 12, 9, 25]:
        hm.put(k, 10 * k)
    
    len(hm._table)       # → 25  (ha redimensionat en inserir la 7a clau)
    hm.get(25)           # → 250    