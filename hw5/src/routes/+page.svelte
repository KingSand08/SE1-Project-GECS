<script lang="ts">
	interface WeatherData {
		current: {
			temp_f: number;
			humidity: number;
			condition: {
				text: string;
			};
		};
	}

	interface Search {
		location: string;
		weatherData: WeatherData | null;
	}

	let weatherData: WeatherData | null = null;
	let location: string = '';
	let previousSearches: Search[] = [];

	async function fetchWeather() {
		const response = await fetch(`/api?location=${location}`);
		const { body } = await response.json();
		weatherData = body;
		previousSearches = [...previousSearches, { location, weatherData }];
	}
</script>

<main class="p-6 bg-gray-200 min-h-screen flex items-center justify-center">
	<div class="max-w-lg mx-auto bg-white rounded-xl shadow-lg overflow-hidden p-6 space-y-6">
		<div class="text-center">
			<div class="text-2xl text-indigo-500 font-semibold">Weather App</div>
			<div class="flex items-center justify-center mt-4">
				<input
					class="w-full px-4 py-2 rounded-md border border-gray-300 focus:border-indigo-500 focus:outline-none"
					bind:value={location}
					placeholder="Enter location"
				/>
				<button
					class="ml-2 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-500"
					on:click={fetchWeather}>Get Weather</button
				>
			</div>
			<h1 class="mt-2 text-xl font-semibold text-gray-900">Weather in {location}</h1>
			{#if weatherData}
				<div class="mt-3 text-base text-gray-500 space-y-1">
					<p>Temperature: {weatherData.current.temp_f}°F</p>
					<p>Humidity: {weatherData.current.humidity}%</p>
					<p>Condition: {weatherData.current.condition.text}</p>
				</div>
			{/if}
		</div>

		<h2 class="text-xl font-semibold text-gray-900">Previous Searches</h2>
		<ul class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
			{#each previousSearches as search (search.location)}
				<li
					class="flex flex-col text-center bg-gray-100 rounded-lg shadow divide-y divide-gray-200 p-4"
				>
					<h3 class="text-gray-900 text-sm font-medium">{search.location}</h3>
					{#if search.weatherData}
						<dl class="mt-1 flex-grow flex flex-col justify-between space-y-1">
							<dt class="sr-only">Temperature</dt>
							<dd class="text-gray-500 text-sm">
								Temperature: {search.weatherData.current.temp_f}°F
							</dd>
							<dt class="sr-only">Humidity</dt>
							<dd class="text-gray-500 text-sm">
								Humidity: {search.weatherData.current.humidity}%
							</dd>
							<dt class="sr-only">Condition</dt>
							<dd class="text-gray-500 text-sm">
								Condition: {search.weatherData.current.condition.text}
							</dd>
						</dl>
					{/if}
				</li>
			{/each}
		</ul>
	</div>
</main>
