# KMM ("KHÔNG MỘT MÌNH"): TỔNG HỢP RULE (đọc file này đầu tiên khi mở box chat mới)

Cập nhật: 2026-10-03. Repo `cvnhwi/kmm`, branch `claude/gracious-archimedes-cao5q7`.
Chi tiết đầy đủ nằm trong skill `.claude/skills/kmm-fantasy-video-prompt/SKILL.md`; bản sao ở `KMM_options/KMM_FANTASY_VIDEO_PROMPT_SKILL.md`, phải luôn giống hệt.
Tham khảo thêm `HANDOFF_GUIDE.md`, `STYLE_GUIDE_B.md`, `REUPLOAD_NEW_ACCOUNT.md`.

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
| Công an (10_CongAn, BẢN MỚI 2026-10-04: quân phục xanh ô liu, mũ kê-pi sao vàng, cầu vai đỏ, quần xanh đậm, giày đen) | `3f6416ad-4680-4cb2-8913-922c65b2afa2` (bản cũ `6afba98a` KHÔNG dùng cho clip mới; các file plan cũ giữ nguyên ID cũ như lịch sử) |
| Bác sĩ (27_BacSi: tóc muối tiêu, kính, khẩu trang y tế, áo blouse trắng, ống nghe, sơ mi xanh nhạt, cà vạt xanh đậm) | `689fabdb-25e4-4996-8cf7-d0e1d71a0636` |
| Kỹ sư (28_KiSu: mũ bảo hộ vàng, kính, sơ mi trắng xắn tay, quần âu xám, giày nâu) | `de74362d-250c-4e0f-bab9-9e7b603cb901` |
| Lính cứu hỏa (29_LinhCuuHoa: mũ đỏ, mặt nạ dưỡng khí, đồ chống cháy xanh đậm sọc phản quang vàng, cuộn dây thừng) | `94ba28f4-68b7-4767-8662-663997434ddb` |
| Bộ đội (CHƯA CÓ MÃ SỐ: mũ cối có sao, quân phục rằn ri xanh, cầu vai vàng, giày lính) | `81b7dde9-08f1-46e2-b4b6-8b7b16674fbf` |
| Bạn học sinh béo (khăn đỏ, quần short xanh đen, ba lô xanh đậm có móc) | `ea2e4e83-b4d6-47bc-b9bd-554fabaeff06` |
| Bạn học sinh nữ bím tóc (khăn đỏ, váy xếp ly xanh đen, ba lô jean) | `01c8ad41-09a0-4c26-8605-3b35cabc8ed5` |
| Tài xế | `aed8c835-e2eb-477f-a4c5-583726b87181` |
| Xe buýt | `1a436a85-6ed7-4897-96bd-2ba2cdc4b77a` |
| Chó nhà (14_Cho, chó thật, vui vẻ) | `380caa13-1788-4fe9-b953-c0818719eebc` |
| Điện thoại Mai | `b7eeb576-8bcf-4a98-b695-48a4e029fda1` |
| BOSS (bộ não có xúc tu dây cáp) | `3db1be87-7da5-4169-b892-e002f1cf2637` |
| Người xấu 1–5 | `9ee934cf-d4a2-4591-a178-9b3805294450`, `075000e7-3a8c-454f-b95e-7ba7db0c2cb4`, `7a051c5e-3012-4307-ac81-103174f0a038`, `f448b33f-6e5a-4bd6-b906-bff62ba2bfae`, `4b93a54a-f21a-45f5-8275-7251118e0386` |
| Sói bóng đêm (MỚI) | `b5f7908e-fcd3-4b00-ad91-309366da6ae0` |
| Quạ / Nhện | `252cd267-8a39-4bf1-8b69-cefa1ddd56a6` / `a01d6370-58c5-4f57-9e49-99938dd25f1a` |

## H. Việc còn mở

- Đã có mục I (câu chuyện + raccord từ draft_1). Cần Huy PD đối chiếu các điểm ở I.3 và cập nhật khi draft đổi.
- Nhân vật cập nhật 2026-10-04 đã lên Higgsfield (mục G): 10_CongAn bản mới, 27_BacSi, 28_KiSu, 29_LinhCuuHoa, và thêm một Bộ đội chưa có mã số (cần Huy PD đặt mã và cho biết vai trò). Chưa rõ vai trò của Bác sĩ, Kỹ sư, Lính cứu hỏa trong câu chuyện (draft_1 chưa có họ).
- Chưa rõ vai trò của B17 và B19.
- Ảnh mẹ `5e1895bb` chưa xác nhận.
- Tên file "B21" đang dùng cho hai bối cảnh khác nhau: B21_CongFantasy và B21_MatSauCong.
- Có thể tạo lại các clip cũ để có SFX, đúng nền mới, đúng luật không con ngươi, đúng dáng chạy bé gái.
- Dáng chạy bé gái: nếu tả bằng chữ vẫn chưa đạt thì xin user một video tham khảo chuyển động.

