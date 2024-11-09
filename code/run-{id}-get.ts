
import { Configuration, RunApi } from 'autotab';

const runClient = new RunApi(new Configuration({
    apiKey: process.env['AUTOTAB_API_KEY'],
}));

async function main() {
  const run = await runClient.retrieve({
    id: "run_344ed4ce-6c14-4b13-96b5-3bbb2000c2e5"
  });
}

main();