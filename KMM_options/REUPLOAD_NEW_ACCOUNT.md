# KMM — Re-upload checklist for the NEW Higgsfield account (2026-10-02)

The user switched to a new Higgsfield account. Media IDs are per account, so **every ID in `HANDOFF_GUIDE.md`, `STYLE_GUIDE_B.md` and the skill file belongs to the OLD account** and will not work on the new one. Re-upload the files below. The assistant then replaces each old ID with the new one in all guides and in the skill.

Status: IN PROGRESS. The account DID change on 2026-10-02 (new workspace `ad401adb-c6e7-47e9-824e-4f7d645dc170`). BG + CH uploaded; guides remapped. Still missing: Fantasy.mp4 master video (needs 720p H.264 + silent AAC), fantasy forest, bus, phone, mom photo, StandardB.

## Steps
1. Reconnect Higgsfield (new account) at https://claude.ai/customize/connectors, then start a new Claude session. Connectors only load at session start.
2. In the new session, ask: "mở widget upload". Upload in the batches below; the widget takes up to 20 files at once.
3. Send back the media_id + filename for each file. The assistant maps old → new IDs and updates every guide.
4. Create a new project/folder "MV KMM" in the new account. The old folder `fef878e4-…` belongs to the old account.

## Batch 1: required for every fantasy scene
| # | File | Role | Old ID (old account) | New ID |
|---|---|---|---|---|
| 1 | `Fantasy.mp4` (master video, original) | Video 1 fantasy master | `83190f2e…` (was the 720p transcode) | |
| 2 | `01_Mai_FAntasy.png` | Mai fantasy | `ef343c87…` | |

Master video: upload the original. The assistant must transcode it again to **H.264 8-bit yuv420p, 1280x720, 24 fps, with a silent AAC track** (the only format that worked). The 720p file that worked lived only on the old account.

## Batch 2: backgrounds
| # | File | Old ID | New ID |
|---|---|---|---|
| 3 | `B15_TuongManHinh.png` (screen wall, latest version) | `f8cfd99c…` | |
| 4 | `B14_Boss.png` (BOSS arena) | `1c507ac3…` | |
| 5 | `B16_SongSo.png` (digital river, main) | `d1f11795…` | |
| 6 | `B16_SongSo2.jpg` (digital river, temporary test, optional) | `4693fc18…` | |
| 7 | `B18_CongToi.jpg` (dark gate) | `c578fe23…` | |
| 8 | fantasy forest | `d823d7cf…` | |
| 9 | fantasy entrance tunnel (cave with monitors) | `b97b3e97…` | |
| 10 | fantasy gate (outside) | `5aa39a50…` | ✅ `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0` |
| 11 | `B02_Hem1_Day` (alley) | `875ca1de…` | |

## Batch 3: villains and creatures
| # | File | Old ID | New ID |
|---|---|---|---|
| 12 | `20_NguoiXau.png` (villain 1, original) | `aad31f63…` | |
| 13 | `22_NguoiXau2.png` | `6fecf90d…` | |
| 14 | `23_NguoiXau3.png` | `9b267259…` | |
| 15 | `24_NguoiXau4.png` | `23145048…` | |
| 16 | `26_NguoiXau5.png` | `7c314fff…` | |
| 17 | `25_BOss.png` (BOSS giant brain) | `46c623a4…` | |
| 18 | smoke wolf | `f48ff106…` | |
| 19 | crow | `6a271d30…` | |
| 20 | spider | `cdcbdc48…` | |

## Batch 4: other characters and props (only when those scenes are needed)
| # | File | Old ID | New ID |
|---|---|---|---|
| 21 | fantasy dad | `f9500265…` | |
| 22 | fantasy mom | `0d42f68e…` | |
| 23 | security guard | `ecde1ad6…` | |
| 24 | `07_CoGiao` teacher | `082374dd…` | |
| 25 | `08_CoLaoCong` cleaner | `651ece17…` | |
| 26 | police (Công an) | `81cdd17a…` | |
| 27 | `15_TaiXe` bus driver | `6f2ff8e2…` | |
| 28 | blue bus | `e077bd7c…` | |
| 29 | Mai's phone | `66324bdf…` | |
| 30 | mom photo (phone screen) | `d318bcb9…` | |
| 31 | `StandardB.mp4` (real-world scenes only, optional) | `c5746038…` | |

