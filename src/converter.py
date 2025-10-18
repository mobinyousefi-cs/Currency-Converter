"""Currency conversion logic."""
self.ttl = ttl # time-to-live for rates in seconds
self._cache: Dict[str, Dict] = {}
self._lock = threading.RLock()


def _fetch_rates(self, base: str) -> Dict[str, float]:
params = {"base": base}
try:
resp = self.session.get(API_URL, params=params, timeout=10)
resp.raise_for_status()
data = resp.json()
rates = data.get("rates")
if not rates:
raise RateFetchError("No rates in response")
return rates
except requests.RequestException as e:
raise RateFetchError(str(e)) from e


def get_rates(self, base: str = "EUR") -> Dict[str, float]:
key = base.upper()
now = time.time()
with self._lock:
entry = self._cache.get(key)
if entry and now - entry["ts"] < self.ttl:
return entry["rates"]


rates = self._fetch_rates(key)
with self._lock:
self._cache[key] = {"ts": now, "rates": rates}
return rates


def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
"""Convert amount from `from_currency` to `to_currency`.


Raises RateFetchError on network or API failures.
"""
if from_currency.upper() == to_currency.upper():
return float(amount)


base = from_currency.upper()
rates = self.get_rates(base=base)
to_curr = to_currency.upper()
try:
rate = rates[to_curr]
except KeyError:
raise RateFetchError(f"Currency not supported: {to_curr}")
return float(amount) * float(rate)