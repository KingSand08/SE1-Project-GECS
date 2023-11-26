// tests/+server.test.ts
import { expect, test } from 'vitest'
import { GET as getWeather } from '../src/routes/api/+server'

test('GET weather data', async () => {

    const request = { url: `http://api.weatherapi.com/v1/current.json?key=f473fed20e1641d0b8011337232411&q=sanjose` }
    const response = await getWeather(request)

    const responseData = await response.json()

    expect(responseData).toEqual({ body: { error: { code: 1006, message: "No matching location found." } } })
})

test('GET weather data for San Jose', async () => {

    const request = { url: `http://api.weatherapi.com/v1/current.json?key=&q=san%20jose` }
    const response = await getWeather(request)
    const responseData = await response.json()

    expect(responseData.body.location.name).toBe("San Jose")
})