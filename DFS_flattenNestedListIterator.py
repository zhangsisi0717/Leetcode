###recursion algorithm to flatten the nestedList
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.raw = nestedList
        self.flat_list = self.flatten()
        self.cur_idx = 0

    def next(self) -> int:
        val = self.flat_list[self.cur_idx]
        self.cur_idx = self.cur_idx +1
        return val.getInteger()

    def hasNext(self) -> bool:
        return self.cur_idx <= len(self.flat_list)-1

    def flatten(self) -> list:
        def recur(l):
            if l.isInteger():
                return [l]
            re = []
            cur_list = l.getList()
            for e in cur_list:
                re+=recur(e)
            return re
        final=[]
        for i in self.raw:
            final += recur(i)
        return final

