# Studio Dev E2E evidence

Network: `studio-dev`, chain `61997`, RPC `https://studio-dev.genlayer.com/api`.
Actor: `ic-deployer` (`0xf5c66e5155a62e27047ad4cce729593d6b9c03fc`).
Contract: `0x69Fe6D78E486CF0eB3b4828B3763e9BCD86162d0`.

| Scenario | Transaction | Finality/consensus | Authoritative result |
|---|---|---|---|
| Constructor/deploy | `0xaf38ff5df3ee569df12f8c9ec27849aad5697b1b41713d0c5c57ef0d9d1e105c` | FINALIZED / ACCEPTED | contract address above |
| Create sealed notice | `0x45bbc73475a59cc42aa8b5de98a73d2d4af7ed203c9f251ec3aa1900751f19c3` | FINALIZED / MAJORITY_AGREE | notice status `DRAFT` |
| Seal notice | recorded in CLI receipt | FINALIZED / ACCEPTED | `get_notice.status = SEALED` |
| Happy-path open assessment | `0x917b4b41f62d6340a136efe2ec0eb61becccdbd6b2d54e9e1639612578f98a5d` | FINALIZED / MAJORITY_AGREE | `OPEN`, identity true, window `OPEN`, trip limit `3500` |
| After-close commercial with all pre-closure flags | `0xf5ace3ac28955d04127279ffc0955a1ab0c8c0215bd2e408ff8a83effc5e7110` | FINALIZED / ACCEPTED | identity true, window `AFTER`, sale exception `ALLOWED`; validator disagreement correctly fails closed to `UNRESOLVED` |
| After-close recreational residual | `0x7cb49cdfa8a7dc196ec8595c0ac704022b527e574a28ef701ad8a5525de30b65` | FINALIZED / ACCEPTED | authoritative readback `CLOSED_WITH_RESIDUAL`, identity true, recreational residual `ALLOWED` |
| Replay of `assessment-open` | `0x7d16de3bbdc5b6bf113982a965f871097bf23091ff838fd9c6b98f2c36da9035` | FINALIZED / ACCEPTED with `FINISHED_WITH_ERROR` | rejected as invalid or replayed assessment; prior readback unchanged |
| Unauthorized seal by `cpc-unauthorized-20260813` | `0xa724e982939e9d049731e43889dff86202c3f73c21e2aabc5e8d9eb03edf4977` | FINALIZED / ACCEPTED with `FINISHED_WITH_ERROR` | owner-only check rejected; active owner state unchanged |
| Successor notice lifecycle | transactions recorded in `successor_seal.log` and `successor_supersede.log` | FINALIZED / ACCEPTED | old notice readback is `SUPERSEDED`; `get_superseded_by` returns `notice-2025-spanish-mackerel-successor` |

The source bulletin is NOAA's Spanish mackerel northern-zone federal reopening bulletin, SHA-256 `4af351a870befde9b50305f36eb102996fbcd9b9cc1a36e3ddf7b0cdb99cfa2e`.

The deployed contract uses strict equality over the validator-produced source comparison and fails closed to `UNRESOLVED` on disagreement or malformed external data. Replay and lifecycle state violations are rejected before state mutation.

The commercial residual scenario demonstrates the fail-closed counterexample: even with a matching profile and all pre-closure flags, a validator disagreement produces `UNRESOLVED` rather than an unsafe permission. The recreational residual scenario reaches the permitted residual state after the sector closes.
