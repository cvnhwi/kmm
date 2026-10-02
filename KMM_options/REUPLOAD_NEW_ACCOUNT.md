# KMM — Re-upload checklist for the NEW Higgsfield account (2026-10-02)

The user switched to a new Higgsfield account. Media IDs are per account, so **every ID in `HANDOFF_GUIDE.md`, `STYLE_GUIDE_B.md` and the skill file belongs to the OLD account** and will not work on the new one. Re-upload the files below. The assistant then replaces each old ID with the new one in all guides and in the skill.

Status: WAITING FOR UPLOADS. Nothing has been re-uploaded yet.

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
