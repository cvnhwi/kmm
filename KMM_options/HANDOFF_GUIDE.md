# KMM: HANDOFF GUIDE (tiếp tục ở box chat khác)

Cập nhật: **2026-10-04 (cuối phiên, khoảng 15:45 UTC)**. Repo `cvnhwi/kmm`, branch `claude/laughing-hypatia-z5fhie` (trước đó: `claude/gracious-archimedes-cao5q7`), thư mục `KMM_options/`.

**Thứ tự đọc khi mở box chat mới:**
1. `KMM_RULES_SUMMARY.md`. Đây là file ghi nhớ chính, đọc đủ các mục A đến J.
   - **Mục J (feedback draft_1) thắng mọi mục khác nếu mâu thuẫn.**
   - Mục H chứa luật góc BOSS và các việc còn mở.
   - Mục I chứa câu chuyện và raccord.
2. **`CHARACTER_BIBLE.md`**: mô tả chuẩn từng nhân vật (copy nguyên văn vào prompt) + luật đấu trường BOSS siêu rộng (RULES J.8) + luật mention `@ImageN`/`@Video1` (RULES J.9).
3. File này: tổng quan, các thao tác kỹ thuật, trạng thái.
4. `QA_RULES.md`: linter + checklist + bài học (đọc mục "Known lessons").
5. `STYLE_GUIDE_B.md` (luật đầy đủ) và `CAMERA_LIBRARY_B.md` (mục 8 là director pass).
6. Skill: `.claude/skills/kmm-fantasy-video-prompt/` (bản sao ở `KMM_FANTASY_VIDEO_PROMPT_SKILL.md`) và `.claude/skills/cinematic-director/`.
   - Skill có thể chưa có các update ngày 2026-10-04. Nếu khác nhau thì theo `KMM_RULES_SUMMARY.md`.

**Dùng với LLM/agent khác:** mọi luật, ID và trạng thái nằm trong repo này (không phụ thuộc bộ nhớ chat). Agent mới cần:
- Quyền đọc/ghi repo `cvnhwi/kmm` (clone, commit, push lên branch ghi ở trên hoặc branch phiên mới).
- **Higgsfield MCP** (đã kết nối tài khoản của Huy PD) để gen video/ảnh, `jobs_wait`, `sandbox_exec` (xem frame), `media_upload_widget` (user upload).
- Nếu agent KHÔNG có Higgsfield MCP: chỉ viết request JSON vào `KMM_options/requests/`, chạy linter, rồi đưa JSON cho Huy PD tự submit trên Higgsfield (các trường: model, mode, draft, resolution, aspect_ratio, generate_audio, duration, folder_id, medias, prompt).
- Python 3 để chạy linter `KMM_options/tools/kmm_prompt_qa.py` (không cần thư viện ngoài).

`KMM_HANDOFF_30_09.md` ở thư mục gốc là handoff CŨ (thời gen keyframe ảnh, account Higgsfield cũ). Chỉ giữ làm lịch sử.

---

---

## 0. TÓM TẮT RULE MỚI 2026-10-04 (đọc trước khi viết bất kỳ prompt nào)

| Rule | Nội dung ngắn | Ở đâu |
|---|---|---|
| J.7 | Đoạn phá BOSS = cả team chụm vũ khí/tay vào tâm vòng tròn → shockwave vòng phẳng → cúp điện → não teo, tan khói. Happy ending 3 shot + title (title thêm hậu kỳ). | RULES |
| J.8 | Mô tả kỹ từng nhân vật bằng dòng chuẩn; đấu trường BOSS SIÊU RỘNG (khối [Arena Scale]). | CHARACTER_BIBLE 1-3 |
| J.9 | Mention đúng tag Higgsfield: `@Video1`, `@Image1…@ImageN` theo thứ tự medias; gắn tag cạnh tên mỗi lần nhắc. | RULES, skill 17 |
| J.10 | ĐẾM NGƯỜI: [Head Count] "EXACTLY N", danh sách đánh số, số người mỗi shot; cấm người thừa/đúp. | CHARACTER_BIBLE 4 |
| J.11 | QA BẮT BUỘC trước mỗi lần gen: `python3 KMM_options/tools/kmm_prompt_qa.py <request.json>` = 0 ERROR + checklist `QA_RULES.md`; báo cáo QA cho Huy PD. Không viết tên studio/phim (vd "Disney") trong prompt. | QA_RULES.md |
| J.12 | Cảnh đông người: không cận mặt; mỗi khung tối đa ~3-5 người nhận diện được; chỉ đính kèm ref cho người lộ rõ. | RULES, skill 20 |
| J.13 | Nhiều nhân vật riêng biệt → CẮT THEO NHÓM ≤4 người/shot, giữ raccord (scene map, trục 180°, hướng nhìn, cùng thời điểm/ánh sáng). | RULES, skill 21 |
| J.14 | Video master MỚI `000a36ef` (FANTASY.mp4); MỌI gen vào MV KMM › **FANTASY 2 `08a93ec8-25e5-49aa-83c2-0492790d5567`**. Linter báo lỗi nếu sai. | RULES |
| J.15 | **KHÓA STYLE: mọi nhân vật cùng look 3D như Mai/@Video1 trong MỌI video** (khối [Style Lock] nguyên văn; sheet chỉ là design; bỏ nét vẽ 2D/màu nước/chì). Ngoại lệ: sói/quái bóng đêm = bóng đen phẳng. Linter báo lỗi nếu thiếu. | CHARACTER_BIBLE 5, skill 22 |
| Sói | Sói bóng đêm = bóng đen phẳng, viền tan khói, KHÔNG lông (không bao giờ viết "fur"). | CHARACTER_BIBLE 2 |
| Upload | Widget Higgsfield hiện ĐƯỢC trong phiên này (`media_upload_widget`). Proxy chặn upload.higgsfield.ai nên không upload trực tiếp từ container. | — |

