# KMM — Style guide DAILY (cảnh đời thường)

Style mới, tách riêng khỏi style B fantasy (`KMM_options/`). Tạo 2026-10-01 ~17:10 UTC. Cảnh đời thường mới và plan file của chúng nằm trong `KMM_daily/`.

## 1. Phạm vi
- Mọi cảnh đời thường: nhà Mai, hẻm, đường phố, trường học, xe buýt bên ngoài, mọi cảnh không phải fantasy.
- Cảnh fantasy vẫn theo `KMM_options/STYLE_GUIDE_B.md`.

## 2. Reference cố định
| Vai trò | media_id | Ghi chú |
|---|---|---|
| **Video master DAILY** | `0e1937c4-209b-4fc7-b110-a0861bf2fd47` | `DAILY_720p.mp4`: H.264 High 8-bit yuv420p, 1280x720, 24 fps, AAC 44.1 kHz, 6.08 s. Convert từ gốc user `812c8476-c81b-4713-9e91-f88c85628518` (DAILY.mp4, HEVC Main 10, 1080p): KHÔNG dùng bản gốc. Gắn làm `video_references` cho MỌI cảnh đời thường. Đã test OK: 4 job night friends (e7ec1737, 3f9f1f1b, a04b8d06, 6927b1c2) COMPLETED 2026-10-01. |
| **Mai (01_Mai)** | `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` | KHÔNG dùng Mai fantasy. Chờ user xác nhận có character sheet mới không. |

| **Phòng Mai sunset** | `6c670ace-47b0-463f-a0eb-2846fcfdbc1b` | `B03_PhongMai1_Sunset.png` (user upload 2026-10-01). Thay bản cũ `71a09bcb-813d-4888-a25b-1bd5b602a00f`, không dùng bản cũ nữa. Nội dung chưa được trợ lý xem: mô tả là "layout, materials and sunset light of Image N" đến khi user xác nhận chi tiết. |
| **Prop đồng hồ báo thức** | `b73a2861-966f-4c8d-9b36-e1d8da8a64c4` | Sheet 6 góc (user 2026-10-01): đồng hồ 2 chuông inox bạc bóng, quai cong, búa gõ giữa 2 chuông, 2 chân xoè, mặt đen vạch + số màu kem, kim bạc chỉ 6 giờ, mặt sau 2 núm + công tắc + nắp pin. Trong prompt: "design only, ONE clock", mặt đồng hồ CHỈ vạch chia, KHÔNG số (luật không chữ/số) trừ khi user cho phép. |
| **Lớp học** | `b7451b85-b8fd-469b-bf7b-030a52763921` | `B12_Class.png` (user upload 2026-10-02), thay bản cũ `3b2fcd92-040d-4efe-9654-525dda7dec90`. Nội dung chưa được trợ lý xem. |
| **Hành lang trường** | `b4786353-3cce-4744-952b-06b2fb992c67` | `B17_Hanhlang.png` (user upload 2026-10-02), plate hành lang đầu tiên. Nội dung chưa được trợ lý xem. |
| **Nội thất xe buýt** | `8ee01cf4-4770-4ff1-b5de-39434d458e93` | `B05_Bus1_Day.png` (user upload 2026-10-01). Thay bản cũ `7b04666b-2fe0-41d7-b72d-5d39d89e9a4c`. Ánh sáng ban ngày trong plate được thay theo từng cảnh (vd. hoàng hôn). |

Trợ lý không xem được video/ảnh: chưa biết nội dung video DAILY, chỉ mô tả là "look, mood and lighting of Video 1".

## 3. Thông số Higgsfield (mặc định, giống dự án)
`seedance_2_5`, `mode: omni_reference`, `draft: true`, `480p`, `16:9`, `generate_audio: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`, `folder_id: fef878e4-1957-439e-8b50-00a4ee8454c6` (MV KMM). Báo giá trước, chờ user nói "gen".

## 4. Dòng mở đầu prompt (đề xuất, chờ user duyệt)
> DAILY-LIFE MASTER REFERENCE FIRST: Video 1 is the master reference for the style, mood and characters of this whole clip. Match its render look, materials, colour palette, lighting mood, atmosphere, character design, proportions and animation feel on every frame; do not copy its exact shots, camera or story.

