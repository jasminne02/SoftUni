from project.software.software import Software


class Hardware:
    NOT_ENOUGH_RESOURCES_ERROR_MESSAGE = "Software cannot be installed"

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.__capacity_used = 0
        self.__memory_used = 0

    def install(self, software: Software):
        self.__validate_installation_is_possible(software)
        self.__install_software(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.__uninstall_software(software)

    # PRIVATE METHODS #
    def __install_software(self, software: Software):
        self.__memory_used += software.memory_consumption
        self.__capacity_used += software.capacity_consumption
        self.software_components.append(software)

    def __uninstall_software(self, software: Software):
        self.__memory_used -= software.memory_consumption
        self.__capacity_used -= software.capacity_consumption
        self.software_components.remove(software)

    def __validate_installation_is_possible(self, software: Software):
        if not self.__has_enough_memory(software) or not self.__has_enough_capacity(software):
            raise Exception(self.NOT_ENOUGH_RESOURCES_ERROR_MESSAGE)

    def __has_enough_capacity(self, software: Software):
        if software.capacity_consumption + self.__capacity_used > self.capacity:
            return False
        return True

    def __has_enough_memory(self, software: Software):
        if software.memory_consumption + self.__memory_used > self.memory:
            return False
        return True
