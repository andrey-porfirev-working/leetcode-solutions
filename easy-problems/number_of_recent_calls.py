class RecentCounter:

    def __init__(self):
        self.requests = list()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000 or self.requests[0] > t:
            self.requests.pop(0)
        return len(self.requests)


class RecentCounter_v_2:

    def __init__(self):
        self.requests = list()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)

class RecentCounter_v_3:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000 or self.requests[0] > t:
            self.requests.pop(0)
        return len(self.requests)


from collections import deque


class RecentCounter_v_4:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)