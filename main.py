import pandas as pd


rating_diff = 0
rank_diff = 0
rating_limits = [0, 3000]
rank_limits = [0, 39]
unique_matches_data = []
df = pd.read_excel('tournament_35993173.xlsx')
tours = [1, 2, 3, 4, 5]
dublicate_count = 0
def unique_matches(dataframe, b) -> int:
    for row in dataframe.iterrows():
        player_a = row[1]['№']
        for tour in tours:
            match = row[1][tour]
            player_b = int(match[:-1])
            match_res = match[-1]

            for pl in tours:
                if pl == tour:
                    pass
                else:
                    match = row[1][pl]
                    player_c = int(match[:-1])
                    if player_c == player_b:
                        print("REALLY DUBLIC")

            if [player_a, player_b] and [player_b, player_a] not in unique_matches_data:
                if match_res == '+':
                    unique_matches_data.append([player_a, player_b])
                    print([player_a, player_b])
                elif match_res == '-':
                    unique_matches_data.append([player_b, player_a])
                    print([player_b, player_a])
            else:
                b = b + 1
                # print(f"DUBLICATE {b}!")



def classified_matches_rating(rating_difference) -> int:
    pass

def matches_total(dataframe) -> int:
    pass

def classified_matches_percent(dataframe) -> int:
    pass

def high_win(dataframe) -> int:
    pass

def low_win(dataframe) -> int:
    pass

def failed_matches(dataframe) -> int:
    pass


unique_matches(df, dublicate_count)
print(len(unique_matches_data))
print(dublicate_count)
def make_unique_array(arrays):
    unique_set = set()
    for arr in arrays:
        unique_set.add(tuple(arr))
    return [list(arr) for arr in unique_set]

# Example usage:
arrays = [[1, 2], [2, 3], [1, 2], [3, 4], [2, 3]]  # Example array of arrays
unique_arrays = make_unique_array(unique_matches_data)
print(len(unique_arrays))