| Sói (chốt cuối) | **Đính kèm sheet sói `b5f7908e` và chép đúng thiết kế** (tai dựng, bờm gai, mõm dài, mắt vàng), toàn thân đen đặc như mực; bờm gai CHỈ là đường viền, không có kết cấu lông; sói TO (vai cao hơn Mai). | CHARACTER_BIBLE 2 |
| Mắt không con ngươi | Khi cận mắt (sói, quái): đặt khối **"EYE RULE (MOST IMPORTANT)"** ngay sau dòng master, nhắc "no pupil" ở mọi khối, KHÔNG viết câu kiểu "focused on its prey". Đã kiểm chứng hiệu quả (wolf profile v2). | QA_RULES (bài học) |
| Scale | Viết khối **[Scale Lock, match @Video1]** với kích thước thật (Mai ~1,4 m; cổng rễ chỉ cao ~2 lần Mai, rộng bằng hẻm; hầm không khổng lồ) và tỉ lệ khung hình (Mai = 1/3, 1/5…). KHÔNG viết "huge gate/giant tunnel". | QA_RULES |
| Góc cực đoan | Góc sát trần / top-down / góc lạ: chữ không đủ, model bị video master kéo về ngang tầm mắt. **Tạo ảnh khung đầu + khung cuối** (gpt_image_2_5) cùng góc, truyền `start_image` + `end_image`, ghi @Video1 "style only, do NOT copy its camera". Camera fixed giữ góc tốt nhất. | QA_RULES |
| Khung tham khảo của user | Ảnh draft có timecode/nhãn cảnh in chữ → KHÔNG đính kèm; mô tả bố cục bằng chữ (hoặc tạo ảnh khung đầu sạch). | — |
| Review | Claude tự review bằng `sandbox_exec`: tải mp4, trích 4 frame (0.3/1.7/3.2/4.7 s), crop phóng to chi tiết (mắt). Báo "đã xem 4 frame" (không phải xem toàn bộ chuyển động); tốc độ/âm thanh để Huy PD đánh giá. | mục 2 |
| Test model khác | Khi Huy PD nói "test, không lưu setting" (vd Seedance 2.0): gen bình thường nhưng KHÔNG ghi vào guide/repo (prompt chỉ ở scratchpad). | — |

**Ref nhân vật cập nhật hôm nay:** An ninh v2 `046ff4df` (không mũ, không dùi cui), Bộ đội v2 `4ef44ef0`, Bác sĩ v2 `23d201b9`, Kỹ sư v2 `ea7e2f28` (kính gọng vuông). Lính cứu hỏa vẫn `94ba28f4` (sheet màu nước). Các sheet 2D/màu nước nên được làm lại bản 3D khi có thể.

**Thư mục/request:** file request JSON đã qua QA lưu ở `KMM_options/requests/`; linter ở `KMM_options/tools/kmm_prompt_qa.py`.

---

## 1. Dự án và cách làm việc

- **Dự án:** MV hoạt hình 3D "KHÔNG MỘT MÌNH" (KMM), chiến dịch an toàn trẻ em trên mạng.
  - Nhà tài trợ: UNICEF, UNODC, Bộ Công an.
  - User: **Huy PD (Hwi)**, Production Director tại Purple Studio / FLEX Films. Gọi là "anh/chị".
  - Feedback đạo diễn đến qua Huy PD; có nhắc đến "anh Duy".
