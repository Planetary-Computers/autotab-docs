import autotab
from autotab.rest import ApiException
from pprint import pprint


client = autotab.Client(
    autotab.Configuration(
        api_key = os.environ["AUTOTAB_API_KEY"]
    )
)

try:
    run = await autotab.RunApi(client).retrieve(
        id="run_344ed4ce-6c14-4b13-96b5-3bbb2000c2e5"
    )
    print(f"state: {run.state} output: {run.data}")
except ApiException as e:
    print(f"Exception: {e})
