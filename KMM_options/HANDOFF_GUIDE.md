# KMM — HANDOFF GUIDE (tiếp tục ở box chat khác)

Cập nhật: 2026-10-01 ~16:50 UTC. Repo `cvnhwi/kmm`, branch `claude/gracious-archimedes-cao5q7`, thư mục `KMM_options/`.
Đọc `KMM_RULES_SUMMARY.md` (tổng hợp toàn bộ rule) trước, rồi file này, sau đó đọc `STYLE_GUIDE_B.md` (luật đầy đủ) và `CAMERA_LIBRARY_B.md` (camera, mục 8 = director pass). Skill camera: `.claude/skills/cinematic-director/`.

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
- workspace `ad401adb-c6e7-47e9-824e-4f7d645dc170`
- **TẤT CẢ generation vào folder "MV KMM": `11749213-086c-4a29-a963-b5a064eb4af7`** (truyền `folder_id` mọi lần, kiểm bằng `list_project_assets`). Đây là project MV KMM của account MỚI (dùng chung với team, có sẵn các thư mục con ENVIRONMENT/CHARACTER/VIDEO/ART STYLE). **Luật (user 2026-10-02): MỌI generation đều vào folder gốc "MV KMM" `11749213-086c-4a29-a963-b5a064eb4af7`, không đưa vào thư mục con, không tạo project/folder mới.**
- Model `seedance_2_5`, `mode: omni_reference`, `draft: true`, `resolution: 480p`, `aspect_ratio: 16:9`, `generate_audio: true` (SFX only, no background music: every prompt has an [Audio] block with "NO music"; user rule 2026-10-03), `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- Media roles: `video_references`, `image_references`. Giá ~3 credit/giây (6s≈18, 8s≈24, 15s≈45). Duration 4-30s.
- Dùng `generate_video_batch` (ổn định hơn `generate_video`, hay timeout 60s; nếu timeout → kiểm `list_project_assets` trước khi gửi lại, tránh gen trùng) → `jobs_wait` → `show_generation_by_ids`.
- Upload ảnh/video của user: gọi `media_upload_widget` **một mình trong lượt**, user gửi lại media_id.
- `speedramp` không chỉnh được (luôn "auto") → chống slow motion bằng prompt.
- **Video reference phải là H.264 8-bit yuv420p, có audio track, 720p** (HEVC 10-bit / 854x480 6s từng làm job FAILED không báo lỗi). Kiểm tra/convert bằng `sandbox_exec` (ffprobe/ffmpeg) + `media_upload` (PUT cần header `If-None-Match: *`) + `media_confirm`.

## 3. ID tham chiếu ĐANG DÙNG
> ⚠️ 2026-10-02: ĐÃ ĐỔI sang account Higgsfield MỚI (workspace `ad401adb-c6e7-47e9-824e-4f7d645dc170`, gói ultra; project MV KMM `11749213-086c-4a29-a963-b5a064eb4af7`). Các ID dưới đây đã được thay bằng ID mới (log đầy đủ trong `REUPLOAD_NEW_ACCOUNT.md`). Dòng có ⚠️ = vẫn là ID account cũ, KHÔNG dùng được cho tới khi upload lại. Ảnh mới chưa phân vai: `B17_Hanhlang.png` `409ef811-4f88-4a99-a0ea-bd14a5eab41b` (có thể là hầm lối vào), `B19_BOSS.JPG` `65ec906c-0eac-449c-a7fd-78e71f3eb94c`, `B14_Boss_Sheet.png` `d42f15fa-c890-462f-9d54-0d55063bcc1b`, Bố/Mẹ đời thực `6c05a666-c64f-4aaa-acec-6056b3ed3b5e` / `00da7806-ed3f-4a59-8502-756e495480b5`.

| Vai trò | ID | Ghi chú |
|---|---|---|
| **Video tham khảo FANTASY (master)** | `24430dd0-a7ec-4d5c-a555-46abfb7600a1` (Fantasy.mp4, account mới; test job `6a9c8607` COMPLETED 2026-10-02 → dùng được) | `Fantasy_v2_720p.mp4` (H.264 720p, 6s, audio im lặng), đã test chạy OK. Gốc user `9fb61ba4…` (HEVC, KHÔNG dùng) |
| **Mai fantasy** | `0d56fcb2-47cc-4271-b785-c73f4ab9a17b` | `01_Mai_FAntasy.png` |
| Sói bóng đêm | `b5f7908e-fcd3-4b00-ad91-309366da6ae0` | khói, mắt hổ phách nhỏ, KHÔNG răng |
| Hầm/lối vào fantasy | `b97b3e97-5b27-4deb-92ea-a10693bc61e9` ⚠️(ID account CŨ, chưa upload lại) | vách hang nhiều màn hình cũ |
| Hẻm (relit đêm âm u) | `c0accc1d-53eb-4d6b-a777-acbac2133117` | B02_Hem1_Day, luôn re-lit gloomy night |
| Rừng fantasy | `1bac4a73-28ce-4557-a3b3-148077284b0a` (B20_RungFantasy.png) | Cập nhật 2026-10-02, thay `b88078fa` |
| **Dòng sông số** | `0cc5cb01-897c-4b90-a706-cef1ba043c92` | `B16_SongSo.png` (thay `fa8a5475…`) |
| **Tường màn hình** | `e2fab0e1-0afa-4726-ab31-3bfa83179a9e` | `B15_TuongManHinh.png` (cập nhật lần 4, 2026-10-02; thay `ebb49e7c…`, `54a5db90…`, `b59fa3e7…`, `b5785b69…`, `b331cb43…`) |
| **Mặt sau cổng** (cùng sảnh tường màn hình, nhìn ngược về phía cổng) | `791e7f16-d6aa-4f37-af10-6f89f95a550e` | `B21_MatSauCong.png` (2026-10-03). Dùng cho các cảnh quay về phía cổng: Mai chạy vào, tựa cửa, trốn góc cạnh cửa, góc ngược từ tường màn hình. |
| **Phòng Boss** | `c8394b3d-556c-4229-a4a4-73daafabcfd9` | `B14_Boss.png` (thay `f1ae9d0a…`, `076ec352…`) |
| **Não Boss** | `3db1be87-7da5-4169-b892-e002f1cf2637` | `25_BOss.png` (cập nhật 2026-10-02; thay `9e4e6ae8…`, không dùng lại). Giữ đúng thiết kế trong ảnh |
| **Cổng Fantasy** (Mai lần đầu bước từ thành phố thực sang thế giới fantasy) | `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0` | `B21_CongFantasy.png` (2026-10-03). KHÁC Cổng tối B18. Thay ID cũ `5aa39a50`. |
| Cổng TEST (`congtest1`) | `6eeba192-23af-4c30-87ac-aad9e0893f8f` | `congtest1.jpg` (2026-10-03), chỉ để test, KHÔNG thay Cổng Fantasy |
| Rừng TEST (`rungtest1`) | `5f0b9709-7517-42e9-9319-1792a60478cc` | `rungtest1.jpg` (2026-10-03), chỉ để test, KHÔNG thay Rừng B20 |
| **Cổng tối** (mới) | `7c1e33a4-10da-431a-aec4-b396f2103c77` | `B18_CongToi.jpg` (thêm 2026-10-02, KHÁC Cổng Fantasy) |
| **Người xấu gốc / người bóng đêm** | `9ee934cf-d4a2-4591-a178-9b3805294450` | `20_NguoiXau.png` (cập nhật 2026-10-02; thay `2f07fe73…`, không dùng lại) |
| Người xấu 2 / 3 / 4 / 5 | `075000e7-3a8c-454f-b95e-7ba7db0c2cb4` / `7a051c5e-3012-4307-ac81-103174f0a038` / `f448b33f-6e5a-4bd6-b906-bff62ba2bfae` / `4b93a54a-f21a-45f5-8275-7251118e0386` | `22_NguoiXau2.png` / `23_NguoiXau3.png` / `24_NguoiXau4.png` / `26_NguoiXau5.png` (kho người xấu, dùng random) |
| Quạ / Nhện | `252cd267-8a39-4bf1-8b69-cefa1ddd56a6` / `a01d6370-58c5-4f57-9e49-99938dd25f1a` | |
| Bố fantasy / Mẹ fantasy | `8eeb2595-7127-4d3f-9dc6-9c124caa1c99` / `a6286ab4-eaba-40ed-988f-3452354fe6ce` | |
| Chú an ninh / Cô giáo / Cô lao công / Công an | `682c6b6d-e255-473f-983c-56cc65aab6d3` / `89b32a5e-bfbc-44af-96e9-a274bb04cf51` / `2f4bb001-827c-4409-8887-3cd734d1b89b` / `6afba98a-2c36-4e0d-a373-be24ce4bdc75` | |
| Tài xế xe buýt | `aed8c835-e2eb-477f-a4c5-583726b87181` | 15_TaiXe, KHÔNG phải chú an ninh |
| Xe buýt xanh | `1a436a85-6ed7-4897-96bd-2ba2cdc4b77a` | biển trống, không chữ |
| Điện thoại Mai | `b7eeb576-8bcf-4a98-b695-48a4e029fda1` | ốp xanh da trời, nút vàng, sticker mèo+chó |
| StandardB (video cũ, cảnh đời thực) | `c5746038-2de6-4154-852e-6e431e457aa5` ⚠️(ID account CŨ, chưa upload lại) | không dùng cho cảnh fantasy |
| Mai đời thực (tạm không dùng) | `fae9baae-3a83-4f65-bfe8-ee32fcc94a78` | |

## 4. Luật cứng (mọi prompt)
- Chỉ **style B** (premium stylized 3D). A/C/D đã xoá.
- **Không chữ, số, logo, giao diện đọc được** ở bất cứ đâu (biển, màn hình, profile card).
- Quái vật = khói, mắt hổ phách nhỏ, **không răng**, **KHÔNG BAO GIỜ chạm Mai**.
- Mai không mặc hoodie; trẻ em 6-6.5 đầu, người lớn 7-7.5 đầu; không chibi.
- Sàn mờ, không kẻ ô caro. Sài Gòn 2026, xe máy đội mũ bảo hiểm, chạy bên phải.
- **Người xấu / bóng đen / nhện / sói / quạ / rắn = BÓNG ĐÊM BÌNH THƯỜNG** (user 2026-10-02, cập nhật): đen trung tính phẳng như bóng đổ, KHÔNG ánh chàm/tím, KHÔNG có khối, KHÔNG glow/aura/viền màu/hiệu ứng tím bao quanh, khói (nếu có) là khói đen thường không phát sáng; mắt (nếu có) là hình phát sáng phẳng nhỏ, KHÔNG con ngươi. Dùng khối [Villain Look] trong `STYLE_GUIDE_B.md`.
- **Người xấu / người bóng đen = nhiều ảnh input random** (user 2026-10-02): mỗi khi cảnh có người xấu hoặc người bóng đen, đính kèm NHIỀU ảnh thiết kế người xấu (trộn ngẫu nhiên trong kho ảnh) để đám đông đa dạng; mỗi người bóng vẽ đúng một trong các thiết kế, không tự chế thêm. Kho ảnh (5): `9ee934cf-d4a2-4591-a178-9b3805294450` (20_NguoiXau, gốc mới) · `075000e7-3a8c-454f-b95e-7ba7db0c2cb4` (22_NguoiXau2) · `7a051c5e-3012-4307-ac81-103174f0a038` (23_NguoiXau3) · `f448b33f-6e5a-4bd6-b906-bff62ba2bfae` (24_NguoiXau4) · `4b93a54a-f21a-45f5-8275-7251118e0386` (26_NguoiXau5). **Nhắc lại (user 2026-10-02): LUÔN đính kèm ĐỦ 5 ảnh người xấu** ở mọi cảnh có người xấu/bóng đen (kể cả cảnh chỉ có 1-2 bóng đen ở hậu cảnh), thứ tự ảnh xáo trộn ngẫu nhiên mỗi clip; prompt ghi rõ mỗi bóng đen chọn ngẫu nhiên 1 trong 5 thiết kế, trộn đều, không lặp một thiết kế cho cả đám, không lai. Cận 1 người xấu: vẫn đính kèm đủ 5, chỉ định ngẫu nhiên 1 thiết kế cho nhân vật đó.
- **KHÔNG CON NGƯƠI, LUÔN GHI VÀO PROMPT** (user 2026-10-03): mọi nhân vật bóng đêm, người xấu, thú bóng đêm (sói, quạ, nhện, rắn), bàn tay bóng đêm và BOSS đều KHÔNG có con ngươi. Mỗi prompt có họ (kể cả chỉ thoáng qua hoặc ở hậu cảnh) phải có dòng [Eyes]: mắt là hình hạt hạnh nhân phẳng, phát sáng một màu đều, không con ngươi đen, không chấm tối, không con ngươi dọc, không mống mắt. Avoid luôn thêm "pupils, black pupils, dark dots in the eyes, slit pupils, irises, realistic eyes". Xem rule 5d trong skill.
- **Mai chạy kiểu bé gái YỂU ĐIỆU, NHẸ NHÀNG** (user 2026-10-03, cập nhật): bước nhỏ, nảy nhẹ, gần như nhón chân, hai bàn chân gần nhau; cẳng chân hất sang HAI BÊN ra sau; gối sát; thân trên thẳng, vai mềm; khuỷu tay gập sát eo, cẳng tay hơi mở sang hai bên, bàn tay lỏng ở cổ tay, phẩy qua lại sang ngang (không vung trước-sau); hông vai lắc nhẹ; tóc váy bay nhẹ. Tốc độ vừa phải, mềm mại. KHÔNG kiểu vận động viên. Không viết "sprints hard/arms pumping" cho Mai (skill rule 5e).
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
- **Cảnh sông số: Mai qua sông bằng CÂY GỖ ĐỔ bắc ngang sông** (user 2026-10-02, có ảnh ref): một thân cây cổ thụ đổ nằm ngang vắt qua cả dòng sông từ bờ này sang bờ kia, hơi cao hơn lớp profile; Mai chạy trên mặt thân gỗ, nhìn ngang (side profile) trái → phải, hai tay hơi dang giữ thăng bằng, viền cyan. Hero frame tham khảo: góc thấp ngang từ bờ gần sát mặt sông, thân gỗ trải ngang hết khung, profile trôi ở tiền cảnh dưới gỗ, cây cổ thụ đen nhiều rễ/dây leo hai bên (một cây có gân đỏ), cột sáng cyan phía sau, mây giông. Không dùng cầu xây.
- **Nhện = bóng tối cùng vibe người xấu** (user 2026-10-02): đen trung tính phẳng như bóng cắt (không ánh tím, không viền/aura), không khối, không lông/texture, khói đen mảnh ở chân, mắt phẳng không con ngươi, không răng nanh. Cảnh nhện hù: ưu tiên góc over-shoulder của Mai khi nhện hạ xuống. Rừng: không khí u tối (trời âm u, sương, lạnh).
- Cảnh hẻm: trời **đã âm u sẵn** (mây xám tím, đèn natri/trắng, đường ướt).

## 5. Cấu trúc prompt cảnh FANTASY
Dòng đầu luôn là:
> FANTASY MASTER REFERENCE FIRST: Video 1 is the master reference for the style, mood and characters of this whole clip. Match its render look, materials, colour palette, lighting mood, atmosphere, character design, proportions and animation feel on every frame; do not copy its exact shots, camera or story.

Sau đó các khối: `[Generation Goal]` → `[References]` (Video 1 = style/mood/nhân vật, KHÔNG camera; Image = Mai/sói/bối cảnh, "design only, ONE figure") → `[Space & Blocking]` → `[Action & Camera, time-ordered]` (Shot N (t-t s): START → PEAK → END, "Cut.") → `[Acting]` → `[Character Look]` → `[Expression]` → `[Monitors]` → `[Lighting]` (Match Video 1…) → `[Visual Style]` → `[Avoid]` (luật cứng + lỗi riêng cảnh).
Medias: `video_references` = `24430dd0…` + `image_references` = Mai fantasy + các ref cảnh.

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
Tiếp tục dự án MV KMM. Đọc KMM_options/KMM_RULES_SUMMARY.md trước (tổng hợp rule), rồi KMM_options/HANDOFF_GUIDE.md, rồi STYLE_GUIDE_B.md và CAMERA_LIBRARY_B.md (mục 8) trong repo cvnhwi/kmm, branch claude/gracious-archimedes-cao5q7. Dùng skill .claude/skills/cinematic-director. Trả lời tiếng Việt, prompt tiếng Anh, mọi video gen vào folder MV KMM 11749213-086c-4a29-a963-b5a064eb4af7, cảnh fantasy luôn đính kèm video master 24430dd0-a7ec-4d5c-a555-46abfb7600a1 và Mai fantasy 0d56fcb2-47cc-4271-b785-c73f4ab9a17b.
```
