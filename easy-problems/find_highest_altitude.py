class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max = 0
        altitudes = [0]
        for g in gain:
            altitudes.append(altitudes[-1]+g)
            if max < altitudes[-1]:
                max = altitudes[-1]
        return max

    def largestAltitude_v_2(self, gain: list[int]) -> int:
        max_altitude = 0
        current_altitude = 0

        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude