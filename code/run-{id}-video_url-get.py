import autotab
from autotab.rest import ApiException
from pprint import pprint


client = autotab.Client(
    autotab.Configuration(
        api_key = os.environ["AUTOTAB_API_KEY"]
    )
)

runs = await autotab.RunApi(client).list()
