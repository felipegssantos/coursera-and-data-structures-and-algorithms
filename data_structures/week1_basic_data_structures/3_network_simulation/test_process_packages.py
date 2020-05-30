from pathlib import Path

import pytest

from process_packages import process_requests, Request, Response, Buffer


@pytest.fixture(params=list(range(1, 23)))
def request_response_generators(request):
    path = Path(__file__, '../tests').resolve()
    i_str = str(request.param).rjust(2, '0')
    input_path = Path(path, i_str)
    answer_path = Path(path, f'{i_str}.a')
    return requests_generator(input_path), responses_generator(answer_path)


def requests_generator(path):
    with open(path) as input_file:
        buffer_size, n_requests = input_file.readline().split()
        yield int(buffer_size), int(n_requests)
        for line in input_file:
            arrived_at, time_to_process = line.split()
            yield Request(int(arrived_at), int(time_to_process))


def responses_generator(path):
    def parse_expected_response(started_at):
        was_dropped = False if started_at >= 0 else True
        return Response(was_dropped, started_at)

    with open(path) as answer_file:
        return [parse_expected_response(int(line)) for line in answer_file]


def test_process_packages(request_response_generators):
    incoming_requests, expected_responses = request_response_generators
    buffer_size, n_requests = next(incoming_requests)

    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = next(incoming_requests)
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    assert responses == expected_responses
