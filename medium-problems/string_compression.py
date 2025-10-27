class Solution:
    def compress(self, chars: list[str]) -> int:
        if not chars:
            return 0
        write_idx = 0
        read_idx = 0
        while read_idx < len(chars):
            current_char = chars[read_idx]
            count = 0
            while read_idx < len(chars) and chars[read_idx] == current_char:
                read_idx += 1
                count += 1
            chars[write_idx] = current_char
            write_idx += 1
            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1
        return write_idx
    def compress_v_2(self, chars: list[str]) -> int:
        n = len(chars)
        write = 0
        count = 1
        for i in range(1, n + 1):
            if i == n or chars[i] != chars[i - 1]:
                chars[write] = chars[i - 1]
                write += 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                count = 1
            else:
                count += 1
        return write