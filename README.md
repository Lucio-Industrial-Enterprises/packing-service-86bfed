# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

```python
shipping_quote(weight_kg, zone, service="standard") -> float
```

Returns a shipping quote in US dollars.

| Parameter   | Type    | Description                                      |
|-------------|---------|--------------------------------------------------|
| `weight_kg` | `float` | Parcel weight in kilograms (must be positive).   |
| `zone`      | `str`   | Delivery zone: `"local"` or `"regional"`.        |
| `service`   | `str`   | Service level: `"standard"` (default) or `"express"`. |

**Pricing:**

| Zone       | Standard base | Express surcharge |
|------------|--------------|-------------------|
| `local`    | $5.00        | +$7.00            |
| `regional` | $8.00        | +$7.00            |

A per-kg rate of $1.50 is added for all services and zones.

**Examples:**

```python
from warehouse.rates import shipping_quote

shipping_quote(2, "local")                    # → 8.0  (standard)
shipping_quote(2, "local", service="express") # → 15.0 (express)
```

**CLI usage:**

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

```
$ python -m warehouse.cli 2 local
$8.00
$ python -m warehouse.cli 2 local --service express
$15.00
```
