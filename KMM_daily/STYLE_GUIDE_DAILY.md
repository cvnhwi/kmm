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

Trợ lý không xem được video/ảnh: chưa biết nội dung video DAILY, chỉ mô tả là "look, mood and lighting of Video 1".

## 3. Thông số Higgsfield (mặc định, giống dự án)
`seedance_2_5`, `mode: omni_reference`, `draft: true`, `480p`, `16:9`, `generate_audio: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`, `folder_id: fef878e4-1957-439e-8b50-00a4ee8454c6` (MV KMM). Báo giá trước, chờ user nói "gen".

## 4. Dòng mở đầu prompt (đề xuất, chờ user duyệt)
> DAILY-LIFE MASTER REFERENCE FIRST: Video 1 is the master reference for the style, mood and characters of this whole clip. Match its render look, materials, colour palette, lighting mood, atmosphere, character design, proportions and animation feel on every frame; do not copy its exact shots, camera or story.

## 5. Luật style & cấu trúc prompt
Chờ prompt mẫu của user. Khi nhận được sẽ ghi vào đây (khối prompt, ánh sáng, look, camera, acting).

Luật cứng chung của dự án vẫn áp dụng trừ khi user nói khác: không chữ/số/logo; quái là khói, mắt hổ phách, không răng, không chạm trẻ; Mai không mặc hoodie; trẻ 6-6.5 đầu, người lớn 7-7.5 đầu; Sài Gòn 2026, xe chạy bên phải, đội mũ bảo hiểm; đám đông không chuyển động đồng loạt; real-time 24fps, không slow motion.
