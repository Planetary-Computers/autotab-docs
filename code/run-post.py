import autotab
from autotab import RunSkillRequest
from autotab.rest import ApiException


client = autotab.Client(
    autotab.Configuration(
        api_key = os.environ["AUTOTAB_API_KEY"]
    )
)

try:
    run = await autotab.RunApi(client).start(
        run_skill_request=RunSkillRequest(
            skill_id="skill_a6738f77-afc2-454e-a6d6-207caa8d145f",
            inputs={
                "query": "OpenAI news"
            }
        )
    )
except ApiException as e:
    print(f"Exception: {e})
