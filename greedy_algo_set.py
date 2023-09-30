# Данная программа ищет минимальный набор станций, который будет покрывать все заданные штаты.
# Программа реализует жадный алгоритм с хорошим, но не оптимальным решением.

# Фукция, покрывающая штаты минимальным набором станций.
def cover_states_by_stations(st_needed: set(), sts: {}):
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


# Полный список штатов
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Список станций, из которого будет выбираться покрытие
stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ca"]),
    "kfive": set(["ca", "az"])
}

print("Минимальный набор станций, покрывающий все заданные штаты:", cover_states_by_stations(states_needed, stations))


