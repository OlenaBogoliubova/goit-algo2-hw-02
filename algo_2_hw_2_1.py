from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера
    """
    jobs = sorted(print_jobs, key=lambda x: (x['priority'], x['print_time']))
    selected_jobs = []
    total_time = 0
    total_volume = 0
    count = 0
    
    for job in jobs:
        if count < constraints['max_items'] and total_volume + job['volume'] <= constraints['max_volume']:
            selected_jobs.append(job['id'])
            total_time += job['print_time']
            total_volume += job['volume']
            count += 1
    
    return {
        "print_order": selected_jobs,
        "total_time": total_time
    }

# Тестування
if __name__ == "__main__":
    def test_printing_optimization():
        test_cases = [
            ([{"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
              {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
              {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}], "Тест 1 (однаковий пріоритет)"),
            ([{"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
              {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
              {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}], "Тест 2 (різні пріоритети)"),
            ([{"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
              {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
              {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}], "Тест 3 (перевищення обмежень)")
        ]
        constraints = {"max_volume": 300, "max_items": 2}
        
        for test, name in test_cases:
            print(f"{name}:")
            result = optimize_printing(test, constraints)
            print(f"Порядок друку: {result['print_order']}")
            print(f"Загальний час: {result['total_time']} хвилин\n")
    
    test_printing_optimization()