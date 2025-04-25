from math import ceil

class Pagination:
    def __init__(self, data, items_on_page):
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

    def find_page(self, data):
        if data not in self.data:
            raise Exception(f'\'{data}\' is missing on the pages')
        i=0
        res=[]
        while self.data.find(data,i) != -1:
            res.append(self.data.find(data,i) // self.items_on_page)
            i = self.data.find(data,i)+1
        return res
    def display_page(self, page_number):
        return self.data[page_number * self.items_on_page : (page_number + 1) * self.items_on_page]

if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    assert pages.page_count == 4, print(pages.page_count)
    assert pages.item_count == 19, print(pages.item_count)
    assert pages.count_items_on_page(0) == 5
    assert pages.count_items_on_page(3) == 4
    #pages.count_items_on_page(4)
    pages.find_page('Your')
    assert pages.display_page(0) == 'Your '
    print(pages.find_page('Your'))
    print(pages.find_page('e'))
    print(pages.find_page(' '))
    print(pages.find_page('b'))
    print(pages.find_page('Y'))
    print(pages.find_page('beautiful'))
    print(pages.find_page('great'))
