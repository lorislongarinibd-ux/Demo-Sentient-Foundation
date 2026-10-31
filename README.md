# Agent Receipt Metadata Demo

**Scope:** Minimal, dependency-free educational reference implementation for checking whether a *declared* AI-agent action receipt has required metadata and agrees with a separately supplied claim. This is a synthetic demonstration only.

This tool is **not** an authorization or revocation enforcement mechanism; it cannot establish that an agent, observer, action, authorization, signature, timestamp or external event is authentic. It does not verify actual action completion, physical execution, cryptographic integrity, or real-world AI safety.

## What it does

Compares two JSON objects (a declared claim and a declared receipt) using basic required-field and string-match checks. Returns one of:

- `READY_FOR_INSPECTION`: required declared strings appear present and corresponding; **not** proof of execution or safety.
- `INCOMPLETE_METADATA`: required declared values absent or blank.
- `INCONSISTENT_METADATA`: declared values mismatch or reported outcome cannot be accepted as a checkable report.

All included inputs are artificial placeholders. There is no network access, data collection, API service, cloud dependency, account creation, or production integration.

## Requirements

Python 3.9+ (standard library only; no `pip install`).

## Run the examples

```bash
python3 receipt_demo.py sample_receipts.json
```

Expected statuses, in order:

```text
synthetic_consistent_metadata ... READY_FOR_INSPECTION
synthetic_stale_policy ... INCONSISTENT_METADATA
synthetic_missing_observer ... INCOMPLETE_METADATA
```

## Run tests

```bash
python3 -m unittest -v test_receipt_demo.py
```

The nine methods check only rules and fixture responses chosen by the same authoring process. Passing unit tests are **not** independent validation, safety certification, or evidence of real-world correctness.

## Public boundary

This repository is a newly authored, intentionally minimal demonstration. It contains no pre-existing proprietary source code, FPGA RTL, bitstreams, private experimental logs, non-public benchmarks, credentials, personal task data, or industrial test artifacts. There is no currently demonstrated adoption or independent reviewer endorsement.

## License

Apache License, Version 2.0. See [LICENSE](LICENSE). Software provided "AS IS" without warranties.
