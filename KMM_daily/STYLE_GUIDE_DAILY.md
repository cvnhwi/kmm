# KMM — Style guide DAILY (cảnh đời thường)

Style mới, tách riêng khỏi style B fantasy (`KMM_options/`). Tạo 2026-10-01 ~17:10 UTC. Cảnh đời thường mới và plan file của chúng nằm trong `KMM_daily/`.

## 1. Phạm vi
- Mọi cảnh đời thường: nhà Mai, hẻm, đường phố, trường học, xe buýt bên ngoài, mọi cảnh không phải fantasy.
- Cảnh fantasy vẫn theo `KMM_options/STYLE_GUIDE_B.md`.

## 2. Reference cố định
| Vai trò | media_id | Ghi chú |
|---|---|---|
| **Video master DAILY** | `0e1937c4-209b-4fc7-b110-a0861bf2fd47` | `DAILY_720p.mp4`: H.264 High 8-bit yuv420p, 1280x720, 24 fps, AAC 44.1 kHz, 6.08 s. Convert từ gốc user `812c8476-c81b-4713-9e91-f88c85628518` (DAILY.mp4, HEVC Main 10, 1080p): KHÔNG dùng bản gốc. Gắn làm `video_references` cho MỌI cảnh đời thường. Chưa test gen. |
| **Mai (01_Mai)** | `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` | KHÔNG dùng Mai fantasy. Chờ user xác nhận có character sheet mới không. |

| **Phòng Mai sunset** | `6c670ace-47b0-463f-a0eb-2846fcfdbc1b` | `B03_PhongMai1_Sunset.png` (user upload 2026-10-01). Thay bản cũ `71a09bcb-813d-4888-a25b-1bd5b602a00f`, không dùng bản cũ nữa. Nội dung chưa được trợ lý xem: mô tả là "layout, materials and sunset light of Image N" đến khi user xác nhận chi tiết. |

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
