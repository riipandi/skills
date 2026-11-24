# Indonesian text

Use this whenever the output is in Indonesian: every chat reply in a session where the user writes in Indonesian,
an Indonesian draft to rewrite or review, or an artifact that `language.md` allows in
Indonesian (locale files, UI copy for the `id` locale, a file the user asked for in
Indonesian).

The goal is plain Indonesian a reader understands on first reading, with no loss of meaning,
nuance, or precision. Plain does not mean simplified. This file adapts the
`bahasa-indonesia-plain` skill by orepras to this skill's safeguards. Where the two disagree,
`SKILL.md` wins: no invented facts, the author's sample outranks house rules, and no dashes.

## Chat replies

Most Indonesian this skill produces is conversation. These rules apply to every reply in an
Indonesian chat session, whatever the task: coding, debugging, planning, or writing. The rest
of this file applies to chat too, scaled to the length of the reply.

- Lead with the answer or the result. Background comes after, if at all.
- Match the user's register. If they write `kamu`, `aku`, or `gue`, do not answer in stiff
  formal prose. If they write `Anda`, stay formal. Pick one form of address and keep it.
- Keep technical terms the user uses in English as they are: `commit`, `pull request`, `deploy`,
  `endpoint`, `branch`. Do not write `permintaan tarik`. Use the Indonesian word when it is the
  common one: `berkas` or `file`, `unduh`, `unggah`, `tautan`, `setelan`.
- Do not italicize or quote every English term. Write it plainly.
- No service-desk wrapper: `Tentu!`, `Pertanyaan bagus!`, `Semoga membantu!`, `Jangan ragu
  untuk bertanya`.

## Content principles

- Start from what the reader needs to know to act or decide, not from what you want to say.
- Put the most important point first: in the document, the section, the paragraph, and the
  sentence. Conclusion, then detail, then background.
- One idea per sentence, one topic per paragraph. Aim for 12 to 20 words per sentence and
  rarely more than 25. This is a target for guides and UI text, not a cap on authored prose.
- Name the number, the name, the date. Avoid vague fillers such as `berbagai macam`, `ke
  depannya`, `dalam rangka`, `terkait hal tersebut`.
- Cut what adds no meaning. Do not cut a condition, a warning, or a qualifier the source needs.

## Word choice

Prefer the everyday word over office and bureaucratic language:

| Instead of | Prefer |
|---|---|
| memanfaatkan, mengoptimalkan (non-technical) | menggunakan, memakai |
| memfasilitasi, memberdayakan | membantu |
| berkolaborasi, bersinergi | bekerja sama |
| menghadirkan, men-deliver | membuat, menyediakan |
| terkait hal tersebut, berkenaan dengan | soal, tentang |
| dalam rangka, guna | supaya, agar, untuk |
| melakukan pengecekan, melakukan pembayaran | mengecek, membayar |
| adalah merupakan | adalah (or drop it) |
| hal ini dikarenakan | karena, sebab |
| pada saat ini, di masa sekarang | sekarang, saat ini |

Avoid stock metaphors and buzzwords unless they name a specific thing: `ekosistem`, `sinergi`,
`akselerasi`, `transformasi digital`, `robust`, `leverage`, `deep dive`, `solusi terintegrasi`.

Use `dia`, `ia`, or `beliau` as the neutral singular pronoun when the person is unknown. Use
`kami` for the organization or team and `kita` only when the reader is included.

## Natural sentence structure

Avoid sentences that read as translated from English.

```txt
Prefer: Kamu bisa mengubah kata sandi kapan saja.
Avoid:  Perubahan kata sandi dapat dilakukan kapan saja oleh kamu.

Prefer: Isi semua kolom yang wajib diisi.
Avoid:  Pastikan bahwa semua kolom yang bersifat wajib telah diisi terlebih dahulu.

Prefer: Simpan perubahan?
Avoid:  Apakah Anda yakin ingin menyimpan perubahan yang telah dilakukan?
```

Common calques to fix:

