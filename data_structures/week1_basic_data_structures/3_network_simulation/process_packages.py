# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:

    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # Remove finished packets from processing queue
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)

        if len(self.finish_time) < self.size:
            try:
                start_time = max(self.finish_time[-1], request.arrived_at)
            except IndexError:  # self.finish_time is empty
                start_time = request.arrived_at
            end_time = start_time + request.time_to_process
            self.finish_time.append(end_time)
            return Response(False, start_time)
        else:
            return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
