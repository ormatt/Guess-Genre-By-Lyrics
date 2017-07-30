import json


def build(genres_tree_path):
    with open(genres_tree_path, 'r') as reader:
        genres_subgenres_dict = json.load(reader)

        genres_tree = {}
        for genre, subgenres_list in genres_subgenres_dict.iteritems():
            for subgenre in subgenres_list:
                genres_tree[subgenre] = genre

        all_genres_list = genres_tree.keys()
        return genres_tree, all_genres_list
