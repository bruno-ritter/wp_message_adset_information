import requests
import json
from creds import FB_ACCOUNT, FB_ACCESS_TOKEN
from datetime import date, timedelta

def get_data_meta_ads(account, access_token, timeframe='last_7d'):

    url_facebook = f'https://graph.facebook.com/v19.0/act_{account}/insights?fields=campaign_name,adset_name,ad_name,campaign_id,adset_id,ad_id,created_time,objective,impressions,clicks,spend,reach,frequency,video_p75_watched_actions,optimization_goal,quality_ranking,actions&level=ad&limit=500&time_increment=1&date_preset={timeframe}&period=day&access_token={access_token}'

    json_data = requests.get(url_facebook)
    json_data = json_data.json()

    return json_data

dict_objective_results = {
    'LINK_CLINKS': 'link_click'
}

yesterday = (date.today() - timedelta(days=1))

json_adset = get_data_meta_ads(account=FB_ACCOUNT, access_token=FB_ACCESS_TOKEN)

json_adset_yesterday = [item for item in json_adset['data'] if item['date_start'] == yesterday.strftime("%Y-%m-%d")]

# print(json.dumps(json_adset, indent=2))
 
amount_spend_in_period = round(sum(float(item['spend']) for item in json_adset['data']), 0)
amount_spend_yesterday = round(sum(float(item['spend']) for item in json_adset_yesterday), 0)

result_objective = 0
for campaign in json_adset['data']:
    try:
        for action_type in campaign['actions']:
            if action_type['action_type'] == 'link_click':
                result_objective += int(action_type['value'])
    except: KeyError

cost_per_result = round(amount_spend_in_period / result_objective, 2)

campaign_name = ''
best_ad_name = ''

message = f"Nos últimos 7 dias foram investidos R$ {int(amount_spend_in_period)}, resultando em {result_objective} cliques no link com custo de {cost_per_result} por resultado. E ontem ({yesterday.strftime('%d/%m')}) foram investidos R$ {int(amount_spend_yesterday)}. \nO melhor anúncio da semana está sendo o {best_ad_name} da campanha {campaign_name}."

print(message)
