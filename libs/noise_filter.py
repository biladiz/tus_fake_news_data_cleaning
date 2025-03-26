import pandas as pd

# TODO: Consider applying length filter to each comment

class NoiseFilter:

    def __init__(self, df, config):
        self.df = df

        # Default configs
        self.config = {
            'MinLengths': {
                'title': 0,
                'comments': 0
            },
            'ExcludeImages': False,
            'TextFilters': {
                # 'subreddit': '',
            },

        }
        self.config.update(config) # Override default configs


    def filter_by_length(self):
        """
        Filter the Dataset to include only rows where the specified column(s)
        have a number of words of at least the specified length min_length.
        """
        for col_name, min_length in self.config['MinLengths'].items():
            if col_name not in self.df.columns:
                raise ValueError(f"Column '{col_name}' does not exist in the Dataset.")
        
            # Filter rows based on word count
            if min_length >= 0:
                self.df = self.df[self.df[col_name].str.split().str.len() > min_length]

    def remove_images(self):
        """
        Remove rows where the 'IsImage' column is set to True.
        """
        if 'hasImage' not in self.df.columns:
            raise ValueError("Column 'IsImage' does not exist in the Dataset.")
        
        # Filter out rows where IsImage is True
        self.df = self.df[self.df['hasImage'] != True]

    
    def filter_by_substring(self):
        """
        Limit dataset to rows where the specified columns include the specified substring(s).

        """
        for col_name, substrings in self.config['TextFilters'].items():
            if col_name not in self.df.columns:
                raise ValueError(f"Column '{col_name}' does not exist in the Dataset.")

            if isinstance(substrings, str):
                substrings = [substrings]

            pattern = '|'.join(substrings)
            self.df = self.df[self.df[col_name].str.contains(pattern, na=False)]


    def apply(self):
        """
        Apply filters based on the input configuration.
        """
        if self.config.get('MinLengths', False):
            self.filter_by_length()
        
        if self.config.get('ExcludeImages', False):
            self.remove_images()
        
        if self.config.get('TextFilters', False):
            self.filter_by_substring()

        return self.df



if __name__ == '__main__':

    test_data = {
        'title': ['Title 1', 'This is some text', 'This is yet another post', 'Another title'],
        'comments': ['This is an interesting comment', 'A very short comment', 'Foo Bar', 'Bla bla'],
        'hasImage': [True, False, True, False],
        'subreddit': ['foo', 'bar', 'bar', 'foo']
    }

    df = pd.DataFrame(test_data)
    print(f"Full data frame:\n{df}")


    config = {
        'MinLengths': {
            'title': 0,
            'comments': 0
        },
        'ExcludeImages': False,
        'TextFilters': {
            'subreddit': '',
        },
    }

    noise_filter = NoiseFilter(df, config)
    print(f"Filter applied with all filters disabled:\n{noise_filter.apply()}")


    config = {
        'MinLengths': {
            'title': 0,
            'comments': 3
        },
        'ExcludeImages': False,
        'TextFilters': {
            'subreddit': '',
        },
    }
    noise_filter = NoiseFilter(df, config)
    print(f"Filtered comments <= 3 words:\n{noise_filter.apply()}")


    config = {
        'MinLengths': {
            'title': 3,
            'comments': 3
        },
        'ExcludeImages': False,
        'TextFilters': {
            'subreddit': '',
        },
    }
    noise_filter = NoiseFilter(df, config)
    print(f"Filtered title and comments <= 3 words:\n{noise_filter.apply()}")


    config = {
        'ExcludeImages': True,
    }
    noise_filter = NoiseFilter(df, config)
    print(f"Filtered images:\n{noise_filter.apply()}")


    config = {
        'TextFilters': {
            'subreddit': 'foo',
        },
    }
    noise_filter = NoiseFilter(df, config)
    print(f"Filtered subreddits:\n{noise_filter.apply()}")


    config = {
        'TextFilters': {
            'subreddit': ['oo', 'bar'],
        },
    }
    noise_filter = NoiseFilter(df, config)
    print(f"Filtered subreddits:\n{noise_filter.apply()}")
