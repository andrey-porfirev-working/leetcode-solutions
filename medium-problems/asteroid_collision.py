class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        pointer = len(asteroids) - 1
        while pointer > 0:
            if asteroids[pointer] > 0:
                pointer -= 1
            else:
                if asteroids[pointer-1] < 0:
                    pointer -= 1
                else:
                    if asteroids[pointer] + asteroids[pointer-1] > 0:
                        asteroids.pop(pointer)
                    elif asteroids[pointer] + asteroids[pointer-1] < 0:
                        asteroids.pop(pointer-1)
                        pointer -= 1
                    else:
                        asteroids.pop(pointer)
                        asteroids.pop(pointer-1)
                        pointer -= 1
            if pointer == len(asteroids):
                pointer -= 1
        return asteroids

    def asteroidCollision_v_2(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0 or not stack:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] < -asteroid:
                        stack.pop()
                        continue
                    elif stack[-1] == -asteroid:
                        stack.pop()
                    break
                else:
                    stack.append(asteroid)

        return stack
