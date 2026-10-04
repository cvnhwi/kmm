# 04 — Mẫu xuất kết quả

## 1. Khung trả lời chuẩn

```
## 1. Tóm tắt
- Logline: …
- Theme: …
- Arc cảm xúc: [giá trị đầu] → [giá trị cuối]
- Thời lượng / tỉ lệ / BPM: …

## 2. Visual strategy
- Giọng đạo diễn tham chiếu: A (cho phần …), B (cho phần …) — lý do
- Quy tắc máy theo arc: Hồi I …, Hồi II …, Hồi III …
- Color script: …
- Motif: …

## 3. Shot list
(bảng — xem mục 2)

## 4. Điểm cần duyệt
- [đề xuất] … (chỗ mình thêm vào ngoài kịch bản)
- Câu hỏi: …
```

## 2. Bảng shot list

| # | Beat (trích KB) | Cỡ | Góc | Lens | Máy | Chuyển động | Thời lượng | Nội dung hình | Ý đồ kể chuyện | Âm thanh / Nhạc | Chuyển cảnh | Ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1A | "…" | EWS | High | 24mm | DYNAMIC | Crane down chậm | 4s | … | Giới thiệu thế giới | Intro piano | Cut | Villeneuve |
| 1B | "…" | MCU | Eye-level (trẻ) | 50mm | FIXED | Locked-off | 3s | … | … | … | L-cut | Kore-eda |

Quy ước:
- **#**: số cảnh + chữ cái cho shot (1A, 1B…). Shot đề xuất thêm ghi `1C*` và cột Nội dung bắt đầu bằng `[đề xuất]`.
- **Máy**: FIXED hoặc DYNAMIC (viết hoa để đọc nhanh tỉ lệ).
- **Chuyển động**: 1 động tác chính; nếu dynamic ghi rõ điểm đầu → điểm cuối ("từ WS sau lưng Mai → MCU khi cô quay lại").
- **Ref**: đạo diễn/phim tham chiếu (tùy chọn, giúp đội hiểu nhanh).

Bản rút gọn (khi người dùng chỉ cần nhanh):
`1A · EWS · high · crane down · 4s — Hẻm Sài Gòn sáng sớm, mái tôn, cây; máy hạ xuống cửa nhà Mai. (Giới thiệu thế giới an toàn)`

## 3. Mẫu prompt keyframe (ảnh tĩnh)

Cấu trúc: **[Ref ảnh] + [Style] + [Location/plate] + [Ánh sáng/giờ] + [CAMERA] + [Hành động/biểu cảm] + [Trang phục] + [Nhân vật/đạo cụ khác] + [Negative/luật dự án]**

Câu CAMERA viết theo thứ tự: shot size → angle → lens → composition → depth.
```
Camera: medium close-up, eye-level at child height, 50mm lens feel, Mai placed on the right third looking left into negative space, shallow depth of field, the doorway behind her out of focus.
```

Từ vựng camera tiếng Anh hay dùng:
- Size: extreme wide shot, wide shot, full shot, medium wide shot, medium shot, medium close-up, close-up, extreme close-up, insert shot of …
- Angle: eye-level, child's eye-level (camera at 1m), low angle looking up, high angle looking down, top-down overhead, dutch angle tilted 10 degrees, over-the-shoulder from behind X, point-of-view from X, through a half-open door, framed by a window
- Lens: ultra-wide 16mm distortion, wide 24mm, natural 35mm, 50mm, 85mm portrait, long telephoto 200mm compressed background
- Composition: symmetrical one-point perspective, rule of thirds, centered, lots of negative space, frame within a frame, foreground silhouette, layered foreground/midground/background, low horizon, character small in frame
- Depth/light: deep focus, shallow depth of field, rack focus (video), backlit silhouette, rim light, practical lamp light, cold screen glow on face, warm tungsten interior, golden hour, blue hour

## 4. Mẫu prompt video AI (image-to-video / text-to-video)

Quy tắc cho video AI (Higgsfield, Kling, Veo, Runway, Seedance…):
- **1 chuyển động máy + 1 hành động nhân vật** mỗi clip (3–5s). Phức tạp hơn → chia shot.
- Mô tả *khung đầu → khung cuối* nếu là dynamic.
- Dùng tên chuyển động chuẩn: `static locked-off camera`, `slow dolly in`, `slow push-in`, `dolly out / pull back`, `truck left/right`, `tracking shot following from behind`, `leading shot walking backwards in front of`, `pan left/right`, `tilt up/down`, `crane up / pedestal up`, `crane down`, `slow orbit 90 degrees around`, `handheld subtle shake`, `whip pan`, `crash zoom`, `dolly zoom (vertigo effect)`, `rack focus from foreground to background`, `FPV drone fly-through`.
- Ghi tốc độ: `very slow`, `slow`, `smooth`, `fast`, `sudden`.
- Ghi những gì GIỮ NGUYÊN: `character design and art style stay consistent, no morphing`.

