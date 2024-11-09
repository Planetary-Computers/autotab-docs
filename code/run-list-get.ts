
import { Configuration, RunApi } from 'autotab';

const runClient = new RunApi(new Configuration({
    apiKey: process.env['AUTOTAB_API_KEY'],
}));

async function main() {
  const runs = await runClient.list();
  console.log("runs:", runs);
}

main();