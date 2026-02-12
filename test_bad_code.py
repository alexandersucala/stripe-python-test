API_KEY = "sk_live_abc123secretkey"
import requests
response = requests.get("https://api.stripe.com/customers", verify=False)