- **Ngôn ngữ:** trả lời bằng tiếng Việt, viết prompt bằng tiếng Anh.
- **Phạm vi:** chỉ làm cảnh **FANTASY**. Không thêm cảnh đời thường ngoài trời (feedback J).
  - "Mai" hoặc "Mi" luôn là Mai fantasy. Bố và mẹ luôn là bản fantasy.
- **Mọi video: tất cả nhân vật cùng một look 3D như Mai/video master** (khối [Style Lock], RULES J.15; linter báo lỗi nếu thiếu).
- **Chỉ báo đúng những gì đã xem:** sau khi job xong, trích 4 frame bằng `sandbox_exec` (mục 2) và báo "đã xem 4 frame" kèm nhận xét ✅/🟡/❌. Không khẳng định về chuyển động, tốc độ hay âm thanh; để Huy PD đánh giá khi xem video. Nếu chưa xem frame thì ghi "chưa kiểm tra nội dung".
- **Tự chọn mặc định khi thiếu thông tin**, rồi flag rõ đã chọn gì.
  - **NGOẠI LỆ, luật góc BOSS:** xem mục 4.
- **Quy trình mỗi cảnh:**
  0. **QA bắt buộc** (RULES J.11): `python3 KMM_options/tools/kmm_prompt_qa.py <request.json>` = 0 ERROR + checklist `QA_RULES.md`.
  1. Gọi `generate_video_batch`.
  2. Viết file `KMM_options/option_B_<tên>.md` (prompt, thông số, Status SUBMITTED, job id).
  3. Commit và push.
  4. Đặt `send_later` khoảng 8 phút để kiểm tra lại.
  5. Khi job xong: `jobs_wait` lấy `result_url`, tải về trong `sandbox_exec` và trích 4 frame để review (không dùng `show_generation_by_ids`: output quá lớn).
  6. Đổi Status thành COMPLETED, commit và push.
  7. Báo cáo bằng tiếng Việt kèm checklist.
  - Notification check-in đến sau khi job đã hiện thì chỉ trả lời ngắn.
- **Git:**
  - Push bằng `git push -u origin <branch của phiên hiện tại>` (phiên 2026-10-04: `claude/laughing-hypatia-z5fhie`).
  - Không tạo PR nếu không được yêu cầu.
  - Commit theo trailer attribution của session hiện tại.
  - Không ghi tên model trong commit hay file.

## 2. Higgsfield

| Mục | Giá trị |
|---|---|
| workspace | `ad401adb-c6e7-47e9-824e-4f7d645dc170` (private, gói ultra) |
| project/folder MV KMM | `11749213-086c-4a29-a963-b5a064eb4af7`. **Từ 2026-10-04 mọi generation vào thư mục con FANTASY 2 `08a93ec8-25e5-49aa-83c2-0492790d5567`** (`folder_id`). Thư mục con: ENVIRONMENT `242c1f0f…`, VIDEO `380c30d1…`, CHARACTER `cef6ff7a…`, ART STYLE `75dc09e9…`, PROP `d4f6c2d9…` |
| model / mode | `seedance_2_5` / `omni_reference` |
| chất lượng | `draft: true`, `resolution: 480p`, `aspect_ratio: 16:9` |
| âm thanh | `generate_audio: true`. **Chỉ SFX, không nhạc nền.** Khối [Audio] kết bằng "NO music, NO score, NO melody". |
| declined_preset_id | `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Nếu lỗi đòi id khác thì dùng đúng id trong thông báo lỗi (từng dùng `f1821f84-945b-4cd1-9085-1f479db0028e`). |
| media roles | `image_references` (ảnh, đánh số @Image1..N theo thứ tự), `video_references` (video master, @Video1), **`start_image` / `end_image`** (khung đầu/cuối, KHÔNG tính vào @ImageN, nhắc bằng chữ "start frame/end frame") |
| ảnh khung đầu/cuối | `generate_image` model `gpt_image_2_5`, quality high, 1k, 16:9, folder FANTASY 2; refs = bối cảnh + nhân vật (+ ảnh khung đầu khi tạo khung cuối: "EXACT same image, only Mai moved") |
| model khác | `seedance_2_0` (mode `std`, 480p, 4-15 s) đã TEST cho cảnh đông người (không lưu setting). Mặc định vẫn là seedance_2_5. |
| thời lượng / giá | 4–30 giây mỗi clip, khoảng 3 credit mỗi giây |

**Thao tác kỹ thuật đã kiểm chứng:**
- **Upload asset của user:** gọi `media_upload_widget` **một mình trong lượt**. User upload xong sẽ gửi lại media_id.
- **Xem ảnh hoặc video asset:**
  - Proxy của container chặn CDN cloudfront.
  - **Dùng `sandbox_exec` của Higgsfield:**
    1. `curl` URL `https://d2ol7oe51mr4n9.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/<media_id>.png` (thử png, jpg, webp).
    2. Dùng ffmpeg thu nhỏ hoặc ghép lưới.
    3. Trả ảnh về bằng `image_paths`: tối đa 4 ảnh, tổng ≤512 KiB, nên dùng 2–3 ảnh mỗi lần.
  - Sandbox bị xóa vài giây sau mỗi lệnh, nên gộp tải và xử lý vào CÙNG MỘT lệnh.
