def shuttle(n, t, m, timetable):
# 1 타임테이블을 sort한다
    timetable.sort()
# 2 n개의 버스 객체 (출발시간, 승객명단)생성
# 3 가장 마지막 배차된 버스의 승객이 꽉찼으면 제일 마지막 승객 도착 시간 -1 시간에 간다.
#   아니면 마지막 배차 버스 시간에 간다.
    pass


def compareTime(a,b):
    hourA = int(a[0]) * 10 + int(a[1])
    minuteA = int(a[3]) * 10 + int(a[4])
    hourB = int(b[0]) * 10 + int(b[1])
    minuteB = int(b[3]) * 10 + int(b[4])
    if hourA > hourB:
        return True
    elif hourA == hourB and minuteA > minuteB:
        return True
    else:
        return False


class bus:
    def __init__(self, time):
        self.leavingTime = time
        self.customerList = []
    pass

shuttle(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
shuttle(2, 10, 2, ["09:10", "09:09", "08:00"] )
shuttle(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
shuttle(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"] )
shuttle(1, 1, 1, ["23:59"] )
shuttle(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
