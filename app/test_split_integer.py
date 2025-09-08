import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (0, 0),
        (0, 1),
        (1, 0),
        (4, 17),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (0, 1),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    for index in range(len(parts)):
        if index + 1 < len(parts):
            assert parts[index] == parts[index + 1]


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (1, 1),
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts)[0] == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (7, 8),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    actual = split_integer(value, number_of_parts)
    expected = sorted(actual)
    assert expected == actual


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (5, 6),
        (7, 8),
        (0, 1),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert len(parts) == number_of_parts
