import autotab
from autotab.rest import ApiException
from pprint import pprint


client = autotab.Client(
    autotab.Configuration(
        api_key = os.environ["AUTOTAB_API_KEY"]
    )
)

try:
    await autotab.RunApi(client).cancel(
        id="run_344ed4ce-6c14-4b13-96b5-3bbb2000c2e5"
    )
except ApiException as e:
    print(f"Exception: {e})