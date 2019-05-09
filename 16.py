class LatestNLogs:
    def __init__(self, n):
        self.__logs = []
        self.__limit = n

    def record(self, order_id):
        self.__logs.append(order_id)
        if len(self.__logs) > self.__limit:
            self.__logs.pop(0)

    def get_last(self, i):
        if len(self.__logs) < i:
            return None
        return self.__logs[len(self.__logs)-i]

logs = LatestNLogs(3)
logs.record(123)
logs.record(234)
logs.record(345)
logs.record(456)

assert logs.get_last(1) == 456
assert logs.get_last(3) == 234
assert logs.get_last(4) is None
