class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # calculate the distance between two points
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # calculate the distance from the origin to the target
        target_distance = distance([0, 0], target)

        # calculate the minimum distance from each ghost to the target
        for ghost in ghosts:
            ghost_distance = distance(ghost, target)
            # Check if the ghost can reach the target before you
            if ghost_distance <= target_distance:
                return False

        return True
