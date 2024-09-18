class Solution:
    def countSegments(self, s: str) -> int:
        segments = s.split(' ')

        filteredSegments = list(filter(lambda x: x != '', segments))

        return len(filteredSegments)