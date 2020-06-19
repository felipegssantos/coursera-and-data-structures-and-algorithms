# python3

from collections import namedtuple
from random import randint


Record = namedtuple('Record', ['phone', 'name'])


class PhoneBook:

    def __init__(self, key_length=7, prime=10000019, table_size=2):
        assert 10**key_length < prime
        self.m = table_size
        self.contacts = self.init_contacts()

        self.key_length = key_length
        self.p = prime
        self.a = randint(1, self.p - 1)
        self.b = randint(0, self.p - 1)

        self.n = 0

    def init_contacts(self):
        return [[] for _ in range(self.m)]

    @property
    def load_factor(self):
        return self.n / self.m

    def hash(self, x):
        return ((self.a * int(x) + self.b) % self.p) % self.m

    def add(self, phone, name):
        chain = self.contacts[self.hash(phone)]
        for i in range(len(chain)):
            if chain[i].phone == phone:
                chain.pop(i)
                break
        chain.append(Record(phone, name))

        if self.load_factor > 1:
            self.m = 2 * self.m
            self.rehash()

    def reshash(self):
        old_contacts = self.contacts
        self.contacts = self.init_contacts()
        for old_chain in old_contacts:
            first_record = old_chain[0]
            chain = self.contacts[self.hash(first_record.phone)]
            for record in old_chain:
                chain.append(record)

    def delete(self, phone):
        chain = self.contacts[self.hash(phone)]
        for i in range(len(chain)):
            if chain[i].phone == phone:
                chain.pop(i)
                break

    def find(self, phone):
        chain = self.contacts[self.hash(phone)]
        for i in range(len(chain)):
            if chain[i].phone == phone:
                return chain[i].name


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    book = PhoneBook(table_size=len(queries))
    for cur_query in queries:
        if cur_query.type == 'add':
            book.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            book.delete(cur_query.number)
        else:
            response = book.find(cur_query.number)
            if response is None:
                response = 'not found'
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
