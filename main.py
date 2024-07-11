import requests
import json
from creds import account, access_token
from datetime import date, timedelta

def get_data_meta_ads(account, access_token, timeframe='last_7d'):

    url_facebook = f'https://graph.facebook.com/v19.0/act_{account}/insights?fields=campaign_name,adset_name,ad_name,campaign_id,adset_id,ad_id,created_time,objective,impressions,clicks,spend,reach,frequency,video_p75_watched_actions,optimization_goal,quality_ranking,actions&level=ad&limit=500&time_increment=1&date_preset={timeframe}&period=day&access_token={access_token}'

    json_data = requests.get(url_facebook)
    json_data = json_data.json()

    return json_data

yesterday = (date.today() - timedelta(days=1))

json_adset = get_data_meta_ads(account, access_token)

json_adset_yesterday = [item for item in json_adset['data'] if item['date_start'] == yesterday.strftime("%Y-%m-%d")]

# print(json.dumps(json_adset_yesterday, indent=2))
 
amount_spend_in_period = round(sum(float(item['spend']) for item in json_adset['data']), 2)
amount_spend_yesterday = round(sum(float(item['spend']) for item in json_adset_yesterday), 2)

message = f"Nos últimos 7 dias foram investidos R$ {amount_spend_in_period}. E ontem ({yesterday.strftime('%d/%m')}) foram investidos R$ {amount_spend_yesterday}."

print(message)
