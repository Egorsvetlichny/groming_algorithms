# Данная программа ищет минимальный набор станций, который будет покрывать все заданные штаты.
# Программа реализует жадный алгоритм с хорошим, но не оптимальным решением.

# Функция, покрывающая штаты минимальным набором станций.
def cover_states(st_needed: set, sts: dict):
    # Хранение итогового набора станций
    final_station = set()

    while st_needed:
        best_station = None
        states_covered = set()

        for station, states in sts.items():
            covered = st_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        st_needed -= states_covered
        final_station.add(best_station)

    return final_station


if __name__ == '__main__':
    # Полный список штатов
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    # Список станций, из которого будет выбираться покрытие
    stations = {
        "k_one": {"id", "nv", "ut"},
        "k_two": {"wa", "id", "mt"},
        "k_three": {"or", "nv", "ca"},
        "k_four": {"nv", "ca"},
        "k_five": {"ca", "or", "az"}
    }

    print("Минимальный набор станций, покрывающий все заданные штаты:", cover_states(states_needed, stations))
