# Fishery Reopening Residual Rule Receipt

This contract records a bounded fishery notice and returns a fail-closed receipt for a specific species, zone, sector, permit class, and query time. It does not authorize fishing.

## Current status

Stage 3 is deployed on Studio Dev (chain 61997) at `0x69Fe6D78E486CF0eB3b4828B3763e9BCD86162d0`. Deployment receipt: `0xaf38ff5df3ee569df12f8c9ec27849aad5697b1b41713d0c5c57ef0d9d1e105c`.

## Contract surface

- Owner lifecycle: `create_notice`, `seal_notice`, `supersede_notice`.
- Public assessment: `assess_profile`.
- Readback: `get_notice`, `get_assessment`, `get_superseded_by`, `is_harvest_open`, `get_residual_rights`.
- Decisions: `OPEN`, `CLOSED_WITH_RESIDUAL`, `CLOSED`, or `UNRESOLVED`.

The source bulletin, hash, and exact profile fields are stored with each notice. Identity mismatch, invalid state, malformed fields, replay, and unauthorized lifecycle writes fail closed.

## Verified Studio Dev evidence

The exact transaction/readback matrix is in `E2E_EVIDENCE.md`. The happy-path create, seal, and open assessment are finalized with majority consensus; the authoritative open readback is `decision: OPEN`, `identity_match: true`, `window_state: OPEN`, and `trip_limit_lb: 3500`.
