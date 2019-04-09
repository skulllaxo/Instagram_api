import os
import Comments as cmm
import datetime
import pandas as pd
import Page_instagram as pi
import Insights as ins
import Dataframes




class Post:


    def __init__(self,id,like_count,data_comments,comment_count,graph,thumb_url,caption):
        self.id = id
        self.like_count = like_count
        self.data_comments = data_comments
        self.comment_count = comment_count
        self.graph = graph
        self.thumb_url = thumb_url
        self.caption = caption












    def dataframecomments(self):
        df_comments = pd.DataFrame()
        if self.data_comments != 'null':
            comment_list = self.data_comments['data']
            for cm in comment_list:
                id_comment = cm['id']
                text_comment = cm['text']
                complete_date = cm['timestamp']
                year = int(complete_date[0:4])
                month = int(complete_date[5:7])
                day = int(complete_date[8:10])
                hour = int(complete_date[11:13])
                minute = int(complete_date[14:16])
                second = int(complete_date[17:19])
                real_date = datetime.datetime(year,month,day,hour,minute,second)
                comment = cmm.Comments(id_comment=id_comment,date_comment=real_date,text_comment=text_comment,post_id=self.id,thumb_url = self.thumb_url,caption = self.caption)

                df_comments = df_comments.append({'id_comment':id_comment,'date_comment':real_date,'text_comment':text_comment,'post_id':self.id,'thumb_url':self.thumb_url,'caption':self.caption},ignore_index=True)
        # df_comments.set_index('id_comment',inplace=True)

        return df_comments


        cod = id

        if cod != '17904215368136262':

                try:
                    total_insights = graph.get_object(cod+'?fields=insights.metric(impressions,reach,engagement,saved,video_views)')
                except:
                    total_insights=graph.get_object(cod+'?fields=insights.metric(impressions,reach,engagement)')



                name_metrics = total_insights['insights']['data']

                for metric in name_metrics:

                    name_metric = metric['name']
                    id_metric = metric['id'][:17]
                    period_metric = metric['period']

                    values_metrics = metric['values']
                    for value in values_metrics:
                        value_metric = value['value']


                    mtc = ins.Insights_instagram(id=id_metric, metric=name_metric, period=period_metric, value=value_metric,thumb_url=thumb_url,caption = caption)
                    df_insights = df_insights.append({'id':id_metric, 'metric':name_metric, 'period':period_metric, 'value':value_metric,'thumb_url':thumb_url,'caption':caption},ignore_index=True)

        df_insights.set_index('id',inplace=True)
        df_insights.to_csv('Insights.csv',sep='|')











