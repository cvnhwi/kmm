# KMM — Re-upload checklist for the NEW Higgsfield account (2026-10-02)

The user switched to a new Higgsfield account. Media IDs are per account, so **every ID in `HANDOFF_GUIDE.md`, `STYLE_GUIDE_B.md` and the skill file belongs to the OLD account** and will not work on the new one. Re-upload the files below. The assistant then replaces each old ID with the new one in all guides and in the skill.

Status: NOT NEEDED (checked 2026-10-02). After reconnecting, Higgsfield shows the SAME private workspace `7d16e180-91e1-4bfc-a35e-8eed97d27b03`: folder MV KMM `fef878e4…` still exists with today's jobs (e.g. `31ee52eb`, `68589847`), so all existing media IDs remain valid. Keep this checklist only for a real account change (different workspace ID).

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
| 10 | fantasy gate (outside) | `5aa39a50…` | |
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
