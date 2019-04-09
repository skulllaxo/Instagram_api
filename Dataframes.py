import pandas as pd
class DataFrames:

        def post(csv_file='Post.csv'):
                df = pd.read_csv(str(csv_file),sep='|')
                return df

        def comments(csv_file = 'comments.csv'):
                df = pd.read_csv(str(csv_file),sep='|')
                return df

        def insights(csv_file = 'Insights.csv'):
                df = pd.read_csv(str(csv_file), sep='|')
                return df


        def campaigns(csv_file = 'Campaigns.csv'):
                df = pd.read_csv(str(csv_file), sep='|')
                return df

















