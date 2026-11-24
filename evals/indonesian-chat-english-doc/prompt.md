---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Tolong buatkan file docs/adr-001-queue.md. Isinya ADR singkat: kita pilih Redis Streams daripada Kafka buat antrean job karena tim cuma 3 orang, volume sekitar 40 ribu job per hari, dan kita sudah jalanin Redis buat cache. Kafka ditolak karena biaya operasionalnya ketinggian buat tim sekecil ini. Keputusannya ditinjau lagi kalau volume tembus 1 juta job per hari.