Old generated clips (job IDs in the plan files) stay on the old account; they cannot be used as references from the new account.

## NEW account upload log (workspace `ad401adb-c6e7-47e9-824e-4f7d645dc170`, project MV KMM `11749213-086c-4a29-a963-b5a064eb4af7`)
Status update 2026-10-02: the account DID change (new workspace above, ultra plan). The "NOT NEEDED" note above is outdated; re-upload is in progress.

### BG round 1 — real-world plates (19)
| File | New ID |
|---|---|
| B02_Hem1_Day.png | `c0accc1d-53eb-4d6b-a777-acbac2133117` |
| B02_Hem2_Day.png | `9f47f7d7-7398-40dd-be3b-19a6f3856efe` |
| B02_Hem3_Day.png | `9c8dcde7-b6b5-4148-884b-a3bee58f41ee` |
| B03_PhongMai1_Sunset.png | `e390535f-d97e-4aa4-b4de-a912accabdda` |
| B04_NgaTu1_Day.png | `8b0669a4-c547-4d7d-a776-cb3aa6316de1` |
| B04_NgaTu2_Day.png | `ca849b95-68b8-4727-ad73-1f57f52e97ae` |
| B06_ViaHe1_Day.png | `2dbfcd8a-a452-4b03-bbc0-0e11f3a82f6e` |
| B06_ViaHe2_Day.png | `17d3d211-766e-46c2-9a1f-2e4abe2d2154` |
| B06_ViaHe3_Day.png | `6deba2bf-49ec-46aa-b232-1f048d2da848` |
| B07_Station1_Noon.png | `56d0f801-5d06-40db-ba85-0c485bb5e770` |
| B07_Station2_Noon.png | `32e58526-5e86-4cad-902a-21a20a57875f` |
| B07_Station3_Noon.png | `13f5b48b-4075-4f13-88e8-426ac4913b50` |
| B09_Truong1_Day.png | `b099f6f3-6647-462b-b422-5a78c1e1589e` |
| B10_PhongMai1_Night.png | `55d354f8-c4d2-44f4-9ab2-bda9ad4b8714` |
| B10_PhongMai1_Night2.png | `449270ea-0b5f-4e19-bde7-03b95d29113f` |
| B11_Bep.png | `42e149bb-55ec-4244-b5ec-a7061984b432` |
| B12_Class.png | `e23144fd-d16f-4c4c-aaa8-306b835a1843` |
| B13_HangQuan.png | `1d4b7ca0-82ba-4772-a43b-395438bac493` |
| B13_HangQuan2.png | `41afc209-2130-4cde-bd45-bf337d211332` |

### BG round 2 — remaining plates incl. fantasy (10)
| File | New ID | Note |
|---|---|---|
| B13_HangQuan2.png | `555a718f-836d-41c3-8724-cd945d8f2a1f` | duplicate upload of round 1 `41afc209`; either works |
| B13_HangQuan3.png | `789a5e96-6c50-4d81-82c5-bb153183dc94` | |
| B14_Boss.png | `c8394b3d-556c-4229-a4a4-73daafabcfd9` | BOSS arena (old `1c507ac3`) |
| B14_Boss_Sheet.png | `d42f15fa-c890-462f-9d54-0d55063bcc1b` | BOSS arena sheet |
| B15_TuongManHinh.png | `e2fab0e1-0afa-4726-ab31-3bfa83179a9e` | screen wall (old `f8cfd99c`) |
| B21_MatSauCong.png | `791e7f16-d6aa-4f37-af10-6f89f95a550e` | back of the gate: same screen-wall hall, reverse view toward the entrance gate (2026-10-03) |
| B21_CongFantasy.png | `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0` | FANTASY GATE: where Mai first crosses from the real city into the fantasy world (2026-10-03; old `5aa39a50`). Different from dark gate B18. |
| B16_SongSo.png | `0cc5cb01-897c-4b90-a706-cef1ba043c92` | digital river MAIN (old `d1f11795`) |
| B16_SongSo2.png | `880c4d73-e265-4a88-be8a-66d6fd353f88` | digital river DRAFT/temporary (old `4693fc18`) |
| B17_Hanhlang.png | `409ef811-4f88-4a99-a0ea-bd14a5eab41b` | corridor; possibly the entrance tunnel (old `b97b3e97`), to confirm |
| B18_CongToi.jpg | `7c1e33a4-10da-431a-aec4-b396f2103c77` | dark gate (old `c578fe23`) |
| B19_BOSS.JPG | `65ec906c-0eac-449c-a7fd-78e71f3eb94c` | BOSS plate, new name; role to confirm |

