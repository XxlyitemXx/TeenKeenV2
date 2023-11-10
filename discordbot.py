
# RASPBERRY PI CODE



from discord import SyncWebhook
# install discord : pip install discord
import requests
import dataloadcheckRASP


inputloot1 = dataloadcheckRASP.data1
inputloot2 = dataloadcheckRASP.data2
inputloot3 = dataloadcheckRASP.data3


WEBHOOK_URL = "https://discord.com/api/webhooks/1172538727185252414/Si8JY0Ki9JSuyCMQBYrNSWAeHqu3uwkY-aGnYaB48R7uDIdH3cHhaPePM-xRycSXyNpD"   #เอาwebhook urlมาวางที่นี่


hook = SyncWebhook.from_url(WEBHOOK_URL)

hook.send("recycle :", inputloot1)
hook.send("biowaste :", inputloot2)
hook.send("dangrous :", inputloot3)