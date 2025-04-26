from math import ceil

class Pagination:
    def __init__(self, data, items_on_page):
        if items_on_page <= 0:
            raise ValueError("items_on_page must be positive")
        self.data = data
        self.items_on_page = items_on_page

    @property
    def page_count(self):
        return ceil(len(self.data) / self.items_on_page)

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        if page_number >= self.page_count or page_number < 0:
            raise Exception('Invalid index. Page is missing.')
        if page_number == self.page_count - 1:
            return self.item_count - self.items_on_page * (self.page_count - 1)
        else:
            return self.items_on_page

    def what_page(self, index):
        return index // self.items_on_page

    def find_page(self, data):
        if data not in self.data:
            raise Exception(f'\'{data}\' is missing on the pages')
        index = 0
        res = []
        while self.data.find(data,index) != -1:
            i = self.what_page(self.data.find(data, index))
            res.append(self.what_page(self.data.find(data, index)))
            while self.what_page(self.data.find(data, index) + len(data) - 1) > i:
                res.append(self.what_page(self.data.find(data, index)) + i)
                i += 1
            index = self.data.find(data, index) + 1
        return res

    def display_page(self, page_number):
        if page_number >= self.page_count or page_number < 0:
            raise Exception('Invalid index. Page is missing.')
        return self.data[page_number * self.items_on_page : (page_number + 1) * self.items_on_page]

if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    assert pages.page_count == 4
    assert pages.item_count == 19
    assert pages.count_items_on_page(0) == 5
    assert pages.count_items_on_page(3) == 4
    try:
        pages.count_items_on_page(4)
        pages.find_page('great')
    finally:
        assert pages.find_page('Your') == [0]
        assert pages.display_page(0) == 'Your '
        assert pages.find_page('Your') == [0]
        assert pages.find_page('e') == [1, 3]
        assert pages.find_page(' ') == [0, 2]
        assert pages.find_page('b') == [1]
        assert pages.find_page('Y') == [0]
        assert pages.find_page('beautiful') == [1, 2]
