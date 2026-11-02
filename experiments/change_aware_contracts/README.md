# Change-aware boundary contract witness

**Status:** independently executed **synthetic** Python standard-library fixture, NOT a real LangChain package reproduction, not an agent benchmark, not an LLM evaluation, no new method claimed.

Based on the *behavioral mechanism* in [LangChain PR #40530](https://github.com/langchain-ai/langchain/pull/40530) → [issue #40853](https://github.com/langchain-ai/langchain/issues/40853) → [PR #40864](https://github.com/langchain-ai/langchain/pull/40864).

## Run

```sh
cd experiments/change_aware_contracts
python -m unittest discover -v
python protocol_witness.py
```

Recorded result 2026-11-02: **8 tests passed** using Python standard-library `unittest`. The modeled stages have orphan-result counts **0 → 1 → 0**. After the local repair, the narrow unit check passes while the downstream message-pairing invariant fails.

The local code deliberately re-implements only the minimal protocol concept; there are no external dependencies or real provider calls. The changed helper/mutant behavior is known by construction, so this demo proves no real-world detection rate. Next: pin and execute the *actual reporter's* offline script against upstream package versions, then compare ordinary tests with edit-triggered boundary tests on independently confirmed historical regressions.

See [research study](../../research/2026-11-02_CHANGE_AWARE_CONTRACT_TESTING.md).