Not yet seen in BG uploads: fantasy forest (old `d823d7cf`). (Fantasy gate uploaded 2026-10-03: `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0`.)

### CH round 1 (20)
| File | New ID | Note |
|---|---|---|
| 01_Mai.png | `fae9baae-3a83-4f65-bfe8-ee32fcc94a78` | real-life Mai (old `b42c82ad`) |
| 01_Mai_FAntasy.png | `0d56fcb2-47cc-4271-b785-c73f4ab9a17b` | **Mai fantasy** (old `ef343c87`) |
| 02_BanDanToc.png | `656bfc6b-74a1-44b9-823d-21b0754c2b1c` | friend |
| 03_BanKinh.png | `7d2e2e14-3460-4f0d-aa90-a3d76888d5f5` | friend |
| 04_BanMap.png | `eb705dd1-e849-4460-9aa1-4561fe91241f` | friend |
| 05_Bo.png | `6c05a666-c64f-4aaa-acec-6056b3ed3b5e` | dad (real) |
| 06_Me.png | `00da7806-ed3f-4a59-8502-756e495480b5` | mom (real) |
| 07_CoGiao.png | `89b32a5e-bfbc-44af-96e9-a274bb04cf51` | teacher (old `082374dd`) |
| 08_CoLaoCong.png | `2f4bb001-827c-4409-8887-3cd734d1b89b` | cleaner (old `651ece17`) |
| 09_AnNinh.png | `682c6b6d-e255-473f-983c-56cc65aab6d3` | security guard (old `ecde1ad6`) |
| 10_CongAn.png | `6afba98a-2c36-4e0d-a373-be24ce4bdc75` | police (old `81cdd17a`) |
| 14_Cho.png | `380caa13-1788-4fe9-b953-c0818719eebc` | dog |
| 15_TaiXe.png | `aed8c835-e2eb-477f-a4c5-583726b87181` | bus driver (old `6f2ff8e2`) |
| 16_Bo_Fantasy.png | `8eeb2595-7127-4d3f-9dc6-9c124caa1c99` | fantasy dad (old `f9500265`) |
| 17_Soi.png | `b5f7908e-fcd3-4b00-ad91-309366da6ae0` | smoke wolf — UPDATED design (prev `d07c926b`, old `f48ff106`) |
| 18_Qua.png | `252cd267-8a39-4bf1-8b69-cefa1ddd56a6` | crow (old `6a271d30`) |
| 19_Nhen.png | `00ac4f6b-39f0-49f3-8a9d-6f56ca30c55c` | spider (old `cdcbdc48`) |
| 20_NguoiXau.png | `ffe68c08-d6b4-469a-9c75-63f7b7b08258` | villain 1 (old `aad31f63`) |
| 21_Me_Fantasy.png | `a6286ab4-eaba-40ed-988f-3452354fe6ce` | fantasy mom (old `0d42f68e`) |
| 22_NguoiXau2.png | `271c1e53-ec7a-4ea9-8573-7003abc37f52` | villain 2 (old `6fecf90d`) |

