import type { RequestHandler } from "@sveltejs/kit";
import { WEATHERAPI_API_KEY } from "$env/static/private";

export const GET: RequestHandler = async (request) => {
    const location = new URL(request.url).searchParams.get('q')
    const response = await fetch(
        `http://api.weatherapi.com/v1/current.json?key=${WEATHERAPI_API_KEY}&q=${location}`
    );
    const weatherData = await response.json();
    return new Response(JSON.stringify({ body: weatherData }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
    });
}