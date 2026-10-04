# KMM: HANDOFF GUIDE (tiếp tục ở box chat khác)

Cập nhật: **2026-10-04**. Repo `cvnhwi/kmm`, branch `claude/gracious-archimedes-cao5q7`, thư mục `KMM_options/`.

**Thứ tự đọc khi mở box chat mới:**
1. `KMM_RULES_SUMMARY.md`. Đây là file ghi nhớ chính, đọc đủ các mục A đến J.
   - **Mục J (feedback draft_1) thắng mọi mục khác nếu mâu thuẫn.**
   - Mục H chứa luật góc BOSS và các việc còn mở.
   - Mục I chứa câu chuyện và raccord.
2. File này: tổng quan, các thao tác kỹ thuật, trạng thái.
3. `STYLE_GUIDE_B.md` (luật đầy đủ) và `CAMERA_LIBRARY_B.md` (mục 8 là director pass).
4. Skill: `.claude/skills/kmm-fantasy-video-prompt/` (bản sao ở `KMM_FANTASY_VIDEO_PROMPT_SKILL.md`) và `.claude/skills/cinematic-director/`.
   - Skill có thể chưa có các update ngày 2026-10-04. Nếu khác nhau thì theo `KMM_RULES_SUMMARY.md`.

`KMM_HANDOFF_30_09.md` ở thư mục gốc là handoff CŨ (thời gen keyframe ảnh, account Higgsfield cũ). Chỉ giữ làm lịch sử.

---

## 1. Dự án và cách làm việc

- **Dự án:** MV hoạt hình 3D "KHÔNG MỘT MÌNH" (KMM), chiến dịch an toàn trẻ em trên mạng.
  - Nhà tài trợ: UNICEF, UNODC, Bộ Công an.
  - User: **Huy PD (Hwi)**, Production Director tại Purple Studio / FLEX Films. Gọi là "anh/chị".
  - Feedback đạo diễn đến qua Huy PD; có nhắc đến "anh Duy".
- **Ngôn ngữ:** trả lời bằng tiếng Việt, viết prompt bằng tiếng Anh.
- **Phạm vi:** chỉ làm cảnh **FANTASY**. Không thêm cảnh đời thường ngoài trời (feedback J).
  - "Mai" hoặc "Mi" luôn là Mai fantasy. Bố và mẹ luôn là bản fantasy.
- **Không bao giờ nói đã kiểm tra nội dung output.** Luôn ghi "chưa kiểm tra nội dung" và đưa checklist theo từng clip.
- **Tự chọn mặc định khi thiếu thông tin**, rồi flag rõ đã chọn gì.
  - **NGOẠI LỆ, luật góc BOSS:** xem mục 4.
- **Quy trình mỗi cảnh:**
  1. Gọi `generate_video_batch`.
  2. Viết file `KMM_options/option_B_<tên>.md` (prompt, thông số, Status SUBMITTED, job id).
  3. Commit và push.
  4. Đặt `send_later` khoảng 8 phút để kiểm tra lại.
  5. Khi job xong: `jobs_wait`, rồi `show_generation_by_ids`.
  6. Đổi Status thành COMPLETED, commit và push.
  7. Báo cáo bằng tiếng Việt kèm checklist.
  - Notification check-in đến sau khi job đã hiện thì chỉ trả lời ngắn.
- **Git:**
  - Push bằng `git push -u origin claude/gracious-archimedes-cao5q7`.
  - Không tạo PR nếu không được yêu cầu.
  - Commit theo trailer attribution của session hiện tại.
  - Không ghi tên model trong commit hay file.

## 2. Higgsfield

| Mục | Giá trị |
|---|---|
| workspace | `ad401adb-c6e7-47e9-824e-4f7d645dc170` (private, gói ultra) |
| project/folder MV KMM | `11749213-086c-4a29-a963-b5a064eb4af7`: **mọi generation vào đây** (`folder_id`). Thư mục con: ENVIRONMENT `242c1f0f…`, VIDEO `380c30d1…`, CHARACTER `cef6ff7a…`, ART STYLE `75dc09e9…`, PROP `d4f6c2d9…` |
| model / mode | `seedance_2_5` / `omni_reference` |
| chất lượng | `draft: true`, `resolution: 480p`, `aspect_ratio: 16:9` |
| âm thanh | `generate_audio: true`. **Chỉ SFX, không nhạc nền.** Khối [Audio] kết bằng "NO music, NO score, NO melody". |
| declined_preset_id | `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Nếu lỗi đòi id khác thì dùng đúng id trong thông báo lỗi (từng dùng `f1821f84-945b-4cd1-9085-1f479db0028e`). |
| media roles | `image_references` (ảnh), `video_references` (video master) |
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

**Video master (luôn đính kèm):** `24430dd0-a7ec-4d5c-a555-46abfb7600a1`

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
| Bác sĩ 27_BacSi | `689fabdb-25e4-4996-8cf7-d0e1d71a0636` | Chỉ thấp thoáng trong đoàn người phe mình |
| Kỹ sư 28_KiSu | `de74362d-250c-4e0f-bab9-9e7b603cb901` | Như trên |
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

Lịch sử đầy đủ nằm trong các file `option_B_*.md`.

## 8. Việc còn mở (ưu tiên từ trên xuống)

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
Tiếp tục dự án MV KMM. Đọc KMM_options/KMM_RULES_SUMMARY.md (đủ mục A–J; mục J feedback draft_1 ưu tiên cao nhất), rồi KMM_options/HANDOFF_GUIDE.md, STYLE_GUIDE_B.md và CAMERA_LIBRARY_B.md (mục 8) trong repo cvnhwi/kmm, branch claude/gracious-archimedes-cao5q7. Dùng skill .claude/skills/kmm-fantasy-video-prompt và .claude/skills/cinematic-director. Trả lời tiếng Việt, prompt tiếng Anh. Mọi video gen vào folder MV KMM 11749213-086c-4a29-a963-b5a064eb4af7. Cảnh fantasy luôn đính kèm video master 24430dd0-a7ec-4d5c-a555-46abfb7600a1 và Mai fantasy 0d56fcb2-47cc-4271-b785-c73f4ab9a17b. Cảnh ở đấu trường BOSS mà tôi không nói bối cảnh thì HỎI tôi chọn góc trong bảng Boss_Angles (HANDOFF mục 4), không tự chọn.
```
