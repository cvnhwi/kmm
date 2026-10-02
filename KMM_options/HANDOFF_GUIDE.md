# KMM — HANDOFF GUIDE (tiếp tục ở box chat khác)

Cập nhật: 2026-10-01 ~16:50 UTC. Repo `cvnhwi/kmm`, branch `claude/gracious-archimedes-cao5q7`, thư mục `KMM_options/`.
Đọc file này trước, sau đó đọc `STYLE_GUIDE_B.md` (luật đầy đủ) và `CAMERA_LIBRARY_B.md` (camera, mục 8 = director pass). Skill camera: `.claude/skills/cinematic-director/`.

---

## 1. Dự án & cách làm việc
- **Dự án:** MV "KHÔNG MỘT MÌNH" (KMM), 3D animation chiến dịch an toàn trẻ em trên mạng. User: Hwi, PD tại Purple Studio / FLEX Films.
- **Ngôn ngữ:** trả lời user bằng **tiếng Việt**, prompt viết bằng **tiếng Anh**.
- **Thái độ:** chỉ ra yêu cầu thiếu logic và đề xuất cách sửa. Tự chọn mặc định hợp lý khi thiếu thông tin và **nói rõ đã chọn gì**.
- **Không xem được video/ảnh output** → luôn ghi **"chưa kiểm tra nội dung"**, đưa danh sách điểm soi để user tự kiểm.
- **Hiện tại chỉ gen cảnh FANTASY.** Mọi "Mai" user nói = **Mai fantasy**.
- Mỗi cảnh mới: viết plan file `KMM_options/option_B_scene_<tên>.md` (shot table, beat, job id, status), commit + push, đặt `send_later` check ~6-9 phút, khi xong `show_generation_by_ids` + ghi COMPLETED + commit.
- Git: `git push -u origin claude/gracious-archimedes-cao5q7`, không tạo PR. Commit trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` + `Claude-Session: https://claude.ai/code/session_01AeHAmYFd3WvAQ3hbbrqBAo` (session mới dùng link session mới).