- **Video dài (draft):**
  - User đưa link Google Drive công khai. Tải bằng `https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t` trong sandbox.
  - Trích khung bằng ffmpeg (ví dụ `fps=1/4`, tile 3x3).
  - Video từng bị Higgsfield gắn cờ "nsfw" (job phân tích lỗi, CDN trả 403). Khi đó xin link Drive.
- **Tool lỗi:**
  - `show_medias` đang lỗi schema.
  - `video_analysis_create` hỏng với video bị gắn cờ.
- **Video reference** phải là H.264 8-bit yuv420p, có audio track, 720p. HEVC 10-bit từng làm job FAILED mà không báo lỗi.
- `speedramp` luôn "auto". Chống slow motion bằng prompt.

## 3. Asset ID đang dùng

**Video master (luôn đính kèm):** `000a36ef-3958-42a3-ac67-be28b5139e06`

### 3a. Nhân vật

| Vai | ID | Ghi chú |
|---|---|---|
| Mai fantasy | `0d56fcb2-47cc-4271-b785-c73f4ab9a17b` | Sơ mi trắng, khăn đỏ, váy xanh đen, ba lô xanh nhạt có móc sao, kẹp tóc vàng |
| Bố fantasy | `8eeb2595-7127-4d3f-9dc6-9c124caa1c99` | Áo giáp vest xanh lá + áo phông trắng, bao tay, kính. Tay không. **Bố là người đỡ Mai khi rơi.** |
| Mẹ fantasy | `a6286ab4-eaba-40ed-988f-3452354fe6ce` | Mũ bảo hiểm trắng, áo choàng xanh lá, cầm chảo |
| Chú an ninh **v2** | `046ff4df-ba34-4695-9ff6-9ea1a40b2faa` | Áo kaki ô liu cộc tay, phù hiệu khiên xanh tay trái, không mũ, tóc điểm bạc. Ref mới KHÔNG có dùi cui → tay không. Bản cũ `682c6b6d`. |
| Cô giáo | `89b32a5e-bfbc-44af-96e9-a274bb04cf51` | Áo dài hồng, thước gỗ, tia xanh trắng. Được khen "quá đẹp". |
| Cô lao công | `2f4bb001-827c-4409-8887-3cd734d1b89b` | Nón lá, đồng phục cam, chổi (lửa đỏ hoặc sét đỏ) |
| Công an 10_CongAn **bản mới** | `3f6416ad-4680-4cb2-8913-922c65b2afa2` | Quân phục xanh ô liu, mũ kê-pi. Bản cũ `6afba98a` không dùng cho clip mới. **Xem J.2: vai này chuyển thành an ninh/dân phòng áo bã trầu, chỉ còn cảnh khiên cùng bộ đội. Còn chờ xác nhận đồng phục.** |
| Bộ đội **v2** (30_BoDoi_v2) | `4ef44ef0-12cd-4d15-97b8-983be83cde5d` | Mũ cối sao đỏ, rằn ri, cầu vai vàng 2 sao, phù hiệu cổ súng chéo, giày lính xanh. Bản cũ `81b7dde9`. Làm khiên hologram cùng chú an ninh. |
| Bác sĩ 27_BacSi | `23d201b9-0f1e-465d-b5ab-41b71174eaa6` | Chỉ thấp thoáng trong đoàn người phe mình |
| Kỹ sư 28_KiSu | `ea7e2f28-2923-45fb-8725-72b9df8eea63` | Như trên |
| Lính cứu hỏa 29_LinhCuuHoa | `94ba28f4-68b7-4767-8662-663997434ddb` | Như trên |
| Tài xế 15_TaiXe | `aed8c835-e2eb-477f-a4c5-583726b87181` | Mũ xanh nhạt, ria mép, KHÔNG phải chú an ninh |
| Bạn học sinh béo | `ea2e4e83-b4d6-47bc-b9bd-554fabaeff06` | |
| Bạn học sinh nữ bím tóc | `01c8ad41-09a0-4c26-8605-3b35cabc8ed5` | |
| Chó nhà 14_Cho | `380caa13-1788-4fe9-b953-c0818719eebc` | Chó thật, vui vẻ |
| BOSS (bộ não, xúc tu cáp) | `3db1be87-7da5-4169-b892-e002f1cf2637` | Không con ngươi |
| Người xấu 1–5 (luôn đủ 5, xáo thứ tự) | `9ee934cf-d4a2-4591-a178-9b3805294450`, `075000e7-3a8c-454f-b95e-7ba7db0c2cb4`, `7a051c5e-3012-4307-ac81-103174f0a038`, `f448b33f-6e5a-4bd6-b906-bff62ba2bfae`, `4b93a54a-f21a-45f5-8275-7251118e0386` | |
| Sói bóng đêm / Quạ / Nhện | `b5f7908e-fcd3-4b00-ad91-309366da6ae0` / `252cd267-8a39-4bf1-8b69-cefa1ddd56a6` / `a01d6370-58c5-4f57-9e49-99938dd25f1a` | |
| Xe buýt xanh | `1a436a85-6ed7-4897-96bd-2ba2cdc4b77a` | **Không nhả khói đen.** Có hiệu ứng sức mạnh khi xuất hiện. |
| Điện thoại Mai | `b7eeb576-8bcf-4a98-b695-48a4e029fda1` | |

