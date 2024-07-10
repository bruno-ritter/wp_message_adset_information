import requests
from creds import account, access_token 

def get_data_meta_ads(account, access_token, timeframe='last_7d'):

    url_facebook = f'https://graph.facebook.com/v19.0/act_{account}/insights?fields=campaign_name,adset_name,ad_name,campaign_id,adset_id,ad_id,created_time,objective,impressions,clicks,spend,reach,frequency,video_p75_watched_actions,optimization_goal,quality_ranking,actions&level=ad&limit=500&time_increment=1&date_preset={timeframe}&period=day&access_token={access_token}'

    json_data = requests.get(url_facebook)
    json_data = json_data.json()

    return json_data

json_adset = get_data_meta_ads(account, access_token, timeframe='last_month')

print(json_adset)




