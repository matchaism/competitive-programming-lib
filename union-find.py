from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        """
        初期化
        Parameters
        --------------------
        n : int
            ノード数
        parents : list
            各ノードの親(根)のリスト
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        ノードxが属する木の根を返す
        Parameters
        --------------------
        x : int
            根を見つけたいノード
        Returns
        --------------------
        parents : list
            各ノードの親(根)のリスト
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        ノードx, yが属する木を併合する
        Parameters
        --------------------
        x, y : int
            ノード
        """
        x, y = self.find(x), self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        ノードxが属する木のノード数
        Parameters
        --------------------
        x : int
            ノード
        Returns
        --------------------
        parents : list
            木のノード数
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        ノードx, yが同じ木に属するか
        Parameters
        --------------------
        x, y : int
            ノード
        Returns
        --------------------
        bool
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        ノードxが属する木のノードを返す
        Parameters
        --------------------
        x : int
            ノード
        root : int
            ノードxの値
        Returns
        --------------------
        list
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        Returns
        --------------------
        list
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        すべての根の要素数(木の数)
        Returns
        --------------------
        int
        """
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

# https://note.nkmk.me/python-union-find/

##### Library ends here #####