## 5. Luật style & cấu trúc prompt (từ prompt mẫu của user, 2026-10-01, cảnh xe buýt hoàng hôn)
- **Cấu trúc prompt:** dòng DAILY-LIFE MASTER → thời lượng/số shot/real-time → SPINE (1 câu tóm cảnh) → REFERENCES (vai trò từng Video/Image) → PLATE (layout + vật liệu từ plate, ánh sáng thay mới hoàn toàn) → SPACE & BLOCKING → CHARACTERS ("Image N verbatim" + mô tả trang phục/đạo cụ + trạng thái cảm xúc) → SHOT N (thời gian, cỡ cảnh, góc, FOV độ, vị trí trong khung, foreground, First frame → hành động → Ends with…, "Hard cut.") → CAMERA LAW → ACTING → GRADE → STYLE → AUDIO → CONSTRAINTS (dạng đếm: "Count of … : zero/one") → AVOID.
- **Look:** hand-painted finish trên stylized hybrid 3D/2D: watercolour wash, gouache dry-brush, soft cel-shade edge, line sepia-charcoal thưa, không bao giờ đen tuyền. Paper grain thấp, đều, KHÔNG trên da mặt; hatching bút chì màu chỉ trên vải, tóc, ghế, sàn, nền, KHÔNG trên da (mặt, cổ, tay); mặt sạch, đồng đều (chỉ giữ tàn nhang theo thiết kế). Nền phẳng hơn nhân vật. Line weight cố định, không line boil/shimmer/strobe.
- **Camera:** góc máy, FOV (độ), khoảng cách foreground (5-40 cm) ghi cụ thể theo từng cảnh; chuyển động mượt, một hướng, không rung/whip/zoom snap.
- **Grade:** theo mood từng cảnh, nêu màu chủ đạo + nốt ấm duy nhất được phép.
- **Audio:** chỉ diegetic, không nhạc (lưu ý: mặc định `generate_audio: false`, khối AUDIO chỉ có tác dụng khi bật audio).
- **Constraints:** viết dạng đếm (số Mai, số bạn, số shot, số cut, số lần nhìn điện thoại, số chữ đọc được = 0…).
- Vẫn thêm luật dự án: da Mai trắng sáng như ref, biểu cảm tiết chế, đám đông không đồng bộ, real-time 24fps.
- Plan file mẫu: `daily_scene_bus_dusk_phone_6s.md`.

Luật cứng chung của dự án vẫn áp dụng trừ khi user nói khác: không chữ/số/logo; quái là khói, mắt hổ phách, không răng, không chạm trẻ; Mai không mặc hoodie; trẻ 6-6.5 đầu, người lớn 7-7.5 đầu; Sài Gòn 2026, xe chạy bên phải, đội mũ bảo hiểm; đám đông không chuyển động đồng loạt; real-time 24fps, không slow motion.

## 6. Phân tích ref nhân vật chi tiết (user rule 2026-10-01 ~18:00 UTC)
Trước khi viết prompt có nhân vật, phải lập **Character Lock** cho từng nhân vật từ ảnh ref, rồi dùng lại nguyên văn trong khối CHARACTERS của mọi prompt. Không mô tả chung chung ("backpack with a keychain"), phải ghi rõ:
| Hạng mục | Phải ghi |
|---|---|
| Tóc | màu, độ dài, kiểu (mái, buộc, tết), phụ kiện tóc: hình dạng, màu, chất liệu, bên nào |
| Mặt | màu da, màu mắt, hình mắt, đặc điểm (tàn nhang, má hồng, kính: hình gọng, màu gọng) |
| Áo | màu chính, màu viền/cổ/tay, kiểu cổ, khăn quàng (màu, cách thắt) |
| Quần/váy | màu, kiểu (xếp ly, short), độ dài |
| Tất, giày | màu, kiểu, chi tiết (dây, quai) |
| Cặp/ba lô | màu chính + màu phụ, chất liệu (vải, denim, da), quai, túi trước, khóa kéo |
| Móc khóa/charm | hình dạng chính xác, màu, chất liệu, kích thước so với cặp, gắn ở đâu (khóa kéo, quai, bên trái/phải) |
| Đạo cụ khác | điện thoại, bình nước, đồng hồ…: màu, hình in |
- Nguồn: chỉ từ ảnh ref trợ lý đã thực sự xem được, hoặc user xác nhận. Chi tiết chưa chắc ghi "(chưa xác nhận)" và hỏi user, không bịa.
- Trợ lý không tải được ảnh từ Higgsfield (proxy chặn CloudFront 403). Để trợ lý xem ảnh: user đính kèm ảnh ref trực tiếp vào chat.
- Character Lock lưu ở mục 7 của file này, cập nhật khi có ref mới.

## 7. Character Lock (chờ phân tích từ ảnh ref)
Mai (01_Mai `b42c82ad…`), Map (04_BanMap `fd700683…`), Kính (03_BanKinh `fc1b53f9…`), Dân Tộc (02_BanDanToc `2755d89a…`): chưa phân tích từ ảnh. Mô tả đang dùng trong prompt lấy từ prompt mẫu của user (cảnh xe buýt hoàng hôn), chưa đối chiếu ảnh.

