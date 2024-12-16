import json
import argparse

def generate_test_data(size):
    data = {
        "input_size": size,
        "content": [i for i in range(size)]
    }
    with open("test_data.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, required=True, help='Size of the test data')
    args = parser.parse_args()

    generate_test_data(args.size)