## I. Câu chuyện và raccord (rút từ video draft_1, bản draft mới nhất, dài 3:46)

**Nguồn và độ tin cậy:** rút từ khung hình lấy mỗi 4 giây (1080p, 24fps). Chưa nghe âm thanh/lời bài hát. Cảnh ngắn hơn 4 giây có thể bị sót. Draft sẽ còn sửa nhiều, nên mốc thời gian chỉ là tương đối. Cần Huy PD đối chiếu. Mã cảnh in trên video: `s4.S62-63` (khoảng 1:28 đến 2:32) và `s4.S64` (khoảng 3:36 đến cuối). Có vài dòng chữ ghi chú của editor chồng lên hình, ví dụ ở 2:24: "canh rong hon nguoi me dua chao xuong".

### I.1 Câu chuyện (thứ tự cảnh)

**Phần 1: đời thường (0:00 đến 0:52).** Mai thức dậy với đồng hồ báo thức (0:00), đánh răng (0:04), mẹ nấu ăn trong bếp và Mai ôm mẹ từ phía sau (0:08), ăn bánh mì (0:12). Mai đi qua hẻm (0:16) và chen qua đám học sinh (0:20). Chú công an điều tiết người qua đường (0:24). Mai lên xe buýt xanh cùng bạn béo, cả hai quàng khăn đỏ (0:28 đến 0:36). Xe dừng ở cổng trường có cây phượng (0:36).
- Lớp học: cô giáo mặc áo dài hồng, quay lưng về camera (0:40).
- Sân trường: bạn béo đá bóng (0:44), đám bạn đi chơi (0:48).

**Phần 2: cha mẹ không hiểu (0:52 đến 1:08).**
- Bữa tối buổi tối, quay từ trên cao: bố, mẹ và Mai. Mai cúi vào điện thoại, bố mẹ ăn riêng, không ai nói chuyện (0:52).
- Cận cảnh bố mẹ lo lắng nhìn Mai (0:56).
- Gã bóng đen mắt vàng nhìn máy tính bảng có ảnh Mai (1:00).
- Mai cầm điện thoại ốp hình mèo và chó, có bàn tay đen phủ từ trên xuống (1:04).
- Khuya, Mai nằm lướt điện thoại, đồng hồ gần 12 giờ (1:08).

**Phần 3: thế giới thật bắt đầu méo (1:12 đến 1:28).** Mai đứng ở cửa lớp, mặt căng thẳng (1:12). Cận cảnh Mai hốt hoảng (1:16). Màn hình "MOM CALL" (1:20). Cô lao công đội nón lá, cầm cán chổi, nét mặt lo lắng (1:24).

**Phần 4: rơi vào thế giới fantasy (1:28 đến 2:20).** Mai đứng sau lưng, hai bên có xúc tu đen (1:28). Con sói bóng đêm ở cuối đường (1:32). Mai chạy trong rừng tối trên con đường giấy phát sáng, có rễ đỏ và tia sáng xanh phía trước (1:36 đến 1:52). Cánh cổng như cửa sổ trình duyệt khổng lồ ghi "nội dung độc hại" (1:56). Sảnh tường màn hình (B15) với các bóng đen cầm máy tính bảng (2:00). Mai khóc, mặt sáng lên vì ánh điện thoại (2:04). Bàn tay đen đặt lên vai rồi bịt miệng Mai (2:08 đến 2:16). Cảnh từ trên cao: Mai nhỏ xíu giữa các bóng bò quanh (2:20).

**Phần 5: giải cứu và chiến đấu (2:24 đến 3:20).**
- Nổ lửa, bố fantasy và mẹ fantasy xuất hiện (2:24). Mai bị treo bằng dây cáp từ trên cao (2:32).
- Bố mẹ hoảng sợ, rồi bố đánh nhau và bị người xấu khống chế (2:36 đến 2:44). Người xấu cầm baton đứng sau lưng bố (2:44).
- Cô giáo vung thước gỗ (2:52). Chú công an xanh lá, nắm đấm phát sáng (2:56). Trong cảnh 3:00, nhóm 5 người đứng dựa lưng nhau giữa vòng vây, quay từ trên cao.
- Chớp trắng, bóng đen mắt vàng tan rã (3:04 đến 3:08). Chú tài xế xe buýt vẫy tay trong cabin xe sáng (3:12). Khiên vàng hologram của công an, có tàn lửa (3:16). Tường màn hình có tia lửa đỏ (3:20).

