import itertools
from pprint import pprint as pp
import numpy as np
import pandas as pd

from .acceptance_indexers import NRCAcceptanceIndexer, TextBlobAcceptanceIndexer, VADERAcceptanceIndexer, CombinedAcceptanceIndexer


def get_acceptance_indexes(post_title, comments):
    results = {}

    for acceptance_indexer_cls in [
        TextBlobAcceptanceIndexer,
        NRCAcceptanceIndexer,
        VADERAcceptanceIndexer,
        # CombinedAcceptanceIndexer,
    ]:
        try:
            # print(f"\nVariation: {acceptance_indexer_cls.__name__}\n")
            acceptance_indexer = acceptance_indexer_cls(post_title, comments)

            # Show individual Acceptance Scores
            # acceptance_scores = acceptance_indexer.get_acceptance_scores()
            # pp(acceptance_scores)

            # Get the Acceptance Index
            acceptance_index = acceptance_indexer.calculate_acceptance_index()
            # print(f"Acceptance Index: {acceptance_index:.2f}")
        except Exception as e:
            results[acceptance_indexer_cls.__name__] = str(e)
        else:
            results[acceptance_indexer_cls.__name__] = acceptance_index

    return results


def test_hyperparameters(post_title, comments, tag=None):
    results = {}
    errors = {}
    # step_size = 0.25
    step_size = 0.5
    # step_size = 1.0

    for acceptance_indexer_cls in [
        TextBlobAcceptanceIndexer,
        # NRCAcceptanceIndexer,
        VADERAcceptanceIndexer,
        # CombinedAcceptanceIndexer,
    ]:
        variation = acceptance_indexer_cls.__name__
        print(f"\nVariation: {variation}\n")
        results[variation] = []
        errors[variation] = []
        acceptance_indexer = acceptance_indexer_cls(post_title, comments)

        # Set all items to zero
        for key in acceptance_indexer.WEIGHTS:
            acceptance_indexer.WEIGHTS[key] = 0

        # Get the keys of the dictionary
        keys = list(acceptance_indexer.WEIGHTS.keys())

        # Generate all combinations of values between 0 and 1 in steps of `step_size`
        value_ranges = [np.arange(0, 1.1, step_size) for _ in range(len(keys))]
        combinations = list(itertools.product(*value_ranges))
        num_combinations = len(combinations)
        print(f"Attempting {num_combinations} combinations...")
        for i, values in enumerate(combinations):
            if i % num_combinations == 100:
                print(
                    f"Attempting {i} of {num_combinations} ({(i / num_combinations * 100)}%) of combinations..."
                )

            # Update the weights with the current combination of values
            for i, key in enumerate(keys):
                acceptance_indexer.WEIGHTS[key] = values[i]

            try:
                # Show individual Acceptance Scores
                # acceptance_scores = acceptance_indexer.get_acceptance_scores()
                # pp(acceptance_scores)

                # Get the Acceptance Index
                acceptance_index = acceptance_indexer.calculate_acceptance_index()
                # print(f"Acceptance Index: {acceptance_index:.2f}")
            except Exception as e:
                errors[variation].append(str(e))
            else:
                result = acceptance_indexer.WEIGHTS.copy()
                result["Acceptance Index"] = acceptance_index
                results[variation].append(result)

        df_results = pd.DataFrame(results[variation])
        file_name = f"{tag}_{variation}" if tag else {variation}
        df_results.to_csv(f"{file_name}.csv")

    return df_results


def get_acceptance_index_variations(title, comments, tag=None):
    comment_list = comments.split("|__|")
    results = get_acceptance_indexes(title, comment_list)
    # results = test_hyperparameters(title, comment_list, tag)
    # print('Results: ', results)

    return results


def add_acceptance_index(df):
    df = pd.concat(
        [
            df,
            df.apply(
                lambda x: get_acceptance_index_variations(
                    x["clean_title"], x["comments"]
                ),
                axis=1,
            ).apply(pd.Series),
        ],
        axis=1,
    )

    return df


if __name__ == "__main__":
    # Sample texts
    post_title = "Alien ship lands on Whitehouse lawn and makes first contact"
    print(f"Post Title: {post_title}")
    acceptance_comments = [
        "Finally, Aliens are here",
        "We better not mess this up",
        "It's real, I was there",
        # "Actually, I was just on LSD",
        # "This is so obviously fake",
        "I dislike Aliens, but they definitely landed on the Whitehouse lawn",
        "This has been confirmed",
        # "This has been debunked",
    ]
    rejection_comments = [
        "As if there are aliens. Why would they land here?",
        "Actually, I was just on LSD",
        "This is so obviously fake",
        "This has been debunked",
    ]

    # results = get_acceptance_index(post_title, comments)
    results = get_acceptance_index_variations(
        post_title, "|__|".join(acceptance_comments), "Accepted"
    )
    print("Acceptance Results:")
    pp(results)
    results = get_acceptance_index_variations(
        post_title, "|__|".join(rejection_comments), "Rejected"
    )
    print("Rejection Results:")
    pp(results)

    # import os
    # data_dir = r"/data"
    # # data_path = os.path.join(data_dir, 'merged_data_v2.csv')
    # data_path = os.path.join(data_dir, 'merged_data_v14_features.csv')
    # data = pd.read_csv(data_path)

    # df = pd.DataFrame(columns=['title', 'comments', '2_way_label'])
    # accepted_item = {
    #     'title': post_title,
    #     'comments': '|__|'.join(acceptance_comments),
    #     '2_way_label': 1,
    # }
    # rejected_item = {
    #     'title': post_title,
    #     'comments': '|__|'.join(rejection_comments),
    #     '2_way_label': 2,
    # }
    # df.append(accepted_item)
    # df.append(rejected_item)

    # # print(data)

    # # add_acceptance_index(data[:1])
    # # # add_acceptance_index(data[:10])
    # # # add_acceptance_index(data)
    # add_acceptance_index(df)