### 3b. Bối cảnh

| Bối cảnh | ID |
|---|---|
| Đấu trường BOSS B14 (plate chung) | `c8394b3d-556c-4229-a4a4-73daafabcfd9` |
| Sảnh tường màn hình B15 | `e2fab0e1-0afa-4726-ab31-3bfa83179a9e` |
| Mặt sau cổng B21_MatSauCong | `791e7f16-d6aa-4f37-af10-6f89f95a550e` |
| Cổng Fantasy B21_CongFantasy | `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0` |
| Cổng Tối B18 | `7c1e33a4-10da-431a-aec4-b396f2103c77` |
| Dòng sông số B16 | `0cc5cb01-897c-4b90-a706-cef1ba043c92` |
| Rừng fantasy B20 | `1bac4a73-28ce-4557-a3b3-148077284b0a` |
| Hẻm (đêm u ám) | `c0accc1d-53eb-4d6b-a777-acbac2133117` |
| Khung đầu Mai chạy top-down, hầm RỘNG (ảnh gen) | `c87a72ca-3f7a-4914-ace1-be773e0fac11` |
| Khung cuối Mai chạy top-down, hầm RỘNG (ảnh gen) | `b137c3ba-52f3-4d5e-8482-438657831a9e` |
| Khung đầu top-down hầm hẹp (cũ, v5) | `c8b4192b-7d18-4632-8b13-433db79374f3` |

Danh sách đầy đủ và lịch sử ID: `KMM_RULES_SUMMARY.md` mục F, G và `REUPLOAD_NEW_ACCOUNT.md`.

## 4. LUẬT GÓC BOSS (Boss_Angles, 10 góc)

- **KHÔNG tự động dùng** các ảnh góc dưới đây.
- Khi Huy PD yêu cầu một cảnh ở đấu trường BOSS (đặc biệt là đánh nhau hoặc toàn cảnh) **mà không nói rõ bối cảnh hay góc**, phải **HỎI LẠI** dùng góc nào. Liệt kê các góc theo mô tả ngắn để chọn.
- Khi Huy PD đã chỉ định góc hoặc ảnh nền, dùng đúng cái đó.
- Mục đích: góc máy đa dạng nhưng bối cảnh đồng nhất.
- Đây là ngoại lệ của luật "tự chọn mặc định".

| Góc | Mô tả ngắn | ID |
|---|---|---|
| goc01 | Sát sàn, đối xứng, hai tường hội tụ vào sương ở giữa | `184025af-2e7a-4310-a3c2-a147c7e14c8a` |
| goc02 | Thấp, tường trái gần và cao vút, tường phải ở xa | `4abb6caa-95e6-4d4d-be28-6290f918e998` |
| goc03 | Thấp, tường phải gần (ngược của goc02) | `c2c8aab3-3f4e-4c90-b5c2-2cd20eea1de4` |
| goc04 | Từ trên cao chéo khoảng 40°, sàn ướt phản chiếu: dàn trận, bao vây kiểu điện ảnh | `055c0f0a-6861-4817-87ce-84e274d682b4` |
| goc05 | Sát sàn, hơi nghiêng (dutch), kịch tính | `c6e4d549-458a-4d8c-b61f-ebeec563848a` |
| goc06 | Gần chính diện một bức tường (dễ phạm luật không chính diện) | `9c55f7a2-196d-4cb0-af94-8e847e4aed01` |
| goc07 | Góc trong nơi hai tường gặp nhau. **Ảnh có sẵn bóng người, prompt phải ghi bỏ hoặc thay.** | `5f57dedc-521a-419c-8204-197f32f184fe` |
| goc08 | Nhìn qua khe giữa hai khối tường | `63b4cda7-021a-4ec7-9d00-605524699b12` |
| goc09 | Gần thẳng từ trên xuống. Dùng ít vì feedback chê giống game. | `644fe76c-bd26-4318-9114-2c27fc548264` |
| goc10 | Hành lang sâu, quầng sáng teal ở giữa: đoàn người phe mình, luồng sáng liên kết | `f09bcd5a-a196-493d-898b-44dff118a622` |