## 2. Higgsfield (thông số cố định)
- workspace `7d16e180-91e1-4bfc-a35e-8eed97d27b03`
- **TẤT CẢ generation vào folder "MV KMM": `fef878e4-1957-439e-8b50-00a4ee8454c6`** (truyền `folder_id` mọi lần, kiểm bằng `list_project_assets`). Không dùng project MV KMM khác (`e46399a5…`, `MV_KMM_S26-31`, `VANH_MV KMM`).
- Model `seedance_2_5`, `mode: omni_reference`, `draft: true`, `resolution: 480p`, `aspect_ratio: 16:9`, `generate_audio: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- Media roles: `video_references`, `image_references`. Giá ~3 credit/giây (6s≈18, 8s≈24, 15s≈45). Duration 4-30s.
- Dùng `generate_video_batch` (ổn định hơn `generate_video`, hay timeout 60s; nếu timeout → kiểm `list_project_assets` trước khi gửi lại, tránh gen trùng) → `jobs_wait` → `show_generation_by_ids`.
- Upload ảnh/video của user: gọi `media_upload_widget` **một mình trong lượt**, user gửi lại media_id.
- `speedramp` không chỉnh được (luôn "auto") → chống slow motion bằng prompt.
- **Video reference phải là H.264 8-bit yuv420p, có audio track, 720p** (HEVC 10-bit / 854x480 6s từng làm job FAILED không báo lỗi). Kiểm tra/convert bằng `sandbox_exec` (ffprobe/ffmpeg) + `media_upload` (PUT cần header `If-None-Match: *`) + `media_confirm`.

## 3. ID tham chiếu ĐANG DÙNG
| Vai trò | ID | Ghi chú |
|---|---|---|
| **Video tham khảo FANTASY (master)** | `83190f2e-aa76-490f-8b36-633ff0cfbee6` | `Fantasy_v2_720p.mp4` (H.264 720p, 6s, audio im lặng), đã test chạy OK. Gốc user `9fb61ba4…` (HEVC, KHÔNG dùng) |
| **Mai fantasy** | `ef343c87-2208-435b-ad72-0ad938ae95bd` | `01_Mai_FAntasy.png` |
| Sói bóng đêm | `f48ff106-d9d6-4233-a770-d36f768a1f64` | khói, mắt hổ phách nhỏ, KHÔNG răng |
| Hầm/lối vào fantasy | `b97b3e97-5b27-4deb-92ea-a10693bc61e9` | vách hang nhiều màn hình cũ |
| Hẻm (relit đêm âm u) | `875ca1de-fe82-40c9-aaa3-1fae77e08461` | B02_Hem1_Day, luôn re-lit gloomy night |
| Rừng fantasy | `d823d7cf-984c-4298-a9ab-62cd1b809b0b` | |
| **Dòng sông số** | `d1f11795-f7e4-49bf-9964-9b6c5dcc1015` | `B16_SongSo.png` (thay `fa8a5475…`) |
| **Tường màn hình** | `ebb49e7c-0834-4999-83f0-1c06fcbcc878` | `B15_TuongManHinh.png` (cập nhật 2026-10-02; thay `54a5db90…`, `b59fa3e7…`, `b5785b69…`, `b331cb43…`) |
| **Phòng Boss** | `1c507ac3-2db9-4d1e-b5e0-53fe183687e5` | `B14_Boss.png` (thay `f1ae9d0a…`, `076ec352…`) |
| **Não Boss** | `46c623a4-deab-4a16-a049-98c6cbd558d5` | `25_BOss.png` (cập nhật 2026-10-02; thay `9e4e6ae8…`, không dùng lại). Giữ đúng thiết kế trong ảnh |
| Cổng lớn | `5aa39a50-f435-41b1-8f99-def9153bc90f` | |
| **Cổng tối** (mới) | `c578fe23-9b72-4e39-8dd0-baf8672fd9df` | `B18_CongToi.jpg` (thêm 2026-10-02, không thay cổng lớn) |
| Người bóng đêm | `2f07fe73-628d-4761-aeff-0b32446d8a0c` | |
| Người xấu 2 / 3 / 4 / 5 | `6fecf90d-fe55-4ea6-9c82-d6e5cf418849` / `9b267259-bba3-433f-8af3-1cce21256268` / `23145048-7051-485c-bbac-4d13f240f4d1` / `7c314fff-ebf8-4f30-b1f7-db7b61292d94` | `22_NguoiXau2.png` / `23_NguoiXau3.png` / `24_NguoiXau4.png` / `26_NguoiXau5.png` (kho người xấu, dùng random) |
| Quạ / Nhện | `6a271d30-4602-4348-8042-8728526956c5` / `cdcbdc48-05d0-…` | |
| Bố fantasy / Mẹ fantasy | `f9500265-b7a9-485e-8720-ef2f16f0503c` / `0d42f68e-37cb-44c1-8930-29d212572dbc` | |
| Chú an ninh / Cô giáo / Cô lao công / Công an | `ecde1ad6-151a-42ec-8100-c4cc04573044` / `082374dd-e37b-4a81-b351-9ee0584847f1` / `651ece17-dea7-4131-aa81-5642f5a0121a` / `81cdd17a…` | |
| Tài xế xe buýt | `6f2ff8e2-08c5-47ad-9b71-25fa28d62738` | 15_TaiXe, KHÔNG phải chú an ninh |
| Xe buýt xanh | `e077bd7c-d7dd-4e99-84d8-fe676d544e86` | biển trống, không chữ |
| Điện thoại Mai | `66324bdf-1d17-4e3c-b10e-545427e88712` | ốp xanh da trời, nút vàng, sticker mèo+chó |
| StandardB (video cũ, cảnh đời thực) | `c5746038-2de6-4154-852e-6e431e457aa5` | không dùng cho cảnh fantasy |
| Mai đời thực (tạm không dùng) | `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` | |

## 4. Luật cứng (mọi prompt)
- Chỉ **style B** (premium stylized 3D). A/C/D đã xoá.
- **Không chữ, số, logo, giao diện đọc được** ở bất cứ đâu (biển, màn hình, profile card).
- Quái vật = khói, mắt hổ phách nhỏ, **không răng**, **KHÔNG BAO GIỜ chạm Mai**.
- Mai không mặc hoodie; trẻ em 6-6.5 đầu, người lớn 7-7.5 đầu; không chibi.
- Sàn mờ, không kẻ ô caro. Sài Gòn 2026, xe máy đội mũ bảo hiểm, chạy bên phải.
- **Người xấu / người bóng đen = nhiều ảnh input random** (user 2026-10-02): mỗi khi cảnh có người xấu hoặc người bóng đen, đính kèm NHIỀU ảnh thiết kế người xấu (trộn ngẫu nhiên trong kho ảnh) để đám đông đa dạng; mỗi người bóng vẽ đúng một trong các thiết kế, không tự chế thêm. Kho ảnh (5): `2f07fe73…` · `6fecf90d…` (22_NguoiXau2) · `9b267259…` (23_NguoiXau3) · `23145048…` (24_NguoiXau4) · `7c314fff…` (26_NguoiXau5). Cảnh đám đông: đính kèm cả 5 (hoặc 3-5 ngẫu nhiên); cận 1 người xấu: chọn ngẫu nhiên 1.
- **Đám đông / người bóng tối không bao giờ chuyển động đồng loạt**, mỗi người một hành động, phản ứng lan dần.
- **Màn hình chớp giật ngẫu nhiên; phần lớn TỐI, chỉ vài cái sáng**, không sáng hết, không theo nhịp.
- **Real-time 24fps, KHÔNG slow motion, không speed ramp.**
- **Cut coverage là mặc định** (nhiều shot cắt cứng mỗi clip); **camera chuyển động khi có hành động**.
- Raccord: scene map, trục 180°, hướng màn hình giữ nguyên (hầm: Mai chạy bắc = trái→phải, camera phía đông).
- Ánh sáng: rim light, bounce/spill màu, haze, có grain, không quá sạch; bóng teal-indigo đọc được, không đen kịt.
- Acting thật theo nguyên tắc Disney: phân tích beat; mắt dẫn → đầu → thân; anticipation, follow-through, weight; không đồng bộ.
- **Da Mai trắng sáng như ref** (khối `[Character Look]`), ánh màu chỉ phủ nhẹ, không làm tối da; có fill nhẹ lên mặt.
- **Biểu cảm tiết chế** (khối `[Expression]`): 1/3-1/2 cường độ, miệng chủ yếu khép/hé, mắt chỉ mở to nhẹ, không gurning/há miệng hét/trợn mắt.
- **Dòng sông số là HOLOGRAM**, không phải nước: chạm vào → gợn pixel, scan line, glitch; Mai không đi xuống sông. Profile card bay nhiều lớp tiền/trung/hậu cảnh, xoáy về tâm vòng xoáy.
- Cảnh hẻm: trời **đã âm u sẵn** (mây xám tím, đèn natri/trắng, đường ướt).

## 5. Cấu trúc prompt cảnh FANTASY
Dòng đầu luôn là:
> FANTASY MASTER REFERENCE FIRST: Video 1 is the master reference for the style, mood and characters of this whole clip. Match its render look, materials, colour palette, lighting mood, atmosphere, character design, proportions and animation feel on every frame; do not copy its exact shots, camera or story.

Sau đó các khối: `[Generation Goal]` → `[References]` (Video 1 = style/mood/nhân vật, KHÔNG camera; Image = Mai/sói/bối cảnh, "design only, ONE figure") → `[Space & Blocking]` → `[Action & Camera, time-ordered]` (Shot N (t-t s): START → PEAK → END, "Cut.") → `[Acting]` → `[Character Look]` → `[Expression]` → `[Monitors]` → `[Lighting]` (Match Video 1…) → `[Visual Style]` → `[Avoid]` (luật cứng + lỗi riêng cảnh).
Medias: `video_references` = `83190f2e…` + `image_references` = Mai fantasy + các ref cảnh.

## 6. Director pass (camera tự động, từ skill cinematic-director)
Mỗi cảnh: (1) beat + cảm xúc, (2) chia shot, (3) chọn cỡ cảnh/góc/lens/move/blocking theo động từ kể chuyện, (4) START/PEAK/END mỗi shot, (5) kiểm khả thi + trục, (6) mô tả chuyển động cụ thể (hướng, tốc độ, kết), (7) bỏ move trang trí. Một chuyển động chính mỗi beat. Góc user chỉ định luôn thắng.
Báo user 4 phần: **Lựa chọn đạo diễn / Thiết kế camera (bảng shot) / Prompt / Lỗi cần tránh**. Chi tiết: `CAMERA_LIBRARY_B.md` mục 8.

## 7. Trạng thái các cảnh fantasy gần nhất (tất cả trong MV KMM, chưa kiểm tra nội dung)
| Cảnh | Bản mới nhất | Job | Ghi chú |
|---|---|---|---|
| Cổng/hẻm: sói chờ ngoài hẻm, Mai ở miệng cổng chạy vào hầm, sói vờn, kết low-angle sói nhảy cao (15s) | **v8** | `e0583447-0dae-465e-ba61-885c31a27856` | đúng vị trí user yêu cầu; v7 `7dd6b0c2…` (sói ở cổng) để so sánh |
| Cổng/hẻm 8s sói vờn, chạy tường, nhảy qua đầu | v6 | `03bce19b-794d-4740-9fd4-c9007c5fad5f` | |
| Cổng/hẻm 6s góc chéo | v5 | `7ad9a461-bbb6-496f-9cf8-e729baf035bf` | test đầu video master mới |
| Cổng/hẻm 6s có/không video | v4a / v4b | `a421aa65…` / `84cb13f4…` | so sánh có video và không video |
| Dòng sông số 8s (hologram, profile bay) | **v4** | `e4be08eb-afc7-4259-9aaf-b700fb3a14fe` | các bản cũ: `820fa189` (4s master), `06ab84db` (720p), `93ad9743` (3 ảnh tách), `176120f8` (StandardB) |
| Hầm nối tiếp video tham khảo 8s | | `eea72b65-071e-457f-b597-fe73363652f4` | user đã đánh dấu yêu thích; Mai cũ, chưa có luật da/biểu cảm |
| Mai chạy ra khỏi hầm vào rừng 8s | | `9f95cbe3-7aad-4067-b5e6-3e65b2b102b3` | Mai cũ; đã tự chọn ra rừng fantasy |
| Hang tối rượt 8s / POV sói 8s | | `d284bc73…` / `d85cd34c…` | StandardB, Mai cũ |
Lịch sử đầy đủ trong các file `option_B_*.md`.

## 8. Việc còn mở
- User chọn bản đẹp nhất của cảnh cổng/hẻm (v7/v8) và sông số; đề xuất nếu 15s bị dồn: tách 2 clip 7-8s (sói chờ + Mai chạy / sói vờn + nhảy).
- Gen lại các cảnh fantasy cũ bằng Mai fantasy + video master mới + luật da/biểu cảm (hầm nối tiếp, ra khỏi hầm) nếu user muốn (~24 credit/cảnh).
- Gen lại cảnh Boss / Tường màn hình bằng ảnh nền mới nếu user yêu cầu (báo giá trước).
- Finalize 1080p khi user chọn clip (báo giá trước, dùng `draft_job_id`).

## 9. Prompt mở đầu cho box chat mới (copy dán)
```
Tiếp tục dự án MV KMM. Đọc KMM_options/HANDOFF_GUIDE.md, rồi STYLE_GUIDE_B.md và CAMERA_LIBRARY_B.md (mục 8) trong repo cvnhwi/kmm, branch claude/gracious-archimedes-cao5q7. Dùng skill .claude/skills/cinematic-director. Trả lời tiếng Việt, prompt tiếng Anh, mọi video gen vào folder MV KMM fef878e4-1957-439e-8b50-00a4ee8454c6, cảnh fantasy luôn đính kèm video master 83190f2e-aa76-490f-8b36-633ff0cfbee6 và Mai fantasy ef343c87-2208-435b-ad72-0ad938ae95bd.
```
