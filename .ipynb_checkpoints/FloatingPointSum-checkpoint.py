#!/usr/bin/env python3
class FloatingPointSum:
    def __init__(self) -> None:
        self.sum = 0

    def get_float_input(self):
        for i in range(2):  # Two chances to enter a proper value
            try:
                value = float(input("Enter a floating-point value: "))
                return value
            except Exception as e:
                print("Invalid input. Please enter a valid floating-point value.")

        print("Exceeded maximum attempts. Quitting input.")
        return None

    def perform_sum(self):
        while True:
            value = self.get_float_input()
            if value is None:
                break

            self.sum += value

        print("Sum of entered values:", self.sum)

# Example usage
if __name__ == "__main__":
    floating_point_sum_instance = FloatingPointSum()
    floating_point_sum_instance.perform_sum()
