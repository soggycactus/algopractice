""" Seat Reservation Manager """
import heapq


class SeatManager:
    """
    Manages n number of seat reservations
    """

    def __init__(self, n: int):
        self.unreserved_seats = []
        self.reserved_seats = []

        for i in range(1, n + 1):
            self.unreserved_seats.append(i)

        heapq.heapify(self.unreserved_seats)

    def reserve(self) -> int:
        """
        reserves the lowest available seat
        """
        seat = heapq.heappop(self.unreserved_seats)
        self.reserved_seats.append(seat)
        return seat

    def unreserve(self, seat_number: int) -> None:
        """
        returns seat_number to the unreserved_seats pool
        """
        self.reserved_seats.remove(seat_number)
        heapq.heappush(self.unreserved_seats, seat_number)


def main():
    """
    Entrypoint of the program
    """
    number_of_seats = 5
    obj = SeatManager(number_of_seats)
    seat1 = obj.reserve()
    obj.unreserve(seat1)
    obj.reserve()
    obj.reserve()
    obj.unreserve(2)
    obj.reserve()
    obj.reserve()
    obj.reserve()
    obj.unreserve(3)

    print(obj.reserved_seats)
    print(obj.unreserved_seats)


if __name__ == "__main__":
    main()
