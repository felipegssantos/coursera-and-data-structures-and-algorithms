import pytest

from covering_segments import optimal_points, Segment


@pytest.mark.parametrize('segments, expected',
                         [([Segment(1, 3), Segment(2, 5), Segment(3, 6)], [3]),
                          ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], [3, 6])])
def test_optimal_points(segments, expected):
    assert optimal_points(segments) == expected
