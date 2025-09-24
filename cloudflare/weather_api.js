export default {
  async fetch(request) {
    const lat = 59.91;  // your latitude
    const lon = 10.75;  // your longitude

    // Fetch full Yr forecast
    const resp = await fetch(`https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=${lat}&lon=${lon}`, {
      headers: {
        "User-Agent": "[Your User-Agent]/1.0"  // Yr requires a User-Agent
      }
    });

    const data = await resp.json();
    const timeseries = data.properties.timeseries;

    // Collect 8 forecasts: now + every 3h up to 24h
    const forecasts = [];
    for (let i = 0; i <= 24; i += 3) {
      const entry = timeseries[i];  // hourly steps
      if (!entry) break;

      const details = entry.data.instant.details;
      const nextHour = entry.data.next_1_hours?.summary?.symbol_code || "unknown";
      const precip = entry.data.next_1_hours?.details?.precipitation_amount || 0;

      // Parse the ISO time into a Date, then extract hour
      const hour = new Date(entry.time).getUTCHours();

      forecasts.push({
        time: hour,
        temperature: details.air_temperature,
        wind: details.wind_speed,
        precipitation: precip,
        symbol: nextHour
      });
    }

    return new Response(JSON.stringify(forecasts), {
      headers: { "content-type": "application/json" }
    });
  }
}