## 5. Câu chuyện, raccord và feedback (tóm tắt, chi tiết ở RULES mục I và J)

- **Draft_1** (3:46, link Drive `1p8pxPdxQP9Wnw04fktfgPGtwhqIjyjP1`) gồm 6 phần:
  1. Đời thường
  2. Bữa tối cha mẹ không hiểu Mai
  3. Gã bóng đen theo dõi, thế giới méo
  4. Fantasy: rừng, cổng "nội dung độc hại", sảnh tường màn hình
  5. Giải cứu và chiến đấu
  6. Kết: Mai rơi, BOSS, cả nhà ôm nhau, bầu trời nứt
- **Feedback vòng 1 (bắt buộc áp dụng):**
  - Phần đầu cần sửa (flycam, đồng hồ, cảnh trong phòng quá 2D, xe buýt top-shot độ phân giải thấp). Phần fantasy tốt.
  - Không thêm cảnh ngoài trời đời thường, chỉ làm fantasy.
  - Công an chuyển thành an ninh/dân phòng áo **bã trầu**, chỉ còn **cảnh khiên cùng bộ đội**. Không bế bé, không đánh solo, không còng tay. Dân phòng bớt đánh nhau.
  - **Bố đỡ Mai rơi.** Không có cảnh còng tay ở bất cứ đâu.
  - Không ném dùi cui hay đồ an ninh (mặc định Claude: cất dùi cui rồi phóng năng lượng từ tay không, chờ duyệt).
  - Xe buýt: không khói đen, có hiệu ứng sức mạnh khi xuất hiện.
  - **Trận phá BOSS là sức tập thể:** rất đông người phe mình nắm tay, có luồng sáng liên kết, thấp thoáng lính cứu hỏa, bộ đội, bác sĩ, kỹ sư (không kể solo). Không nêu tên phim.
    - Góc máy: toàn cảnh đám quái đối đầu phe mình, góc từ sau lưng quái, góc hơi rộng để đỡ lỗi mặt.
  - Cảnh bị bao vây phải làm cho cinematic, không giống game.
  - Kết: happy ending fantasy, dài hơn.

## 6. Luật cứng và moderation (tóm tắt, chi tiết ở RULES mục D, E)

- **Không chữ, số, logo** ở bất cứ đâu.
- **Quái vật:**
  - Không bao giờ chạm vào Mai.
  - Người xấu và thú bóng đêm: đen trung tính phẳng như bóng đổ, **KHÔNG tím**.
  - **KHÔNG CON NGƯƠI**: luôn có khối [Eyes] và Avoid "pupils…". Áp dụng cho mọi người xấu và BOSS.
- **Mai chạy kiểu bé gái yểu điệu** (khối [Running Style]).
- **Đám đông** không bao giờ chuyển động đồng loạt.
- **Tốc độ và camera:**
  - Real-time 24fps, không slow motion.
  - Camera dynamic. Đấu trường và tường màn hình **không quay chính diện phẳng**.
- **Guide action (cảnh đánh nhau):**
  - Mỗi đòn có ba nhịp: lấy đà, đánh, dừng gọn.
  - Khựng 2–3 frame khi trúng, có flash và vòng bụi.
  - Kẻ địch tan thành khói đen và tàn lửa.
  - Cắt cảnh đúng nhịp hành động. Dùng menu góc máy trong RULES mục D.
- **Moderation:**
  - **Mẹ:** dùng câu "mother character of THIS project (original design)… ordinary kitchen pan".
  - **Trẻ em:**
    - Mặc đủ quần áo.
    - Dây chỉ vòng lỏng qua quần áo, không chạm cổ hay mặt.
    - Không giãy giụa.
    - Rơi nhẹ nhàng, lơ lửng, được đỡ an toàn.
  - **Hào quang vàng toàn thân** từng bị chặn `ip_detected`. Chỉ cho phát sáng ở đốt ngón tay.
  - **Khiên hologram:** lục giác, góc cạnh, kiểu công nghệ. Không vòng tròn, rune hay mandala.
  - Không tên thương hiệu, phim hay nhân vật có thật.
- **Mã màu hiệu ứng:**
  - Sét đỏ `#FF1A1A` `#C8000A` `#FF3B30` `#FFE5E5`.
  - Lửa đỏ `#FF0000` `#E00000` `#B30000` `#FFD6D6`.
  - Khiên vàng `#FFC83D` `#FFE066`.
  - Tia của cô giáo màu xanh trắng (không tím).