Still to upload: 23_NguoiXau3, 24_NguoiXau4, 25_BOss, 26_NguoiXau5, bus, phone, mom photo, Fantasy.mp4 master video, fantasy forest. (fantasy gate done 2026-10-03: `22c1d2ad`)

### CH round 2 (7)
| File | New ID | Note |
|---|---|---|
| 20_NguoiXau.png | `9ee934cf-d4a2-4591-a178-9b3805294450` | **used in guides** (round 1 `ffe68c08` also valid) |
| 21_Me_Fantasy.png | `6a337699-bd92-49da-aad9-0c16b6b0c557` | duplicate (guides use round 1 `a6286ab4`) |
| 22_NguoiXau2.png | `075000e7-3a8c-454f-b95e-7ba7db0c2cb4` | **used in guides** (round 1 `271c1e53` also valid) |
| 23_NguoiXau3.png | `7a051c5e-3012-4307-ac81-103174f0a038` | villain 3 |
| 24_NguoiXau4.png | `f448b33f-6e5a-4bd6-b906-bff62ba2bfae` | villain 4 |
| 25_BOss.png | `3db1be87-7da5-4169-b892-e002f1cf2637` | BOSS brain |
| 26_NguoiXau5.png | `4b93a54a-f21a-45f5-8275-7251118e0386` | villain 5 |

Villain pool (5): `9ee934cf` · `075000e7` · `7a051c5e` · `f448b33f` · `4b93a54a`.

### Props + master (4)
| File | New ID | Note |
|---|---|---|
| Fantasy.mp4 | `24430dd0-a7ec-4d5c-a555-46abfb7600a1` | master video; format test job `6a9c8607-5a5c-4bc3-beff-1ce21b2b6e00` (4 s) COMPLETED → works as video_references |
| KMM_PHONE_0930_v001.png | `b7eeb576-8bcf-4a98-b695-48a4e029fda1` | Mai's phone |
| MVKMM_XE BUS_v001_0928.png | `1a436a85-6ed7-4897-96bd-2ba2cdc4b77a` | green bus |
| c02e795c-….png | `5e1895bb-3788-4ee5-ac05-f24f9fd2c228` | unnamed; probably mom photo, to confirm |

### Forest + spider (2)
| File | New ID | Note |
|---|---|---|
| B20_RungFantasy.png | `1bac4a73-28ce-4557-a3b3-148077284b0a` | fantasy forest, updated image 2026-10-02 (replaces `b88078fa`; older `d823d7cf`) |
| 19_Nhen.png | `a01d6370-58c5-4f57-9e49-99938dd25f1a` | spider re-upload; guides now use this (earlier `00ac4f6b` also valid) |

Still missing: StandardB (real-world only). Unconfirmed roles: B17_Hanhlang, B19_BOSS, `5e1895bb` (mom photo?).

| Mai_tuong.png | `46c56ac0-d211-43a9-8660-9de33a4b8a78` | smoky cyan void with tiled floor (new plate, 2026-10-02) |

### Character update (2026-10-04, imported via public GitHub raw URL because the container proxy blocks upload.higgsfield.ai and the upload widget does not render in this client)
| File | New ID | Note |
|---|---|---|
| 30_BoDoi_v2.png | `f5385a7f-1dd1-4e4f-a1a5-1e16aa221d69` | Soldier v2 (replaces `81b7dde9`); file in repo `KMM_options/refs/` |
| 09_AnNinh_v2.png | `6679e746-029e-4286-a4cf-b8d63388eaa8` | Security guard v2 (replaces `682c6b6d`), no cap, no baton |
**Superseded same day by widget uploads (original full-resolution files, same images; guides now use these):**
| File | ID (use this) | Replaces |
|---|---|---|
| 09_AnNinh.png (2688x1152) | `046ff4df-ba34-4695-9ff6-9ea1a40b2faa` | `6679e746` (2000 px import, still valid) |
| 30_BoDOi.png (3120x1328) | `4ef44ef0-12cd-4d15-97b8-983be83cde5d` | `f5385a7f` (2000 px import, still valid) |
