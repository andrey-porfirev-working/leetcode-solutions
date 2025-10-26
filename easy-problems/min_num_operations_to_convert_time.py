class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        step = 0
        def convertToNum(time: str) -> int:
            hours = int(time[0])*10 if time[0] != "0" else 0
            hours += int(time[1])
            minutes_all = 60*hours if hours > 0 else 0
            minutes = int(time[3:]) if time[3] != "0" else int(time[4])
            minutes_all += minutes
            return minutes_all
        current = convertToNum(current)
        correct = convertToNum(correct)
        diff = correct - current
        aval_steps = [60, 15, 5, 1]
        for val in aval_steps:
            while diff >= val:
                diff -= val
                step += 1
        return step

    def convertTime_v_2(self, current: str, correct: str) -> int:
        current_minutes = int(current[:2]) * 60 + int(current[3:])
        correct_minutes = int(correct[:2]) * 60 + int(correct[3:])
        diff = correct_minutes - current_minutes
        if diff < 0:
            diff += 1440
        operations = 0
        for step in [60, 15, 5, 1]:
            operations += diff // step
            diff %= step

        return operations