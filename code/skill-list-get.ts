import { Configuration, SkillApi } from 'autotab';

const skillClient = new SkillApi(new Configuration({
    apiKey: process.env['AUTOTAB_API_KEY'],
}));

async function main() {
  const skills = await skillClient.list();
  console.log("skills:", skills);
}

main();