## 7. Trạng thái clip gần đây (đều COMPLETED, chưa kiểm tra nội dung)

| Cảnh | File plan | Bản mới nhất (job) |
|---|---|---|
| Bố bị khống chế, bị đánh baton | `option_B_boss_arena_dad_grapple_baton_hit_8s.md` | v2 `f35a9107` |
| Cô giáo bắn tia từ thước | `option_B_boss_arena_three_beams_teacher_ruler_10s.md` | v6 `467754eb` (guide action) |
| Cận mặt cô giáo | `option_B_boss_arena_teacher_closeup_ruler_shots_6s.md` | v3 `f3b9cfe0` |
| Bố mẹ dựa lưng (góc BOSS) | `option_B_boss_arena_corner_parents_back_to_back_6s.md` | v8 `006f5ffc` |
| Bố mẹ dựa lưng, đám đông ùa tới (tường màn hình, góc cao) | `option_B_screenwall_high_angle_crowd_rush_parents_back_to_back_8s.md` | `57049417` |
| An ninh + lao công tạo dáng (góc tối BOSS) | `option_B_boss_arena_dark_corner_guard_holsters_baton_cleaner_twirl_8s.md` | v6 `0a9614b7`. **Ném baton: TRÁI feedback J.3, phải làm lại** |
| An ninh + lao công tạo dáng (tường màn hình / sau cổng) | `option_B_screenwall_guard_arms_crossed_cleaner_broom_twirl_6s.md` / `option_B_backofgate_guard_serious_cleaner_broom_open_gate_8s.md` | `8f259c22` / `431bafcb` |
| An ninh + lao công đánh cùng nhau | `option_B_boss_arena_guard_cleaner_teamup_fire_broom_15s.md` | v8 `c9e6891d` (lửa đỏ, 20s), v7 `2532eeac` (sét đỏ) |
| Đám quái lao về camera | `option_B_boss_arena_villain_crowd_charge_camera_6s.md` | v2 `6993e0a4` |
| 5 người hùng bị bao vây (góc cao) | `option_B_boss_arena_five_heroes_surrounded_high_angle_10s.md` | v3 `2ea00d0e`. **Feedback: giống game, phải làm lại** |
| Công an vào với khiên hologram | `option_B_boss_arena_police_hologram_entrance_three_knockback_8s.md` | v2 `ef45e592`. **Phải làm lại theo J.2 (an ninh + bộ đội cùng làm khiên)** |
| BOSS teo nhỏ | `option_B_boss_shrink_cables_snap_10s.md` | v2 `eaafee63` |
| Mai được đỡ, cả nhà ôm | `option_B_boss_arena_mai_caught_family_hug_light_breaks_15s.md` | v4 `3bc1d1ba`. **Công an đỡ bé: TRÁI J.2, bố phải đỡ** |
| Người hùng khi trời nứt | `option_B_boss_arena_heroes_aftermath_sky_cracks_12s.md` | v2 `43504e31` |
| Mai bị cáp giữ, cáp đứt, rơi | `option_B_boss_arena_mai_cable_snaps_detail_fall_7s.md` | v2 `53ca8e6b` |

**Clip làm ngày 2026-10-04 (cuối phiên), Claude đã xem 4 frame mỗi clip:**

| Cảnh | File plan | Bản mới nhất (job) và tình trạng |
|---|---|---|
| Happy ending (phòng BOSS → đồng cỏ hồng) | `option_B_happy_ending_bossroom_to_meadow_20s.md` | v8 15 s style-lock (xem file). Chờ test lại với sheet Bác sĩ/Kỹ sư mới (~45 credit, chờ lệnh). |
| Sói rượt Mai trong hẻm vào cổng (OTS sau đầu sói) | `option_B_wolf_chase_alley_to_fantasy_gate_ots_6s.md` | v6 `c67f909c`: sói to giống sheet, Mai đứng sẵn ở cổng. Còn: bờm hơi giống lông, Mai nhỏ hơn v5 (v5 `6edd622d` tỉ lệ đúng nhất), camera vẫn xuyên qua cổng cuối clip. Chờ Huy PD chọn. |
| Sói chạy profile cận đầu trong cổng | `option_B_wolf_profile_run_inside_gate_5s.md` | v2 `dd8c89ca`: **ĐẠT** mắt không con ngươi, bóng đêm đen, đúng bố cục. |
| Mai chạy trong hầm, camera sát trần top-down | `option_B_mai_run_inside_gate_topdown_5s.md` | v6 `706263b9`: camera FIXED sát trần, hầm rộng, Mai chạy từ trên xuống, tối, không khói. Có thể cần tăng tốc (Mai chỉ đi ~1/3 khung trong 5 s). Chờ Huy PD xem. |
| TEST tường màn hình (Seedance 2.0) | không lưu file (theo yêu cầu) | v2 `4a3a4fff`: người xấu đúng ref cao gầy, chuyển động rõ; góc chưa cao đủ, đám đông ~15-20 người, áo Mẹ chưa có caro, màn hình còn hình mặt người. |

