// @ts-nocheck
import { execFile } from 'child_process';

import { promisify } from 'util';

const execFileAsync = promisify(execFile);

export async function POST({ request }) {
	try {
		const data = await request.json()
		const { stdout, stderr } = await execFileAsync(
			'python3', 
			['predict.py', JSON.stringify(data)]
		)
		console.log("stdout: " + stdout);
		return Response.json(stdout)
	} catch (error) {
		console.error(error);
		return new Response()
	}
}