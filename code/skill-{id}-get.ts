import { Configuration, SkillApi } from 'autotab';

const skillClient = new SkillApi(new Configuration({
    apiKey: process.env['AUTOTAB_API_KEY'],
}));

async function main() {
  const skill = await skillClient.retrieve({
    id: "skill_923d8f38-be0d-4637-9fbe-46ec9cb48312"
  });
  
  console.log("skill:", skill);
}

main();