## 8. Rim light cinematic, tone vàng (user rule 2026-10-01 ~18:00 UTC)
- Rim light được **tăng mạnh** như phim điện ảnh: viền sáng rõ, liên tục trên tóc, vai, mép mặt và mép quần áo, tách nhân vật khỏi nền; có halation nhẹ quanh viền.
- **Màu rim light: vàng ấm (golden / amber-yellow)**, KHÔNG trắng hồng, KHÔNG trắng sáng lạnh. Áp dụng cả cảnh ngày (nắng vàng xiên) lẫn đêm (đèn natri, đèn bóng vàng). Nguồn sáng phải có lý do (mặt trời, đèn đường, đèn xe, đèn trong nhà).
- Không làm đổi màu da gốc của nhân vật; rim chỉ nằm ở viền.
- Prompt wording: "Strong cinematic rim light: a bright, continuous warm golden-yellow edge light outlining hair, shoulders, cheek and clothing edges, separating every character from the background, with a soft golden halation; the rim is golden amber, never pinkish-white or cold bright white."
- AVOID thêm: "weak or missing rim light, pinkish-white rim, cold white rim, flat frontal lighting".

## 9. Tuổi & khuôn mặt Mai: khoảng 13 tuổi (user rule 2026-10-01 ~18:10 UTC)
- Mai khoảng **13 tuổi** (học sinh THCS). Khuôn mặt **không quá tròn, không baby**: mặt trái xoan thon hơn, cằm và đường hàm thanh nhẹ, má bớt phúng phính, mắt vẫn to nhưng tỉ lệ cân đối hơn, cổ dài hơn chút.
- Tỉ lệ cơ thể: khoảng **6.5–7 đầu** (thay cho 6–6.5 đầu trẻ em ở luật chung). Vẫn trẻ trung, dễ thương, không chibi, không thành người lớn.
- Mặc định của trợ lý: 3 bạn cùng lớp (Map, Kính, Dân Tộc) cùng tuổi ~13, cùng áp dụng tỉ lệ này; giữ nguyên đặc điểm riêng (Map vẫn mặt tròn má hồng nhưng không baby).
- Prompt wording (khối CHARACTER): "Mai is about 13 years old, a lower-secondary student: a slimmer oval face with a gently defined chin and jawline, cheeks less round, large but well-proportioned eyes, a slightly longer neck; body about 6.5 to 7 heads tall; youthful and appealing, never baby-faced, never chibi, never adult."
- AVOID thêm: "baby face, round chubby toddler face, oversized head, short toddler proportions, chibi".

## 10. Khóa 24 fps (user rule 2026-10-01 ~18:20 UTC)
- Mọi video DAILY luôn **24 fps**. Prompt ghi: "locked at 24 fps … natural 24 fps animation timing, no frame interpolation"; AVOID: "frame interpolation, choppy or variable frame rate".
- Seedance không có tham số fps → sau khi gen, kiểm tra file bằng ffprobe (sandbox Higgsfield); nếu khác 24 fps thì báo user (có thể conform bằng ffmpeg nếu user muốn).

## 11. KHÔNG dùng cảnh toàn / đại cảnh (user rule 2026-10-02)
- Mặc định **không dùng** wide shot (WS), extreme wide (EWS), establishing / toàn cảnh, aerial, cảnh lộ sâu hậu cảnh xa. Lý do: góc xa và hậu cảnh xa dễ lộ lỗi, dễ bị nhận ra là AI.
- Cỡ cảnh được phép: **MS (ngang hông), MCU, CU, ECU, insert**; MWS (ngang gối) chỉ khi cần thấy hành động thân dưới (bước đi, ngồi dậy), giữ hậu cảnh gần và mềm (shallow depth of field, có tiền cảnh che).
- Hậu cảnh luôn gần (vài mét), có foreground 5-40 cm che bớt, depth of field nông; không có đường chân trời xa, không đám đông xa, không dãy nhà kéo dài.
- Chỉ dùng cảnh toàn khi user yêu cầu rõ ràng.
- Prompt wording (CAMERA LAW): "No wide, extreme wide or establishing shots: every shot is medium, medium close-up, close-up or insert; backgrounds stay close and softly out of focus; never reveal deep distant background."
- AVOID thêm: "wide shot, extreme wide shot, establishing shot, full-room or full-street view, aerial view, deep distant background, horizon".

## 12. Ban đêm = tối hẳn (user rule 2026-10-02)
- "Buổi tối / ban đêm" mặc định là **trời tối hẳn**, không phải hoàng hôn tím: cửa sổ/khoảng trời là xanh navy rất tối gần đen, chỉ ánh sáng từ đèn thực (đèn trần, đèn bàn, đèn tường, đèn đường) đổ thành vũng sáng. Bóng vẫn đọc được (navy tối), không đen kịt.
- AVOID thêm: "dusk, purple or violet sky, blue-hour sky, sunset glow". Chỉ dùng hoàng hôn khi user nói rõ.
