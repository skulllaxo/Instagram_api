import pandas as pd
import Dataframes as dt



class CampaignsInstagram:

    def __init__(self,id,post_id,campaign_name,reach,impressions,spend,date_start,date_stop):
        self.id = id
        self.post_id = post_id
        self.campaign_name = campaign_name
        self.reach = reach
        self.impressions = impressions
        self.spend = spend
        self.date_start = date_start
        self.date_stop = date_stop
        columns = ('id','post_id','campaign_name','reach','impressions','spend','date_start','date_stop')


        # export_camp = dt.DataFrames(columns=columns,campaign_data=lista)





        # df = pd.DataFrame([lista],columns=columns)
        # df = pd.DataFrame(columns=columns)

