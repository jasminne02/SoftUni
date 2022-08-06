from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []
    HARDWARE_NOT_EXIST_ERROR_MESSAGE = "Hardware does not exist"
    SOFTWARE_NOT_EXIST_ERROR_MESSAGE = "Software does not exist"

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__get_hardware_by_name(hardware_name)
        System.__validate_hardware_exists(hardware)
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__get_hardware_by_name(hardware_name)
        System.__validate_hardware_exists(hardware)
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.__get_hardware_by_name(hardware_name)
        software = System.__get_software_by_name(software_name)
        System.__validate_both_exist(software, hardware)
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        software_memory_consumption = 0
        hardware_memory_consumption = 0
        software_capacity_taken = 0
        hardware_total_capacity = 0

        for software in System._software:
            software_memory_consumption += software.memory_consumption
            software_capacity_taken += software.capacity_consumption

        for hardware in System._hardware:
            hardware_memory_consumption += hardware.memory
            hardware_total_capacity += hardware.capacity

        return f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {software_memory_consumption} / " \
                 f"{hardware_memory_consumption}\n" \
                 f"Total Capacity Taken: {software_capacity_taken} / " \
                 f"{hardware_total_capacity}"

    @staticmethod
    def system_split():
        result = ""

        for hardware in System._hardware:
            express_software_number = 0
            light_software_number = 0
            software_total_memory_used = 0
            software_total_capacity_used = 0
            software_names = []

            for software in hardware.software_components:
                if software.software_type == "Express":
                    express_software_number += 1
                elif software.software_type == "Light":
                    light_software_number += 1
                software_total_memory_used += software.memory_consumption
                software_total_capacity_used += software.capacity_consumption
                software_names.append(software.name)

            if len(software_names) == 0:
                software_names = None

            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {express_software_number}\n" \
                      f"Light Software Components: {light_software_number}\n" \
                      f"Memory Usage: {software_total_memory_used} / {hardware.memory}\n" \
                      f"Capacity Usage: {software_total_capacity_used} / {hardware.capacity}\n" \
                      f"Type: {hardware.hardware_type}\n" \
                      f"Software Components: {', '.join(software_names)}\n"

        return result

    # PRIVATE METHODS #
    @classmethod
    def __get_hardware_by_name(cls, hardware_name: str):
        hardware = [h for h in cls._hardware if h.name == hardware_name]
        if hardware is None:
            return hardware
        return hardware[0]

    @classmethod
    def __get_software_by_name(cls, software_name: str):
        software = [s for s in cls._software if s.name == software_name]
        if software is None:
            return software
        return software[0]

    @staticmethod
    def __validate_hardware_exists(hardware: Hardware):
        if hardware is None:
            return System.HARDWARE_NOT_EXIST_ERROR_MESSAGE

    @staticmethod
    def __validate_software_exists(software: Software):
        if software is None:
            return System.SOFTWARE_NOT_EXIST_ERROR_MESSAGE

    @staticmethod
    def __validate_both_exist(software: Software, hardware: Hardware):
        if System.__validate_hardware_exists(hardware) and System.__validate_software_exists(software):
            return "Some of the components do not exist"
