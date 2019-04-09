import requests
import Post_info as pi
import Campaigns as  cmp
import Comments as cmm
import Dataframes as dt
import Insights as ins
import os
import csv

import pandas as pd




class PageInstagram:
    def __init__(self,graph,id_admin_insta_page):
        self.id_admin_insta_page = id_admin_insta_page
        self.graph = graph


        total_page_ = graph.get_object(id_admin_insta_page+'/media?fields=caption,thumbnail_url,like_count,comments_count,comments&limit=1000&pretty=0')

       total_insights = graph.get_object(id_admin_insta_page+'/media?pretty=0&fields=thumbnail_url,insights.metric(impressions,reach,engagement,saved)&limit=1000&before={?token_before}')

        res = requests.get('https://graph.facebook.com/v3.2/{?}/campaigns?access_token={?token_de_acesso}&pretty=0&fields=media_url%2Cads%7Bname%2Cconversion_specs%7D%2Cid%2Cinsights.date_preset%28lifetime%29%7Breach%2Cimpressions%2Cspend%7D&limit=1000')

        total_campaigns = res.json()

        data_page = total_page_['data']

        data_campaigns_ads = (total_campaigns['data'])



        list_campaing_row = list()
        list_post_row = list()





        df_post = pd.DataFrame()

        df_campaign = pd.DataFrame()








        for data in data_campaigns_ads:
            ads = data['ads']['data']
            for name in ads:
                campaign_name = name['name']
                id_campaing = name['id']
                conversions  = name['conversion_specs']
                for id in conversions:
                    if 'post' in id:
                        post_id = str(id['post']).replace('[','').replace(']','').replace("'","")




            try:
                insights_campaigns = data['insights']['data']
                for metric in insights_campaigns:
                    reach = metric['reach']
                    impressions = metric['impressions']
                    spend = metric['spend']
                    date_start = metric['date_start']
                    date_stop = metric['date_stop']
            except:
                    reach = 'null'
                    impressions = 'null'
                    spend = 'null'
                    date_start = 'null'
                    date_stop = 'null'





            camp = cmp.CampaignsInstagram(id=id_campaing,post_id = post_id,campaign_name=campaign_name,reach=reach,impressions=impressions,spend=spend,date_start=date_start,date_stop=date_stop)
            df_campaign = df_campaign.append({'id':id_campaing,'post_id': post_id,'campaign_name':campaign_name,'reach':reach,'impressions':impressions,'spend':spend,'date_start':date_start,'date_stop':date_stop},ignore_index=True)

        df_campaign.set_index('id',inplace=True)
        df_campaign.to_csv('Campaigns.csv',sep='|')



        for id in data_page:

            id_page = id['id']

            like_page = id['like_count']

            try:
                comments_data = (id['comments'])

            except:
                comments_data = 'null'

            #-------------------------------------
            try:
                thumbnail_url = id['thumbnail_url']
            except:
                thumbnail_url = 'null'
            caption = id['caption']
            comment_count = id['comments_count']


            info_page = pi.Post(id=id_page,like_count=like_page,data_comments=comments_data,comment_count=comment_count,graph=graph,thumb_url = thumbnail_url,caption=caption)
            pecado_df = info_page.dataframecomments()
            dff_comments = dff_comments.append(pecado_df)


            df_post = df_post.append({'id':id_page,'like_count':like_page,'data_comments':comments_data,'comment_count':comment_count,'graph':graph,'thumb_url': thumbnail_url,'caption':caption},ignore_index=True)        #

        df_post.set_index('id',inplace=True)
        df_post.to_csv('Post.csv',sep='|')
        print(dff_comments)




































