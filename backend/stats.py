import numpy as np


def preprocess(data):
    return np.array(data).T


def create_histogram(data):
    histogram = np.histogram(data)

    return [{
            'uv': int(height), 
            'name': f'{round(histogram[1][idx], 2)} - {round(histogram[1][idx+1], 2)}'
        }
        for idx, height in enumerate(histogram[0])
    ]


def create_numerical(data):
    return {
        "median": np.median(data, axis=1).tolist(),
        "mean": np.mean(data, axis=1).tolist(),
        "std": np.std(data, axis=1).tolist(),
    }


def generate_json(data, names):
    data = preprocess(data)
    return {
        "feature_names": names,
        "tabular": create_numerical(data),
        "graphs": {
            "histogram": {name:create_histogram(column) for name, column in zip(names, data)} 
                #{"all":create_histogram(data)}, ???
        },
    }