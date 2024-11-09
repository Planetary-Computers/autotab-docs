import autotab
from autotab.rest import ApiException


client = autotab.Client(
    autotab.Configuration(
        api_key = os.environ["AUTOTAB_API_KEY"]
    )
)

try:
    skills = await autotab.SkillApi(client).list()
    print(f"skills: {"\n".join([skill.model_dump_json(indent=2) for skill in skills])}")
except ApiException as e:
    print(f"Exception: {e})
