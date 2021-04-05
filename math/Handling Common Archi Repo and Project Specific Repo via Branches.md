

```sequence
Title: Handling Common Archi Repo and Project Specific Repo via Branches
Archi Repo (Baseline)->Project A (Ongoing): Create new Branch to, with [market]-[projectname]-Ongoing
Project A (Ongoing)->Project A (Ongoing): Project work， keep commit and push
Note right of Project A (Ongoing): DO NOT MERGE BACK TO BASELINE!!!
Archi Repo (Baseline)->Archi Repo (Baseline): Central Repository Updating
Archi Repo (Baseline)->Project A (Ongoing): Sync/Merge from Central Repo to get latest updates
Project A (Ongoing)->Project A (Release): When finish, create new Branch, with [market]-[projectname]-Release
Project A (Release)->Project A (Release): Clean Up till only the final deliverable / artefact left, Commit/Push
Archi Repo (Baseline)->Project A (Release): Merge from Baseline to
Project A (Release)->Project A (Release): Push
Note right of Project A (Release): Final Project Repo Merge Back Review Meeting!
Project A (Release)->Archi Repo (Baseline): Merge from Project A (Release) back to Baseline
Archi Repo (Baseline)->Archi Repo (Baseline): Push
Archi Repo (Baseline)->Archi Repo (Baseline): Post Review and Clean Up
Archi Repo (Baseline)->Archi Repo (Baseline): Commit/Push, Becomes new Baseline
```