Mẫu:
```
[Start frame: Image 1]. Slow dolly in from medium shot to close-up on Mai's face over 4 seconds. Mai slowly lowers her phone, her eyes widen as she realizes something; cold blue screen light fades from her face. Background stays still. Camera movement smooth and steady, no cuts. Keep the same art style, character design, and lighting as Image 1. No text, no numbers.
```

## 5. Ví dụ hoàn chỉnh (minh họa)

**Kịch bản gốc (giả định):**
> Đêm. Mai nằm trên giường lướt điện thoại. Một "người bạn" lạ nhắn tin, tặng quà game. Bóng sói xuất hiện ở góc phòng. Bố mẹ ở phòng khách không biết.

**Beat:** (1) Mai một mình, an toàn giả → (2) tin nhắn đến: tò mò → (3) quà: hấp dẫn → (4) bóng sói: nguy hiểm khán giả thấy, Mai không thấy → (5) bố mẹ không hay biết: bất lực.

**Visual strategy:** Wong Kar-wai (cô đơn trong ánh màn hình) + Hitchcock (khán giả biết nhiều hơn) + Spielberg/Jaws (giấu quái). Fixed chiếm chủ đạo, chỉ 2 cú dynamic: push-in khi nhận quà, rack focus lộ sói.

| # | Beat | Cỡ | Góc | Lens | Máy | Chuyển động | TL | Nội dung | Ý đồ | Âm thanh | Chuyển |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1A | Đêm, Mai lướt ĐT | WS | High, góc trần phòng | 24mm | FIXED | Locked-off | 4s | Phòng tối, Mai nhỏ trên giường, nguồn sáng duy nhất là màn hình | Cô lập, nhỏ bé | Ambient, quạt trần | Cut |
| 1B | " | MCU | Eye-level, nằm ngang | 50mm | FIXED | — | 3s | Mặt Mai nghiêng trên gối, ánh xanh màn hình | Thế giới thu vào màn hình | — | Cut |
| 2A | Tin nhắn lạ | Insert | POV Mai | 85mm | FIXED | — | 1.5s | Màn hình: bong bóng chat sáng lên (KHÔNG chữ, chỉ hình icon/ánh sáng) | Lời gọi | Tiếng "ting" | Cut on sound |
| 2B | " | CU | Eye-level | 50mm | FIXED | — | 2s | Mắt Mai sáng lên, khẽ cười | Tò mò | — | Cut |
| 3A | Tặng quà game | MCU→CU | Eye-level | 35mm | DYNAMIC | Slow push-in | 4s | Ánh sáng màn hình chuyển ấm vàng giả tạo, quà lấp lánh phản chiếu trong mắt | Bị cuốn hút (Scorsese/No-Face) | Nhạc lấp lánh | Cut |
| 4A | Bóng sói | MS | Eye-level, Mai foreground nét | 35mm | DYNAMIC | Rack focus từ Mai ra góc phòng | 4s | Mai nét → mờ; góc tối hậu cảnh nét: bóng khói sói, mắt hổ phách, ở xa, không chạm | Khán giả biết, Mai không (Hitchcock) | Nhạc tụt, trầm rền | Cut |
| 4B* | [đề xuất] | ECU | — | Macro | FIXED | — | 1s | [đề xuất] Móc sao vàng trên ba lô treo ghế, bóng tối đang phủ dần lên | Gieo motif ngôi sao | — | L-cut tiếng TV |
| 5A | Bố mẹ không biết | WS | Through-frame qua khe cửa phòng Mai | 50mm | FIXED | — | 4s | Qua khe cửa: phòng khách sáng ấm, bố mẹ xem TV, quay lưng | Ngăn cách hai thế giới (ấm/lạnh) | Tiếng TV nhỏ | Cut |
| 5B | " | EWS | Mặt cắt ngang nhà (dollhouse) | 28mm | DYNAMIC | Very slow truck ngang từ phòng khách sang phòng Mai | 5s | Hai phòng cạnh nhau, một bức tường ngăn — ấm vs lạnh; bóng sói giữa | Chủ đề: gần mà xa (Wes Anderson / Bong Joon-ho) | Nhạc bridge vào | Fade |

**Điểm cần duyệt:** shot 4B* là đề xuất thêm để gieo motif ngôi sao; shot 5B cần dựng mặt cắt nhà (chưa có plate).
