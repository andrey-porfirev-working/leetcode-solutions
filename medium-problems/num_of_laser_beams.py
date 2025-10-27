class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices_up = 0
        devices_to_connect = 0
        beams = 0
        for row in bank:
            if row.count("1") > 0:
                devices_to_connect = row.count("1")
                beams += devices_up * devices_to_connect
                devices_up = devices_to_connect
        return beams

    def numberOfBeams_v_2(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            devices = row.count('1')
            if devices > 0:
                total += prev * devices
                prev = devices

        return total
