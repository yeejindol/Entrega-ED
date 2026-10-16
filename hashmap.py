class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        self._bucket_put(j, key, value)

        # if self._table[j] is None:             # posició lliure
        #     self._table[j] = [key, value]
        #     self._n += 1
        # elif self._table[j][0] == key:         # mateixa clau: actualitzem
        #     self._table[j][1] = value
        # else:                                  # una altra clau: COL·LISIÓ
        #     raise KeyError(f"COL·LISIÓ: {key} amb {self._table[j][0]}")

        if self._n > len(self._table) // 2 :
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        j = self._hash_function(key)
        return self._bucket_get(j, key)

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        self._bucket_remove(j, key)

        return

    def __len__(self):
        return self._n

    def _resize(self, c) :
        old = self._table
        self._table = c * [None]
        self._n = 0

        for bucket in old:
            if bucket is not None:
                for item in bucket:
                    self.put(item[0], item[1])

                

    def _bucket_put(self, j, key, value):

        if self._table[j] is None :
            self._table[j] = []

        for item in self._table[j]:
            if key == item[0]:
                item[1] = value
                return

        self._table[j].append([key, value])
        self._n += 1

    def _bucket_get(self, j, key):
        bucket = self._table[j]

        if bucket is not None:
            for item in bucket:
                if item[0] == key:
                    return item[1]

        return -1

    def _bucket_remove(self, j, key):

        bucket = self._table[j]

        if bucket is None:
            return -1

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self._n -= 1
                return

                
            



if __name__ == '__main__' :

    hm = MyHashMap()
    hm.put(40, 7)
    hm.put(14, 3)        # h(14) = h(40) = 1: ara NO dona error
    print(hm.get(14))           # → 3
    print(hm.get(40))           # → 7
    print(hm.get(27))           # → -1  (27 també va a la posició 1, però no hi és)
    hm.put(14, 99)       # actualitza
    print(hm.get(14))           # → 99
    hm.remove(40)
    print(hm.get(40))           # → -1
    print(len(hm))              # → 1

    # Part 2
    hm = MyHashMap()
    for k in [23, 45, 16, 26, 40, 14, 5, 12, 9, 25]:
        hm.put(k, 10 * k)
    
    len(hm._table)       # → 25  (ha redimensionat en inserir la 7a clau)
    hm._table[0]         # → [[25, 250]]  (25 % 25 = 0)