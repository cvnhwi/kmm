# KMM ("KHÔNG MỘT MÌNH"): TỔNG HỢP RULE (đọc file này đầu tiên khi mở box chat mới)

Cập nhật: 2026-10-03. Repo `cvnhwi/kmm`, branch `claude/gracious-archimedes-cao5q7`.
Chi tiết đầy đủ nằm trong skill `.claude/skills/kmm-fantasy-video-prompt/SKILL.md`; bản sao ở `KMM_options/KMM_FANTASY_VIDEO_PROMPT_SKILL.md`, phải luôn giống hệt.
Tham khảo thêm `HANDOFF_GUIDE.md`, `STYLE_GUIDE_B.md`, `REUPLOAD_NEW_ACCOUNT.md`.

> **HAI STYLE (user 2026-10-03):** toàn bộ rule dưới đây = **STYLE B** (fantasy, Mai fantasy). **STYLE A** = đời thực, hand-painted, dùng **01_Mai** (KHÔNG dùng Mai fantasy), prompt mở đầu `DAILY-LIFE MASTER REFERENCE FIRST`. Đọc `STYLE_GUIDE_A.md` + prompt mẫu `STYLE_A_SAMPLE_PROMPT.md`. Branch làm việc hiện tại: `claude/busy-hawking-7f4dok`. Handoff mới nhất: `HANDOFF_2026-10-04_STYLE_A_B.md`.

---

## A. Cách làm việc với Huy PD

1. **Ngôn ngữ:** trả lời bằng tiếng Việt, viết prompt bằng tiếng Anh.
2. **Phạm vi:** chỉ làm cảnh fantasy. "Mai" hay "Mi" luôn là Mai fantasy. Bố và mẹ luôn là bản fantasy.
3. **Không bao giờ nói đã kiểm tra nội dung video hay ảnh.** Luôn ghi "chưa kiểm tra nội dung" và đưa checklist theo từng clip.
4. **Tự chọn mặc định khi thiếu thông tin**, không hỏi lại. Sau đó báo rõ (flag) những gì đã tự chọn hoặc chỗ kịch bản mâu thuẫn. Thiếu thời lượng thì tự chọn theo nhịp cảnh.
5. **Quy trình cho mỗi yêu cầu:**
   1. `generate_video_batch`.
   2. Viết file kế hoạch `KMM_options/option_B_<tên>.md` có Status SUBMITTED kèm job ID.
   3. Commit và push.
   4. Đặt `send_later` khoảng 8 phút để kiểm tra lại.
   5. Khi job xong: `jobs_wait`, rồi `show_generation_by_ids`.
   6. Đổi Status thành COMPLETED, commit và push.
   7. Báo cáo kèm checklist.
6. **Gom việc:** nếu đã có trigger kiểm tra đang chờ thì `update_trigger` để thêm job vào, không tạo trùng. Notification nào báo các job đã hiện rồi thì chỉ trả lời ngắn.
7. **Asset mới:** khi user nói sẽ upload thì mở `media_upload_widget`. Có media_id thì cập nhật skill (cả hai bản), HANDOFF, REUPLOAD (và STYLE_GUIDE nếu cần), rồi commit.
8. **Lỗi bị chặn:** nếu bị flag (nsfw hoặc ip_detected) thì tạo lại một lần với cách viết nhẹ hơn, rồi báo user.
9. **Lỗi kỹ thuật:** `show_medias` của Higgsfield đang lỗi schema, còn CDN ảnh của Higgsfield bị proxy chặn. Không xem được ảnh asset thì gửi user link cloudfront để tự mở.

## B. Thông số Higgsfield (cố định)

