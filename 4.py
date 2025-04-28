from typing import List, Optional

class MusicTool:
    tool_type: str = "Typical"
    country_of_origin: str = "Undetermined"

    def __init__(self, model: str, maker: str, production_year: int, build_material: str, uses_electricity: bool) -> None:
        self.model = model
        self.maker = maker
        self.production_year = production_year
        self.build_material = build_material
        self.uses_electricity = uses_electricity

    def __str__(self) -> str:
        return f"{self.model} от {self.maker} ({self.production_year} г.)"

    def perform(self, melody: Optional[List[str]] = None) -> None:
        if melody:
            print(f"Исполнение мелодии {', '.join(melody)} на {self.model}")
        else:
            print(f"Исполнение на {self.model}")

    def calculate_age(self, current_year: int) -> int:
        return current_year - self.production_year

    def is_vintage(self) -> bool:
        return self.calculate_age(2024) > 100

    def update_maker(self, new_maker: str) -> None:
        self.maker = new_maker

electric_guitar = MusicTool("Электрогитара", "Gibson", 2015, "Махагони", True)
upright_piano = MusicTool("Пианино", "Petrof", 1995, "Ель", False)
cello = MusicTool("Виолончель", "Amati", 1680, "Клен", False)

print(electric_guitar)
print(upright_piano.calculate_age(2024))
print(cello.is_vintage())
electric_guitar.perform(["Am", "G", "C"])
upright_piano.update_maker("Blüthner")
print(upright_piano)
