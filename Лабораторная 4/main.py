from __future__ import annotations


class Employee:
    """
    Базовый класс сотрудника.

    Атрибуты:
        name: Имя сотрудника.
        salary: Зарплата сотрудника.
    """

    def __init__(self, name: str, salary: float) -> None:
        """
        Создаёт сотрудника.

        Args:
            name: Имя сотрудника.
            salary: Зарплата сотрудника.
        """
        self.name: str = name
        self.salary: float = salary

        # _hours_worked сделан непубличным, чтобы нельзя было менять часы напрямую из вне.
        # Часы должны меняться через метод add_hours.
        self._hours_worked: float = 0.0

    def __str__(self) -> str:
        """
        Возвращает строку для пользователя.
        """
        return f"Employee(name={self.name}, salary={self.salary})"

    def __repr__(self) -> str:
        """
        Возвращает строку для отладки.
        """
        return f"Employee(name={self.name!r}, salary={self.salary!r}, hours={self._hours_worked!r})"

    def add_hours(self, hours: float) -> None:
        """
        Добавляет отработанные часы.

        Args:
            hours: Количество часов.

        Raises:
            ValueError: Если передано отрицательное число часов.
        """
        if hours < 0:
            raise ValueError("hours must be >= 0")
        self._hours_worked += hours

    def calculate_bonus(self) -> float:
        """
        Считает бонус сотрудника.

        Returns:
            Размер бонуса.
        """
        return self.salary * 0.10

    def get_report_line(self) -> str:
        """
        Делает строку для отчёта.

        Returns:
            Строка отчёта.
        """
        return f"{self.name}: salary={self.salary}, hours={self._hours_worked}"


class Manager(Employee):
    """
    Дочерний класс менеджера.

    Отличие: менеджер хранит отдел и количество людей в команде.
    """

    def __init__(self, name: str, salary: float, department: str, team_size: int) -> None:
        """
        Создаёт менеджера (расширяет конструктор базового класса).

        Args:
            name: Имя менеджера.
            salary: Зарплата менеджера.
            department: Отдел.
            team_size: Размер команды.
        """
        super().__init__(name, salary)
        self.department: str = department
        self.team_size: int = team_size

    def __str__(self) -> str:
        """
        Возвращает строку для пользователя.
        """
        return f"Manager(name={self.name}, dept={self.department}, team={self.team_size})"

    def __repr__(self) -> str:
        """
        Возвращает строку для отладки.
        """
        return (
            "Manager("
            f"name={self.name!r}, salary={self.salary!r}, department={self.department!r}, "
            f"team_size={self.team_size!r}, hours={self._hours_worked!r}"
            ")"
        )

    # Унаследованный метод: add_hours() НЕ переопределяем, просто используем как есть.

    def calculate_bonus(self) -> float:
        """
        Перегружает метод calculate_bonus().

        Причина перегрузки: у менеджера бонус зависит от размера команды,
        потому что у него больше ответственности.

        Returns:
            Размер бонуса менеджера.
        """
        base_bonus: float = super().calculate_bonus()
        extra: float = self.salary * 0.02 * self.team_size
        return base_bonus + extra


if __name__ == "__main__":
    e: Employee = Employee("Ivan", 50000.0)
    e.add_hours(8.0)
    print(e)
    print(repr(e))
    print("bonus:", e.calculate_bonus())
    print(e.get_report_line())

    m: Manager = Manager("Olga", 80000.0, "IT", 3)
    m.add_hours(6.0)  # унаследованный метод
    print(m)
    print(repr(m))
    print("bonus:", m.calculate_bonus())  # перегруженный метод
    print(m.get_report_line())
