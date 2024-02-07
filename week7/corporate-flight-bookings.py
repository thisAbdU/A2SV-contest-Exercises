class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        booking = [0 for i in range(n + 1)]
        for i in range(len(bookings)):
            booking[bookings[i][0] - 1] += bookings[i][2]
            booking[(bookings[i][1])] -= bookings[i][2]
        for i in range(1, len(booking)):
            booking[i] += booking[i - 1]
        booking.pop()
        return booking