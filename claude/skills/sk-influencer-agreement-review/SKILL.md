---
name: sk-influencer-agreement-review
description: "Review influencer/creator agreements for content rights, exclusivity, FTC compliance (16 CFR 255), AI/Synthetic Media consent, whitelisting/paid usage, and platform-specific requirements. Covers: Instagram, TikTok, YouTube. Includes AI Influencer/Virtual Influencer guidance. Triggers: (1) 'check contract' → checklist review, (2) 'advise' / 'review' → full consultation with playbook. Jurisdiction: New York, USA (FTC); for Spain/EU apply LGP, LCD, the Spanish influencer code (Autocontrol) and LSSI instead."
metadata:
  author: "Ilya Korneev"
  license: "Apache-2.0"
  homepage: "https://github.com/ik-bk"
  repository: "https://github.com/ik-bk/skills"
---

# Influencer Agreement Review

> **NOT LEGAL ADVICE.** General guidance only. Consult qualified counsel.

## Routing

| Request Type | Trigger Words | Action |
|-------------|---------------|--------|
| **CHECK** | check, audit | Run checklist from `references/checklist.md` |
| **ADVISE** | review, advise | Full consultation using `references/playbook.md` |

**Rules:**
- File uploaded → default to ADVISE
- CHECK + ADVISE can combine
- Output language = Input language (auto-detect)


## CHECK Mode

1. Read `references/checklist.md`
2. Run through each item against document
3. Output table with Status (✅/❌) and Notes

## ADVISE Mode

1. Identify client perspective (Brand or Influencer/Creator)
2. Read `references/playbook.md`
3. Scan document against playbook criteria
4. Output structured consultation:

**Format:**
```
**Overall: 🔴/🟡/🟢**

**Summary:** 3-5 bullets

**Issues:**
| Priority | Section | Issue | Recommendation |
|----------|---------|-------|----------------|
| 🔴/🟡/🟢 | X.X | Problem | Preferred: ... / Fallback: ... |

**Missing Terms:** list vs baseline

**Questions:** clarifications needed
```

## Risk Levels

| Level | Meaning | Action |
|-------|---------|--------|
| 🔴 RED | Material risk | Must fix |
| 🟡 YELLOW | Outside preference | Negotiate |
| 🟢 GREEN | Acceptable | Note only |

## References

| File | When to Read |
|------|--------------|
| `references/checklist.md` | CHECK mode — item-by-item review |
| `references/playbook.md` | ADVISE mode — negotiation guidance |

## Hard Rules

- Never invent clause/section numbers
- File uploaded = ADVISE mode
- Legal terms: English + translation in user's language
