class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = list(senate)
        rad_del_que = 0  # счетчики вместо списков
        dir_del_que = 0

        while True:
            new_senators = []
            rad_count = dir_count = 0

            for s in senators:
                if s == "R":
                    if rad_del_que > 0:
                        rad_del_que -= 1  # R удален
                    else:
                        dir_del_que += 1  # R голосует против D
                        new_senators.append("R")
                        rad_count += 1
                else:  # s == "D"
                    if dir_del_que > 0:
                        dir_del_que -= 1  # D удален
                    else:
                        rad_del_que += 1  # D голосует против R
                        new_senators.append("D")
                        dir_count += 1

            # Проверка условия завершения
            if rad_count == 0:
                return "Dire"
            if dir_count == 0:
                return "Radiant"

            senators = new_senators

    def predictPartyVictory_v_2(self, senate: str) -> str:
        rad_queue = deque()
        dir_queue = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                rad_queue.append(i)
            else:
                dir_queue.append(i)

        n = len(senate)
        while rad_queue and dir_queue:
            rad_idx = rad_queue.popleft()
            dir_idx = dir_queue.popleft()

            if rad_idx < dir_idx:
                rad_queue.append(rad_idx + n)
            else:
                dir_queue.append(dir_idx + n)

        return "Radiant" if rad_queue else "Dire"