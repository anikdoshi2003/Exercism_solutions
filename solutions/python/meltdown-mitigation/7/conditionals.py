"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency bands:
      - green  -> efficiency of 80% or more
      - orange -> efficiency of less than 80% but at least 60%
      - red    -> efficiency below 60%, but still 30% or more
      - black  -> less than 30% efficient

    Percentage value = (generated power / theoretical max power) * 100,
    where generated power = voltage * current.
    """
    if theoretical_max_power == 0:
        raise ValueError("theoretical_max_power must be non-zero")

    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power) * 100

    if percentage_value >= 80:
        return "green"
    if 60 <= percentage_value < 80:
        return "orange"
    if 30 <= percentage_value < 60:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    Categories:
      - 'LOW'    -> temperature * neutrons per second < 90% of threshold
      - 'NORMAL' -> within ±10% of threshold (i.e., between 90% and 110% inclusive)
      - 'DANGER' -> outside the above ranges
    """
    reactor_output = temperature * neutrons_produced_per_second
    lower = 0.9 * threshold
    upper = 1.1 * threshold

    if reactor_output < lower:
        return "LOW"
    if lower <= reactor_output <= upper:
        return "NORMAL"
    return "DANGER"  # no-else-return