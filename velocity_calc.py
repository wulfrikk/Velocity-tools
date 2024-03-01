def calculate_velocity(distance: float, angle: float) -> float:
    """
    Calculates the velocity of an object fired from a cannon based on the given distance and launch angle.

    Parameters:
    - distance: float
        The distance the object is fired.
    - angle: float
        The launch angle of the object in degrees.

    Returns:
    - float:
        The calculated velocity of the object.

    Formula used:
    velocity = sqrt(distance * g / sin(2 * angle)), where g is the acceleration due to gravity (9.81 m/s^2).

    Raises:
    - ValueError:
        If the distance is negative or angle is not within the range [0, 90] degrees.
    """

    import math

    # Constants
    g = 9.81  # Acceleration due to gravity in m/s^2

    # Validating input parameters
    if distance < 0:
        raise ValueError("Distance cannot be negative.")
    if angle < 0 or angle > 90:
        raise ValueError("Angle must be between 0 and 90 degrees.")

    # Calculating the velocity using the formula
    velocity = math.sqrt(distance * g / math.sin(math.radians(2 * angle)))

    return velocity

# Example of using the calculate_velocity function:

try:
    distance = 100  # meters
    launch_angle = 45  # degrees
    velocity = calculate_velocity(distance, launch_angle)
    print(f"The velocity of the object fired from a cannon at a distance of {distance} meters and launch angle of {launch_angle} degrees is {velocity} m/s.")
except ValueError as e:
    print(f"Error: {e}")
