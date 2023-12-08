import re
import numpy as np

def load_data(file_path):
    with open(file_path) as file:
        return [line.split('\n')[0] for line in file]

def extract_game_ids(data):
    return [line.split('Game')[1].split(':')[0] for line in data]

def extract_games(data):
    return [re.split(';', line.split(':')[1]) for line in data]

def get_max_game_length(data):
    games = extract_games(data)
    max_game_length = 0
    return max([len(game) for game in games])

def compile_data_into_array(data):
    max_game_length = get_max_game_length(data)
    number_of_games = len(extract_game_ids(data))
    game_results_array = np.array((number_of_games, max_game_length * 3))
    game_ids = extract_game_ids(data)
    games = extract_games(data)
    for game_id, game in game_ids, games:
        for draw in game:
            color_distribution = re.split(', ', draw)
            for color in color_distribution:
                if 'red' in color:
                    game_results_array[game_id, int(color.split('red')[0])
            game_results_array[game, ]

data = load_data('input.txt')
print(get_max_game_length(data))
