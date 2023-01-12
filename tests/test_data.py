from datetime import time, date

# TODO: Think about generating this dynamically.
# Would that duplicate the logic and bring in more risk?
# Is this a bit manual but easier to ensure accuracy?
test_data = [
    {"Date": date(2023, 1, 1), "Time": time(0, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(0, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(1, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(1, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(2, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(2, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(3, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(3, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(4, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(4, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(5, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(5, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(6, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(6, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(7, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(7, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(8, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(8, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(9, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(9, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(10, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(10, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(11, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(11, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(12, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(12, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(13, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(13, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(14, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(14, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(15, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(15, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(16, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(16, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(17, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(17, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(18, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(18, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(19, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(19, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(20, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(20, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(21, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(21, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(22, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(22, 30, 0)},
    {"Date": date(2023, 1, 1), "Time": time(23, 0, 0)},
    {"Date": date(2023, 1, 1), "Time": time(23, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(0, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(0, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(1, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(1, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(2, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(2, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(3, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(3, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(4, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(4, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(5, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(5, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(6, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(6, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(7, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(7, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(8, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(8, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(9, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(9, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(10, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(10, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(11, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(11, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(12, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(12, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(13, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(13, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(14, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(14, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(15, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(15, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(16, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(16, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(17, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(17, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(18, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(18, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(19, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(19, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(20, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(20, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(21, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(21, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(22, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(22, 30, 0)},
    {"Date": date(2023, 1, 2), "Time": time(23, 0, 0)},
    {"Date": date(2023, 1, 2), "Time": time(23, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(0, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(0, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(1, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(1, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(2, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(2, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(3, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(3, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(4, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(4, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(5, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(5, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(6, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(6, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(7, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(7, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(8, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(8, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(9, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(9, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(10, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(10, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(11, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(11, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(12, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(12, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(13, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(13, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(14, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(14, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(15, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(15, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(16, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(16, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(17, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(17, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(18, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(18, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(19, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(19, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(20, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(20, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(21, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(21, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(22, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(22, 30, 0)},
    {"Date": date(2023, 1, 3), "Time": time(23, 0, 0)},
    {"Date": date(2023, 1, 3), "Time": time(23, 30, 0)},
]