Lịch sử đầy đủ nằm trong các file `option_B_*.md`.

## 8. Việc còn mở (ưu tiên từ trên xuống)

0. **Mới nhất (2026-10-04 cuối phiên), chờ Huy PD:**
   - Xem Mai chạy top-down v6 `706263b9`; nếu cần nhanh hơn: tạo khung cuối với Mai ở sát mép dưới (hoặc ra khỏi khung) để quãng chạy dài hơn, giữ camera fixed.
   - Chọn bản sói rượt Mai trong hẻm (v5 tỉ lệ đúng / v6 sói giống sheet); nếu làm v7: gộp hai điểm mạnh và dùng ảnh khung đầu để khóa tỉ lệ + cho camera dừng trước cổng.
   - Test tường màn hình Seedance 2.0 v3 nếu Huy PD muốn (góc cao hơn bằng ảnh khung đầu, đám đông xa và dày hơn).
   - Gen lại cảnh đông người 15 s (happy ending v8) với sheet Bác sĩ/Kỹ sư mới, ~45 credit.

1. **Chờ Huy PD xác nhận:**
   - Đồng phục an ninh/dân phòng áo bã trầu: cần ảnh ref, hoặc tạo ref mới.
   - "Đồng phục công an mới" có phải là `3f6416ad` không.
   - Mã số cho Bộ đội.
   - Hành động thay cho ném dùi cui.
2. **Các shot gen lại theo feedback** (RULES J.6). Chưa gen, chờ lệnh:
   1. Dân phòng/an ninh theo ý anh Duy.
   2. Bố đỡ Mai rơi.
   3. Mai chạy vào cổng dark web.
   4. Khiên hologram do bộ đội và an ninh cùng làm.
   5. Đoàn người phe mình đối đầu đám quái, có luồng sáng liên kết.
   6. Làm lại cảnh bị bao vây cho cinematic.
   7. Happy ending fantasy dài hơn.
   - Cảnh ở đấu trường BOSS: **hỏi góc** (mục 4).
3. **Các điểm chưa chắc trong raccord** (RULES I.3).
4. Feedback vòng sau: Huy PD sẽ gửi thêm. Ghi vào RULES mục J (J.x mới).
5. Finalize 1080p khi Huy PD chọn clip: báo giá trước, dùng `draft_job_id`.

## 9. Prompt mở đầu cho box chat mới (copy dán)

```
Tiếp tục dự án MV KMM (repo cvnhwi/kmm, branch claude/laughing-hypatia-z5fhie, thư mục KMM_options/). Đọc theo thứ tự: HANDOFF_GUIDE.md (mục 0 tóm tắt rule mới), KMM_RULES_SUMMARY.md (đủ A–J, J.7–J.15 mới nhất), CHARACTER_BIBLE.md, QA_RULES.md, STYLE_GUIDE_B.md, CAMERA_LIBRARY_B.md (mục 7–8). Dùng skill .claude/skills/kmm-fantasy-video-prompt và .claude/skills/cinematic-director. Trả lời tiếng Việt, prompt tiếng Anh. Video master: 000a36ef-3958-42a3-ac67-be28b5139e06 (@Video1). Mọi gen vào MV KMM › FANTASY 2 08a93ec8-25e5-49aa-83c2-0492790d5567. Mọi nhân vật cùng look 3D như Mai (khối [Style Lock]). Trước mỗi lần gen chạy python3 KMM_options/tools/kmm_prompt_qa.py <request.json> (0 ERROR) + checklist QA_RULES.md. Cảnh ở đấu trường BOSS mà tôi không nói góc thì HỎI tôi chọn góc (Boss_Angles). Góc máy cực đoan (sát trần/top-down) thì tạo ảnh khung đầu + khung cuối trước rồi dùng start_image/end_image. Sau mỗi lần gen, trích 4 frame bằng sandbox_exec để tự review rồi báo tôi kèm checklist. Việc đang dở: xem HANDOFF_GUIDE mục 7 (bảng "Clip làm ngày 2026-10-04") và mục 8 bước 0.
```

Nếu dùng LLM/agent KHÔNG có Higgsfield MCP: thay câu "gen" bằng "viết request JSON vào KMM_options/requests/, chạy linter, đưa JSON cho tôi submit".
