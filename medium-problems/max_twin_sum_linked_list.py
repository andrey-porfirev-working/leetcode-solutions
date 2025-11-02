class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        nums = []
        while current:
            nums.append(current.val)
            current = current.next
        left, right = 0, len(nums)-1
        twin_sum_max = 0
        while left < right:
            twin_sum_max = max(nums[left] + nums[right], twin_sum_max)
            left += 1
            right -= 1
        return twin_sum_max

    def pairSum_v_2(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        max_sum = 0
        first = head
        second = prev

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum