from typing import Dict, Any, Callable, Iterable, List

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: Function to select specific columns
    :param filters: Functions to filter data based on column values
    :return: Filtered data with selected columns
    """
    processed_data = selector(data)
    for filter_func in filters:
        processed_data = filter_func(processed_data)
    return processed_data


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def select_columns(data: DataType) -> DataType:
        return [
            {col: item[col] for col in columns}
            for item in data
        ]
    return select_columns


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def filter_columns(data: DataType) -> DataType:
        return [
            item for item in data
            if item.get(column) in values
        ]
    return filter_columns


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'samantha', 'gender': 'female', 'sport': 'volleyball'},
    ]
    value = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', 'Basketball', 'volleyball'),
        field_filter('gender', 'male'),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()