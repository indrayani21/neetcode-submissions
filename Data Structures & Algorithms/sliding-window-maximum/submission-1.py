class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices out of window
            if q and q[0] <= i - k:
                q.popleft()

            # Remove smaller values from the end
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Append max once window of size k is formed
            if i >= k - 1:
                result.append(nums[q[0]])

        return result