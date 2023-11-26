import type { RequestHandler } from "@sveltejs/kit";

export const GET: RequestHandler = async (request) => {
    const location = new URL(request.url).searchParams.get('q')
    const response = await fetch(
        `http://api.weatherapi.com/v1/current.json?key=f473fed20e1641d0b8011337232411&q=${location}`
    );
    const weatherData = await response.json();
    return new Response(JSON.stringify({ body: weatherData }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
    });
}