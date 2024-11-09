import autotab
from autotab.rest import ApiException


client = autotab.Client(
    autotab.Configuration(
        api_key = os.environ["AUTOTAB_API_KEY"]
    )
)

try:
    skill = await autotab.SkillApi(client).retrieve(
        id="skill_923d8f38-be0d-4637-9fbe-46ec9cb48312"
    )
    print(f"skill: {skill.model_dump_json(indent=2)}")
except ApiException as e:
    print(f"Exception: {e})
