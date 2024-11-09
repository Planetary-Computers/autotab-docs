import { Configuration, RunApi } from 'autotab';

const runClient = new RunApi(new Configuration({
    apiKey: process.env['AUTOTAB_API_KEY'],
}));

async function main() {
  const run = await runClient.start({
    runSkillRequest: {
        skillId: "skill_fe517503-384a-45c5-87a3-94f98126e626"
    }
  });
  
  console.log("result:", run);
}

main();