| Mục | Giá trị |
|---|---|
| model / mode | `seedance_2_5` / `omni_reference` |
| chất lượng | `draft: true`, `480p`, `16:9` |
| âm thanh | `generate_audio: true`. **Chỉ tiếng động (SFX), KHÔNG nhạc nền.** Mỗi prompt có khối [Audio] kết thúc bằng "NO music, NO score, NO melody". |
| folder | MV KMM `11749213-086c-4a29-a963-b5a064eb4af7` (mọi lần tạo) |
| declined_preset_id | `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Nếu báo lỗi đòi id khác thì dùng id ghi trong thông báo lỗi, ví dụ `f1821f84-945b-4cd1-9085-1f479db0028e`. |
| media roles | `image_references` cho ảnh, `video_references` cho video master |
| thời lượng | 4–30s mỗi clip. Kịch bản dài thì chia thành nhiều clip. |

## C. Cấu trúc prompt

- **Dòng đầu tiên:** `FANTASY MASTER REFERENCE FIRST: Video 1 is the master reference…`
- **Các khối, theo thứ tự (dùng khối nào cần thiết):**
  1. [Generation Goal]
  2. [References], ghi "this IS the location" và "copy exactly; ONE …"
  3. [Geography]
  4. [Action & Camera, time-ordered], mỗi shot có thời gian, cỡ cảnh và chuyển động máy, kết bằng "Cut."
  5. [Villain Look]
  6. [Eyes]
  7. [Villain Variety]
  8. [Crowd Behaviour]
  9. [Running Style]
  10. [Monitors]
  11. [Impact FX]
  12. [Audio]
  13. [Acting]
  14. [Character Look]
  15. [Expression]
  16. [Lighting & Integration]
  17. [Visual Style]
  18. [Avoid]
- **Luôn đính kèm** video master `24430dd0-a7ec-4d5c-a555-46abfb7600a1`.

## D. Luật cứng (theo số rule trong skill)

1. **Phong cách:** 3D stylized cao cấp như video master, có grain, không quá sạch.
2. **Không chữ:** không chữ, số, logo hay giao diện đọc được ở bất cứ đâu (màn hình, biển, đồng phục, khiên, profile card).
3. **Quái vật:** không bao giờ chạm vào Mai.
4. **Tỉ lệ:** trẻ em cao 6–6.5 đầu, người lớn 7–7.5 đầu. Mai không mặc hoodie.
5. **Đám đông không bao giờ chuyển động đồng loạt.**
   - **5a/5c.** Cảnh nào có người xấu: **luôn đính kèm đủ 5 thiết kế người xấu**, xáo thứ tự ảnh. Thêm hai khối:
     - [Villain Variety]: các bóng đen trông khác nhau rõ rệt.
     - [Crowd Behaviour]: lệch nhịp, mỗi bóng một hành động. Kịch bản ghi "đồng loạt" thì viết thành phản ứng lan dần và flag lại.
   - **5b.** Người xấu và thú bóng đêm (sói, quạ, nhện, rắn, bàn tay bóng): **đen trung tính phẳng như bóng đổ**, không khối, không glow hay aura, **KHÔNG TÍM**. Khói là khói đen thường.
   - **5d. KHÔNG CON NGƯƠI, luôn ghi vào prompt.** Áp dụng cho mọi người xấu, thú bóng đêm, bàn tay bóng và BOSS, kể cả khi chỉ ở hậu cảnh. Khối [Eyes]: "small flat almond shape filled with ONE uniform glowing colour… NO black pupil, NO dark dot, NO slit, NO iris". Avoid thêm: pupils, black pupils, dark dots, slit pupils, irises.
   - **5e. Mai chạy kiểu BÉ GÁI YỂU ĐIỆU.** Khối [Running Style]:
     - Bước nhỏ, nảy nhẹ, gần như nhón chân. Cẳng chân hất **sang hai bên** ra sau.
     - Khuỷu tay sát eo, bàn tay lỏng phẩy sang ngang, không vung trước sau.
     - Tóc và váy nảy nhẹ. Tốc độ vừa phải.
     - KHÔNG kiểu vận động viên. Không viết "sprints hard / arms pumping" cho Mai.
6. **Monitor:** phần lớn tối, vài cái chớp ngẫu nhiên, không chớp theo nhịp. Chỉ sáng hết khi user yêu cầu.
7. **Tốc độ:** real-time 24fps, không slow motion hay speed ramp, trừ khi kịch bản ghi rõ (đó là ngoại lệ, phải flag).
8. **Nhiều shot:** khoảng 4–6 hard cut mỗi 15s. Mỗi shot chỉ một chuyển động máy có lý do.
9. **Raccord:** giữ trục 180° và hướng màn hình (chạy trái sang phải) xuyên suốt các cut.
10. **Mai:** da trắng sáng như ref, biểu cảm tiết chế (1/3 đến 2/3), không hét, không há miệng to.
11. **Điện thoại** luôn cầm dọc.
12. **Sàn mờ**, không kẻ caro.
13. **Hòa vào cảnh:** nhân vật khớp ánh sáng, có contact shadow, có sương trước và sau. Không trông như dán lên.
14. **Camera DYNAMIC mặc định.** Phần lớn shot có chuyển động máy. Shot tĩnh tối đa khoảng 1/5, chỉ dùng cho nhịp lặng. Nếu user ghi "fixed" thì khóa máy hẳn.

### Guide action (cảnh đánh nhau)

- **Menu góc máy:** medium, over-the-shoulder từ phía kẻ địch, cận hero, wide, top shot (cẩu xoay), cận quái lao vào ống kính. Thêm: góc thấp hero, insert cú đánh, POV.
- **Hành động dứt khoát:**
  - Mỗi đòn có ba nhịp: lấy đà, đánh, dừng gọn.
  - Khựng hình 2–3 frame khi trúng.
  - Một đòn hạ một kẻ, combo nối liền, cắt cảnh đúng nhịp hành động.
- **Hiệu ứng:**
  - Vệt vàng ấm theo đòn đánh, vòng sóng bụi, chớp trắng vàng.
  - Kẻ địch tan thành khói đen và tàn lửa vàng.
  - Không tím, không máu.
- **Nhân vật:** Bố dùng nắm đấm và cú đá. Mẹ dùng chảo, kiểu vụng về hoặc khéo léo tùy yêu cầu. An ninh dùng dùi cui. Công an dùng khiên hologram.
- **Phong cách drift (khi yêu cầu kiểu "Tokyo Drift"):**
  - Máy đặt thấp sát cản xe, insert cần số và phanh tay, whip pan, nghiêng khung, khói lốp.
  - **Không ghi tên phim vào prompt.**

## E. Chống bị chặn (moderation / IP)

- **Mẹ:** luôn viết "mother character of THIS project (original design: a modern Vietnamese mom in her fantasy outfit)… original character, not based on any existing film or cartoon character", và "ordinary kitchen pan". Avoid: princesses, long golden hair, tower.
- **Robot xe buýt:** thiết kế riêng, ghép từ bộ phận của chính chiếc xe, không logo, không giống robot thương hiệu nào.
- **Khiên hologram:** lục giác cyan trắng viền vàng, không biểu tượng, không giống khiên của nhân vật truyện tranh.
- **Trẻ em:**
  - Tránh trói, xúc tu quấn người, giãy giụa mạnh.
  - Cách viết an toàn: "fully dressed… holds on, not thrashing, family-friendly".
  - Cảnh rơi: "a gentle, floaty fall, caught safely".
  - Tránh "lips part" và "face fills frame" với trẻ em.
- **Không nêu tên phim hay nhân vật có thật** trong prompt.

## F. Bối cảnh

| Bối cảnh | ID | Ghi chú |
|---|---|---|
| Sảnh tường màn hình B15 | `e2fab0e1-0afa-4726-ab31-3bfa83179a9e` | Nhìn về phía tường monitor (phía bắc). Ánh sáng cyan-teal. |
| Mặt sau cổng B21 | `791e7f16-d6aa-4f37-af10-6f89f95a550e` | Cùng sảnh B15 nhưng nhìn ngược về phía cổng. Khi cắt ngược, giữ trục: cổng một bên, tường monitor một bên. |
| **Cổng Fantasy** | `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0` | `B21_CongFantasy.png`: nơi Mai lần đầu bước từ thành phố thực sang thế giới fantasy. **KHÁC Cổng Tối.** |
| Cổng Tối B18 | `7c1e33a4-10da-431a-aec4-b396f2103c77` | Không dùng thay cho Cổng Fantasy. |
| Đấu trường BOSS B14 | `c8394b3d-556c-4229-a4a4-73daafabcfd9` | Khói cyan. BOSS lơ lửng ở phía bắc. |
| Dòng sông số (chính) B16 | `0cc5cb01-897c-4b90-a706-cef1ba043c92` | Sông là HOLOGRAM. Mai đứng trên bờ, qua sông bằng thân gỗ đổ. |
| Dòng sông số test B16_SongSo2 | `880c4d73-e265-4a88-be8a-66d6fd353f88` | |
| Rừng fantasy B20 | `1bac4a73-28ce-4557-a3b3-148077284b0a` | |
| Hẻm | `c0accc1d-53eb-4d6b-a777-acbac2133117` | Luôn là đêm u ám. |
| congtest1 / rungtest1 (TEST) | `6eeba192-23af-4c30-87ac-aad9e0893f8f` / `5f0b9709-7517-42e9-9319-1792a60478cc` | Chỉ để test. Có thể dùng làm tham chiếu thiết kế, không lặp lại khung hình của ảnh. |

## G. Nhân vật và prop

| Vai | ID |
|---|---|
| Video master (luôn kèm) | `24430dd0-a7ec-4d5c-a555-46abfb7600a1` |
| Mai fantasy | `0d56fcb2-47cc-4271-b785-c73f4ab9a17b` |
| Bố fantasy | `8eeb2595-7127-4d3f-9dc6-9c124caa1c99` |
| Mẹ fantasy (chảo) | `a6286ab4-eaba-40ed-988f-3452354fe6ce` |
| Chú an ninh (dùi cui) | `682c6b6d-e255-473f-983c-56cc65aab6d3` |
| Cô giáo (thước, tia vàng) | `89b32a5e-bfbc-44af-96e9-a274bb04cf51` |
| Cô lao công (chổi) | `2f4bb001-827c-4409-8887-3cd734d1b89b` |
| Công an (10_CongAn) | `6afba98a-2c36-4e0d-a373-be24ce4bdc75` |
| Tài xế | `aed8c835-e2eb-477f-a4c5-583726b87181` |
| Xe buýt | `1a436a85-6ed7-4897-96bd-2ba2cdc4b77a` |
| Chó nhà (14_Cho, chó thật, vui vẻ) | `380caa13-1788-4fe9-b953-c0818719eebc` |
| Điện thoại Mai | `b7eeb576-8bcf-4a98-b695-48a4e029fda1` |
| BOSS (bộ não có xúc tu dây cáp) | `3db1be87-7da5-4169-b892-e002f1cf2637` |
| Người xấu 1–5 | `9ee934cf-d4a2-4591-a178-9b3805294450`, `075000e7-3a8c-454f-b95e-7ba7db0c2cb4`, `7a051c5e-3012-4307-ac81-103174f0a038`, `f448b33f-6e5a-4bd6-b906-bff62ba2bfae`, `4b93a54a-f21a-45f5-8275-7251118e0386` |
| Sói bóng đêm (MỚI) | `b5f7908e-fcd3-4b00-ad91-309366da6ae0` |
| Quạ / Nhện | `252cd267-8a39-4bf1-8b69-cefa1ddd56a6` / `a01d6370-58c5-4f57-9e49-99938dd25f1a` |

## H. Việc còn mở

- Chưa rõ vai trò của B17 và B19.
- Ảnh mẹ `5e1895bb` chưa xác nhận.
- Tên file "B21" đang dùng cho hai bối cảnh khác nhau: B21_CongFantasy và B21_MatSauCong.
- Có thể tạo lại các clip cũ để có SFX, đúng nền mới, đúng luật không con ngươi, đúng dáng chạy bé gái.
- Dáng chạy bé gái: nếu tả bằng chữ vẫn chưa đạt thì xin user một video tham khảo chuyển động.