- `di mana` and `yang mana` as relative pronouns (`sistem di mana pengguna...`). Use `yang`,
  `tempat`, or split the sentence.
- A possessive chain copied from English (`fitur dari aplikasi dari kami`). Write `fitur
  aplikasi kami`.
- `adalah` before an adjective or verb (`Ini adalah penting`). Write `Ini penting`.
- A plural marked twice (`banyak data-data`, `para hadirin sekalian`).
- `-nya` scattered as a stand-in for `the`.
- English word order in noun phrases (`online toko`, `digital layanan`).

Passive voice needs care here. The `di-` passive is natural Indonesian and often the plainest
choice when the object is the topic: `Data disimpan otomatis.` Edit the passive when it hides
who must act, or when it drags an agent behind it with `oleh`. Tier: weak alone.

Use `-lah` and `-kah` sparingly, and only where a speaker would.

## AI tells in Indonesian

The patterns in `patterns.md` appear in Indonesian with the same tiers. Common forms:

| Pattern | Indonesian form |
|---|---|
| S1 Not X but Y | `bukan sekadar X, melainkan Y`; `bukan hanya X, tetapi juga Y`; `Ini bukan tentang X. Ini tentang Y.` |
| S2 Closers | `Dan itulah intinya.` `Sesederhana itu.` `Titik.` `Pada akhirnya, ...` |
| S3 Deep sayings | `Pada dasarnya`, `Pada hakikatnya`, `Yang sebenarnya terjadi adalah`, `X adalah kunci` |
| S4 Run-ups | `Mari kita bahas`, `Mari kita telusuri`, `Perlu diketahui bahwa`, `Perlu dicatat bahwa`, `Jujur saja,`, `Faktanya,` |
| S6 Chatbot residue | `Tentu!`, `Pertanyaan yang bagus!`, `Berikut adalah...`, `Semoga membantu!`, `Jangan ragu untuk...` |
| S8 About the document | `Pada bagian ini kita akan`, `Seperti yang akan kita lihat`, `Artikel ini akan membahas` |
| S9 Inflation | `memainkan peran penting`, `menjadi bukti nyata`, `tonggak sejarah`, `di era digital saat ini`, `di tengah pesatnya perkembangan` |
| S10 Borrowed authority | `para ahli berpendapat`, `penelitian menunjukkan`, `banyak pihak menilai` |
| W1 Stock words | `signifikan`, `komprehensif`, `holistik`, `krusial`, `inovatif`, `optimal`, `seamless` |
| W2 Triads | `cepat, mudah, dan aman` when the text supports one of the three |
| W4 Fillers | `sangat`, `benar-benar`, `sejatinya`, `tentunya`, `pastinya`, `cukup`, `mungkin saja` |
| Generic endings | `Kesimpulannya`, `Dengan demikian`, `Semoga bermanfaat` |

Dashes: the hard rule H1 applies. Indonesian style guides allow the `tanda pisah` for
explanatory pauses, but this skill does not use it. Write a comma, a colon, parentheses, or a
new sentence. For a range write `sampai` or `hingga`: `10 sampai 20 orang`.

## Inclusive language

- Put the person first: `pengguna dengan disabilitas`, not `penyandang cacat`. Use the term a
  community chooses for itself when it differs (for example `Tuli`).
- Avoid stigmatizing words used as labels: `gila`, `bodoh`, `lambat`, `cacat`, `abnormal`.
- Avoid a single assumed norm (`keluarga normal`) and humor based on ethnicity, gender,
  religion, or body.
- Do not assume an urban or Jakarta context, a fast connection, a recent phone, or a bank
  account. Use example names and settings from across Indonesia.

## Trauma-informed communication

- Do not blame the user. Not `Kamu gagal` or `Input tidak valid`. Say what happened and what to
  do next: `Email ini belum terdaftar. Coba email lain atau daftar dulu.`
- Say what will happen before it happens. Never let an irreversible action come as a surprise.
- No false urgency: `Segera selesaikan!`, `Kamu ketinggalan!`. State real deadlines plainly.
- For sensitive topics (health, money, law, loss), acknowledge the weight without dramatizing
  it, and give a clear way to stop or go back.

