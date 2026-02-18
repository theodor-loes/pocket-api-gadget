# Pocket API Gadget

Et interaktivt mini-dashboard som kombinerer sanntidsdata fra ulike API-er i et morsomt og kreativt IoT-prosjekt.

I stedet for å navigere gjennom en tradisjonell liste, beveger en figur seg mellom ulike "stasjoner" (værmelding, togavganger, nyheter o.l.). Dette gir en mer intuitiv og visuell måte å hente informasjon på.

Prosjektet bruker en [Raspberry Pi Pico W](https://www.raspberrystore.nl/PrestaShop/nl/raspberry-pi-pico/439-raspberry-pi-pico-w-met-wifi-zonder-headers-5056561803173.html) og en [Pimoroni Pico Display](https://shop.pimoroni.com/products/pico-display-pack-2-0?variant=39374122582099), hvor man får et fysisk verktøy for å innhente nyttig informasjon på en morsom måte.

---

## ✨ Konsept

Tradisjonelle dashboards presenterer data i lister og sider.

Dette prosjektet utforsker en alternativ tilnærming:
- En figur fungerer som navigasjonsmekanisme
- Brukeren beveger seg fysisk mellom informasjonskilder
- Data visualiseres som scener i stedet for tekst

Målet var å kombinere:
- Kreativ UI
- God objektorientert struktur
- Tydelig separasjon mellom logikk og presentasjon
- Raspberry Pi Pico W

---

## 🧱 Arkitektur

Prosjektet er bygget med tydelig OOP-struktur:
- [Egne klasser for API-håndtering](api/yr.py)
- [Egne klasser for UI-komponenter](graphics/)
- Separasjon mellom:
  - Datainnhenting
  - State management
  - Rendering

Dette gjør prosjektet:
- Enkelt å utvide med nye API-er
- Testbart
- Skalerbart

---

## 🔌 API-integrasjoner

- Værdata (ekstern API)
- Togavganger (ekstern API)

Data hentes dynamisk og presenteres i sanntid.
Da api-dataene tar opp for stort minne for mikrokontrolleren, bruker jeg [Cloudflare](https://www.cloudflare.com/) for å prosessere dataen og formatere den før jeg sender det til mikrokontrolleren. Altså har jeg en egen api som mellomledd, noe du kan finne her: [weather_api.js](cloudflare/weather_api.js).

---

## 🚀 Funksjoner

- Interaktiv navigasjon mellom datakilder
- Kreativ UI med animert figur
- Modulær og ryddig mappestruktur
- Gjenbrukbare komponenter
- Klar separasjon mellom ansvar (Single Responsibility Principle)
<!--
---

## 🖼️ Demo

*(Legg inn GIF eller screenshot her)*

Tips:
- Ta opp en kort skjermvideo og lag en GIF
- Dette øker attraktiviteten betydelig for arbeidsgivere
-->
##💡 Hva jeg lærte

- Hvordan strukturere et prosjekt med tydelig OOP-prinsipper
- Hvordan kombinere flere API-er i én applikasjon
- Hvordan bruke UI-design som en del av navigasjonslogikken
- Viktigheten av separasjon mellom logikk og presentasjon

## 🔮 Videre utvikling

- Flere API-integrasjoner
- Forbedret animasjonssystem
- Responsiv tilpasning
