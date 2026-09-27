# Fishery Reopening Residual Rule Receipt

## STUDIO DEV RESEARCH UPDATE — 2026-09-27
- **Technical slug/class:** `fishery-reopening-residual-rule-receipt`.
- **Network boundary:** Studio Dev only, using the current documented GenLayer CLI/SDK and current Intelligent Contract API. No legacy network, chain, RPC, private key, deployment, broadcast, or Studio test is part of this research.
- **Studio Dev feasibility verdict:** REVISE. The bounded NOAA rule vector is suitable for a Studio Dev build only after a CLI HTML-fetch probe and exact timezone/parser check; no live network or current legal effect is claimed.
- **External-source rule:** only the named allowlisted official domains may be fetched; redirects, blocked pages, source drift, parser ambiguity, validator disagreement, or missing authoritative fields produce `UNRESOLVED` and do not create a favorable state.
- **Build handoff condition:** AI chính may start Stage 3 only after confirming current CLI/API compatibility, storage and nondeterministic-call syntax, Equivalence Principle behavior, and a bounded Studio Dev HTML/PDF/source-access probe. Research evidence is not deployment or E2E evidence.

## STAGE 1

- **Objective/users:** Resolve the controlling open/closed interval and the residual activities still expressly allowed for one fishery sector/profile after a closure or short reopening. Compliance calendars and seafood-market review queues consume the receipt; it does not authorize fishing.
- **Trust problem / GenLayer need:** NOAA bulletins combine species, zone, permit class, time window, trip limit, post-closure sale exception, and recreational residual rights in prose. A headline-only scraper can treat a reopening as universal or a closure as total. Independent validators must agree on the complete bounded applicability tuple.
- **Core mechanism:** owner seals species/group, zone, sector, permit class, query time, and 1-2 NOAA URLs; consensus returns `identity_match`, `window_state`, `trip_limit`, `sale_exception_state`, `recreational_residual_state`, and `OPEN/CLOSED_WITH_RESIDUAL/CLOSED/UNRESOLVED`.
- **Concrete public source set, checked 2026-09-21:** NOAA's [Spanish mackerel northern-zone eight-day reopening bulletin](https://www.fisheries.noaa.gov/bulletin/commercial-reopening-atlantic-migratory-group-spanish-mackerel-northern-zone-federal) states reopening from 2025-09-29 12:01 local to 2025-10-07 12:01 local, a 3,500-pound commercial trip limit, the six-state northern-zone scope, a cold-storage sale/purchase exception for fish harvested/landed/sold before closure, and continued recreational retention under recreational limits while that sector is open. Querying a commercial profile after 2025-10-07 must yield `CLOSED_WITH_RESIDUAL`, not `OPEN`. Treating cold storage as permission for newly harvested fish is the counterexample.
- **Actors/evidence/validator:** manifest owner, assessor, reader; official NOAA HTML and optional linked Federal Register document, sealed hashes/times. Leader and validators independently refetch and exact-match the tuple; evidence instructions are ignored.
- **Closest baseline/difference:** Carrier Service Restriction Applicability Oracle and Port Closure Cargo Exemption Oracle. Inherited: profile-to-restriction mapping. Material difference: a quota-driven fishery lifecycle has a short reopening, sector-specific trip cap, pre-closure inventory exception, and recreational residual right under one bulletin. **Difference: high.** Reusable value is a temporal residual-right receipt.
- **Risks/feasibility:** safety/economic reliance and later bulletins; exact retrieval/hash, closed enums, and `UNRESOLVED` on conflict. NOAA public HTML is evidenced; current GenVM access is a later build-stage probe.
- **Stage 1 acceptance:** complete real decision-field set, non-total-closure counterexample, bounded safe claim, material difference, and fail-closed behavior.

## STAGE 2

- **Model/lifecycle:** `FisheryNotice`, `Profile`, `Assessment`; `DRAFT -> SEALED -> SCHEDULED -> OPEN -> CLOSED_WITH_RESIDUAL | CLOSED -> SUPERSEDED`.
- **Invariants/storage:** immutable agency/species/zone/sector/notice identity; ISO time bounds; known permit and residual enums; no `OPEN` outside interval; cold-storage exception requires all pre-closure predicates; later notice never overwrites history.
- **API/auth:** `create_notice`, `seal_notice`, `assess_profile`, `supersede_notice`, `get_assessment`, `is_harvest_open`, `get_residual_rights`. Owner lifecycle; public assessment; strict URL/hash/time/weight/enum/replay validation.
- **Prompt/EP:** strict JSON, delimited untrusted bulletin, independent refetch/extraction, exact consequential-field comparison; explanation/citations display-only.
- **Failure/retry/replay/appeal/timeout:** identity/time/source conflict => `UNRESOLVED`; identical replay idempotent; later notice or corrected profile creates child assessment; appeal references prior; timeout preserves state.
- **Tests/E2E:** actual eight-day open interval, after-close residual, cold-storage predicates, new-harvest counterexample, recreational-sector condition, wrong species/zone/permit/time, hostile text, malformed output, disagreement, auth, replay, supersession, rollback/readback.
- **CLI/architecture:** later current CLI, explicit Studio Dev account, one contract/test/README/samples/evidence matrix; SDK only. Exclude quota forecasting, vessel tracking, licensing, enforcement, payments, frontend.
- **Stage 2 acceptance/status:** full minimal lifecycle and residual-right binding specified; `REVISE BEFORE BUILD — pending Studio Dev CLI/source-access verification`.
- **Final research disposition:** `REVISE BEFORE BUILD` — Stage 3 may begin only after the Studio Dev CLI/source-access checks listed above pass; no research-only evidence is a deployment or E2E result.
