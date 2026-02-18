export default {
  async fetch(request) {
    const lat = 59.91;  // lat for Oslo
    const lon = 10.75;  // lon for Oslo

    // Henter full værmelding fra YR
    const resp = await fetch(`https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=${lat}&lon=${lon}`, {
      headers: {
        "User-Agent": "[Legg Inn User-Agent]/1.0"  // Yr krever en User-Agent
      }
    });

    const data = await resp.json();
    const timeseries = data.properties.timeseries;

    // Hent 8 værmeldinger: nå + hver 3. time, opp til 24 timer frem
    const forecasts = [];
    for (let i = 0; i <= 24; i += 3) {
      const entry = timeseries[i];  // timeseries er delt opp i timer
      if (!entry) break;

      const details = entry.data.instant.details;
      const nextHour = entry.data.next_1_hours?.summary?.symbol_code || "ukjent";
      const precip = entry.data.next_1_hours?.details?.precipitation_amount || 0;

      // Analyser ISO-tiden til et Date-objekt, for å hente timer
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
