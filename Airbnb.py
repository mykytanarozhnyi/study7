class Rental:
    flats = list()

    def __init__(self, name, meters, price, date):
        self.name = name
        self.meters = meters
        self.price = price
        self.date = date
        Rental.flats.append(self)

    def __str__(self):  # Перевизначаємо метод __str__ для виведення опису помешкання
        return f"This is {self.name} has {self.meters} meters, and costs {self.price}, available from {self.date}"

class Booking:
    bookings = list()

    def __init__(self, name, start_date, end_date, rental):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.rental = rental
        self.bookings.append(self)

    @classmethod
    def book(cls, name, start_date, end_date, rental):
        for booking in cls.bookings:
            if booking.rental == rental:
                if (booking.end_date < start_date or booking.start_date > end_date):
                    continue
                else:
                    print("Rental is already booked")
                    return
        cls(name, start_date, end_date, rental)
        print("Booking successful!")

    @staticmethod
    def check_availability(start_date, end_date, rental):
        for booking in Booking.bookings:
            if booking.rental == rental:
                if (booking.end_date < start_date or booking.start_date > end_date):
                    continue
                else:
                    return False
        return True

if __name__ == "__main__":
    flat1 = Rental("Amazing flat", "58", "160$", "2024-4-20")
    flat2 = Rental("Dworzec Centralny flat", "25", "110$", "2024-4-27")

    # Виводимо інформацію про всі доступні помешкання
    print("\nAvailable flats:")
    for flat in Rental.flats:
        print(flat)

    # Бронюємо помешкання
    Booking.book("John", "2024-4-21", "2024-4-25", flat1)
    Booking.book("Alice", "2024-4-24", "2024-4-30", flat2)
    Booking.book("Hike","2024-3-25","2024-5-26",flat1)
    Booking.book("Mykyta","2024-5-1","2024-5-7",flat2)

