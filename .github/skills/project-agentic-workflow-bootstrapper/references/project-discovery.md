# Project discovery

Use this checklist before proposing an agent architecture.

## 1. Repository shape
- identify major directories and their responsibilities
- identify backend entrypoints, modules, services, adapters, migrations, and integration points
- identify test directories, test styles, fixtures, and CI expectations
- identify docs or specs that already govern behavior more authoritatively than chat instructions
- identify which task types really justify strict governance instead of a leaner profile
- identify which task types require a specification before the plan is frozen
- identify which surfaces are security-sensitive: external APIs, browser flows, authn/authz, tenant isolation, secrets, integrations, regulated data, expensive operations, or admin paths
- identify which real usage scenario best matches lean, standard, or rigorous

## 2. Commands and verification
- determine how the project builds
- determine how targeted tests run
- determine linting, typing, formatting, and smoke-test commands
- record the smallest useful verification commands for backend and tests
- record commands that are risky, slow, destructive, or environment-sensitive
- record any security-specific verification surfaces already present

## 3. Constraints
- list public APIs, compatibility commitments, migration rules, persistence risks, and security-sensitive surfaces
- list directories or files that should rarely be edited
- identify existing comments, specs, ADRs, or docs that represent authority
- identify whether drift has historically justified strict-governance roles
- identify trust boundaries, identity transitions, operator paths, and release criteria that could justify the optional security bundle

## 4. Existing kit audit
- inspect `.github/agents/`, `.github/instructions/`, `.github/prompts/`, workflow docs, hooks, and local specs already present
- note which files are valuable, stale, redundant, missing, or unsafe
- distinguish durable policy from one-off task residue
- decide whether the repository should start as lean, standard, or rigorous

## 5. Skill inventory
- inspect available skills and keep only the ones that materially help this project
- map each relevant skill to the role most likely to use it
- avoid a kitchen-sink routing table
- record why major skill categories were omitted

## 6. External knowledge needs
- decide whether official docs are required to avoid stale or incorrect behavior
- decide whether academic or primary technical literature materially affects the plan
- decide whether a bounded technical spike is required before architecture or planning hardens
- decide whether a source-backed verification layer is needed for specs, ADRs, or review findings
- decide whether the broader documentation-authoring role is unnecessary noise
- decide whether mcp would solve a real capability gap


## 6a. Adoption framing
- identify the closest repository-type example
- identify what the first real task should be for rollout
- identify whether the repo should start with lean, standard, or rigorous

## 7. Discovery output
Write a compact summary that distinguishes:
- fact
- hypothesis
- gap
- command
- risk
- authority source
- recommended profile
- justified optional bundles
