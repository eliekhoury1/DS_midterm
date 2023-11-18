def calculate_area_of_circle(radius):
    return 3.14 * radius ** 2

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    radius = 5
    rectangle_length, rectangle_width = 4, 6
    triangle_base, triangle_height = 3, 8
    celsius_temperature = 22
    number_to_check = 17

    area_circle = calculate_area_of_circle(radius)
    area_rectangle = calculate_area_of_rectangle(rectangle_length, rectangle_width)
    area_triangle = calculate_area_of_triangle(triangle_base, triangle_height)
    fahrenheit_temperature = convert_celsius_to_fahrenheit(celsius_temperature)
    is_prime = is_prime_number(number_to_check)

    print(f"Area of circle with radius {radius}: {area_circle}")
    print(f"Area of rectangle with length {rectangle_length} and width {rectangle_width}: {area_rectangle}")
    print(f"Area of triangle with base {triangle_base} and height {triangle_height}: {area_triangle}")
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")
    print(f"{number_to_check} is a prime number: {is_prime}")

if __name__ == "__main__":
    main()
