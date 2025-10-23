class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pointer = 1
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False if n > 0 else True
            else:
                return True if n <= 1 else False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
        while n > 0:
            if pointer == (len(flowerbed)-1):
                break
            if flowerbed[pointer-1] == 0 and flowerbed[pointer] == 0 and flowerbed[pointer+1] == 0:
                flowerbed[pointer] = 1
                n -= 1
            pointer += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        if n <= 0:
            return True
        else:
            return False

    def canPlaceFlowers_v_2(flowerbed, n):
        count = 0
        length = len(flowerbed)

        for i in range(length):
            # Проверяем, можно ли посадить цветок в текущую позицию
            if flowerbed[i] == 0:  # позиция пуста
                # Проверяем соседние позиции (если они существуют)
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                # Если обе соседние позиции пусты, сажаем цветок
                if empty_left and empty_right:
                    flowerbed[i] = 1  # сажаем цветок
                    count += 1

                    # Если посадили достаточно цветов, возвращаем True
                    if count >= n:
                        return True

        return count >= n