**Phần 6: kết (3:24 đến 3:46).** Mai rơi từ trên cao xuống trong cột sáng (3:24). BOSS bộ não (3:28). Bố quỳ mở tay đón Mai, có chó con, mẹ đứng cạnh (3:32). Bầu trời nứt, tia sét vàng chạy dọc tường màn hình, nắng xuyên vào (3:36, mã `S64`). Chú công an và chú mặc áo xanh nhạt đội mũ xanh đặt tay lên vai nhau, cười (3:40). Cận cảnh cô giáo mỉm cười (3:44).

### I.2 Raccord (giữ nhất quán giữa các cảnh)

**Mai**
- Đồ ngủ và ở nhà: áo phông vàng.
- Ra ngoài và cả thế giới fantasy: sơ mi trắng, khăn quàng đỏ, váy xanh đen, ba lô xanh nhạt có móc khóa hình ngôi sao, kẹp tóc vàng. Giữ đủ các món này trong mọi cảnh fantasy (xem 2:04 đến 2:32).
- Điện thoại ốp hình mèo và chó.

**Bố và mẹ**
- Đời thường: bố tóc muối tiêu, đeo kính, áo phông trắng. Mẹ búi tóc, tạp dề xanh lá.
- Fantasy: bố mặc áo giáp vest xanh lá kèm áo phông trắng, có bao tay, vẫn đeo kính. Mẹ đội mũ bảo hiểm trắng, khoác áo choàng xanh lá.
- Bố không vũ khí (đấm tay không). Mẹ dùng chảo.

**Các nhân vật khác**
- Cô giáo: áo dài hồng, tóc buộc thấp. Cầm thước gỗ trong cảnh fantasy.
- Cô lao công: nón lá quai tím, đồng phục cam có sọc phản quang. Cầm cán chổi.
- Chú công an: quân phục xanh lá, mũ có sao đỏ. Đánh bằng nắm đấm phát sáng, khiên hologram vàng.
- Chú tài xế: mũ xanh nhạt, ria mép, xe buýt xanh lá.
- Bạn béo: khăn đỏ, ba lô có gấu bông.
- Chú mặc áo xanh nhạt, mũ xanh, ria mép, có thẻ tên ở ngực (3:40): chưa chắc là chú an ninh hay tài xế, cần user xác nhận.

**Kẻ xấu**
- Bóng đen phẳng, mắt vàng, không con ngươi.
- Sói bóng đêm xuất hiện ở 1:32.
- BOSS là bộ não đen có xúc tu cáp, xuất hiện ở 3:28.

**Ánh sáng và tông màu**
- Cảnh đời thường (0:00 đến 0:48): sáng ấm, nắng vàng.
- Bữa tối (0:52): đèn vàng ấm, cửa sổ xanh tối.
- Từ 1:28: lạnh, xanh lơ/teal, có sương mù. Nhịp này kéo dài đến hết 3:20.
- Kết (3:36 trở đi): bầu trời xanh thật, nắng xuyên qua vết nứt, ấm lại. Chỉ vết nứt có màu vàng.

**Hướng và bố cục**
- Cảnh sảnh tường màn hình và đấu trường BOSS luôn chụp xiên hoặc từ trên cao, không chính diện.
- Cảnh vòng vây 5 nhân vật (3:00) và Mai nhỏ giữa bóng đen (2:20) đều quay từ trên cao.

### I.3 Điểm chưa chắc, cần Huy PD xác nhận
- Thứ tự cuối: Mai rơi (3:24) rồi BOSS (3:28) rồi cả nhà ôm (3:32). Cần xác nhận BOSS xuất hiện trước hay sau cảnh Mai rơi.
- Danh tính chú áo xanh nhạt ở 3:40 (an ninh hay tài xế).
- Chú công an ở 2:56 so với cảnh ôm ở 3:40: cùng một người hay không.
- Các dòng chữ ghi chú của editor (ví dụ 2:24) có giữ lại hay không.
- Âm thanh, lời bài hát và nhịp nhạc chưa được kiểm tra.