Do not add reassurance the source does not support. `Data kamu tidak hilang` is a factual claim:
write it only when it is true.

## Numbers, dates, and money

These conventions apply to Indonesian text only. English artifacts follow `language.md`.

- Thousands with a period, decimals with a comma: `1.500.000`, `2,5`.
- `Rp75.000` with no space. Large amounts in words: `Rp5 miliar`.
- `50%` with no space. Give the base with a percentage: `30% lebih murah, dari Rp100.000
  menjadi Rp70.000`.
- Dates as `4 Juni 2026`, never `04/06/26`. Ranges as `4 sampai 8 Juni 2026`.
- Times with a period: `10.00`. Write `tengah hari` and `tengah malam` instead of `12.00`.
- Do not stack numbers in one sentence. Move them into a list or a table.
- For critical steps, use order words as well as numerals: `Pertama`, `Kedua`, `Terakhir`.

## Spelling and formatting (EYD)

- Sentence case everywhere: headings, buttons, labels, table headers. Capitals only for proper
  names and official names. Never capitals for emphasis.
- A period ends a full sentence, including a list item that is a full sentence.
- At most one exclamation mark, and only for a real celebration.
- Bold only for a literal UI element name in an instruction: pilih **Simpan**.
- Headings lead with the keyword, stay under about 65 characters, and end with no punctuation.
- Link text describes the destination. Never `klik di sini`.
- Write `misalnya`, `yaitu`, `dan sebagainya` instead of `e.g.`, `i.e.`, `dll.`. Write `dan`
  instead of `&`.

## UI copy and microcopy

| Element | Rule | Example |
|---|---|---|
| Button, CTA | An active verb that names the result | `Simpan dokumen`, `Kirim lamaran`, not `OK` or `Submit` |
| Empty state | State the condition and offer the next step | `Belum ada data di sini. Tambahkan item pertamamu.` |
| Success | Short, warm, concrete | `Profil kamu sudah diperbarui.` |
| Error | What happened, then what to do | `Pengiriman gagal. Coba lagi.` |
| Placeholder | Format example only, never the label | `nama@email.com` |
| Helper text | One sentence answering why or what | `Kami pakai nomor ini untuk mengirim kode masuk.` |
| Destructive confirm | Name the consequence | `Hapus akun? Data kamu akan hilang dan tidak bisa dikembalikan.` |
| Onboarding | Invite, do not order | `Yuk mulai dengan membuat profilmu.` |

Keep product terms consistent with the existing interface. Do not rename a label to improve it
unless the user asked for that.

## RASA: the quality lens

After the draft, read it four times, once per question. RASA is a set of questions, not a
score. Report findings in words.

- **Ritmis.** Read it aloud. Do sentence lengths vary? Does the text breathe? Does anything
  make the reader stumble or reread?
- **Akurat.** Does each word carry exactly the intended meaning, or only come close? Any
  unwanted connotation? Any filler or vague qualifier (`cukup`, `beberapa`, `berbagai`)?
- **Sarat makna.** Does each line carry weight? Is anything long but empty? Does the call to
  action give a real reason?
- **Alami.** Would a person say this? Does the tone fit the moment? Does it read as Indonesian
  or as a translation? Natural is not the same as informal: formal text can still sound human.

## Self-check

- The most important point comes first.
- A first-time reader understands every sentence.
- No calque, bureaucratic phrase, or stock AI phrase remains without a reason.
- No fact, number, condition, or warning was lost while simplifying.
- The text is safe for a reader in a vulnerable state and free of stigma and false urgency.
- Numbers and dates follow the conventions above.
- No dash is used as a connector.

## Source

Adapted from `bahasa-indonesia-plain` by orepras
(<https://gist.github.com/orepras/3e1ca8974fc51d11825f142fa6a66635>), including the RASA
framework. The calque list, the Indonesian pattern table, the chat-reply section, and the dash
rule are additions made for this skill.
