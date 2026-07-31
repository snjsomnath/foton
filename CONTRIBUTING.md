# Contributing

Use Python 3.10 or newer, Rust 1.85 or newer, and Node.js 20 or newer.

```bash
python -m pip install -e ".[honeybee,viewer,test]"
cargo test --workspace
python -m pytest tests/python
cd viewer && npm ci && npm test -- --run
```

Keep changes focused and preserve backend parity. Transport changes should be validated
in this order: direct visibility, full coefficients, then annual illuminance and
metrics. GPU-specific integration tests should skip cleanly when compatible hardware
is unavailable.
