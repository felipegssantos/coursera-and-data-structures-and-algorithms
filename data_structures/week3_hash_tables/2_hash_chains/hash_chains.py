# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:

    def __init__(self, m, p=1000000007, x=263):
        self.m = m
        self.p = p
        self.x = x
        self.n = 0
        self.records = self.init_records()

    def init_records(self):
        return [[] for _ in range(self.m)]

    @property
    def load_factor(self):
        return self.n / self.m

    def hash(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self.x + ord(c)) % self.p
        return ans % self.m

    def add(self, value):
        chain = self.records[self.hash(value)]
        for i in range(len(chain)):
            if chain[i] == value:
                return
        chain.append(value)
        self.n += 1

    #     if self.load_factor > 1:
    #         self.m = 2 * self.m
    #         self.rehash()

    # def rehash(self):
    #     old_records = self.records
    #     self.contacts = self.init_records()
    #     for old_chain in old_records:
    #         first_record = old_chain[0]
    #         chain = self.records[self.hash(first_record)]
    #         for record in old_chain:
    #             chain.append(record)

    def delete(self, value):
        chain = self.records[self.hash(value)]
        for i in range(len(chain)):
            if chain[i] == value:
                chain.pop(i)
                self.n -= 1
                break

    def find(self, value):
        chain = self.records[self.hash(value)]
        for i in range(len(chain)):
            if chain[i] == value:
                return 'yes'
        return 'no'

    def check(self, index):
        chain = self.records[index]
        return ' '.join(reversed(chain))

    def process_queries(self, queries=None):
        if queries is None:
            n = int(input())
            queries = [Query(input().split()) for _ in range(n)]

        result = []
        for query in queries:
            if query.type == 'check':
                result.append(self.check(query.ind))
            elif query.type == 'find':
                result.append(self.find(query.s))
            elif query.type == 'add':
                self.add(query.s)
            elif query.type == 'del':
                self.delete(query.s)
            else:
                raise ValueError(f'Unexpected query type: {query.type}')

        return result


class NaiveQueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    result = proc.process_queries()
    print('\n'.join(result))
