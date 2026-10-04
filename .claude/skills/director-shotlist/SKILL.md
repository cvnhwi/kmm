---
name: director-shotlist
description: Mở rộng (extend) một kịch bản / mô tả cảnh / lời bài hát thành phân cảnh chi tiết (shot list, storyboard, keyframe prompt) với góc máy, cỡ cảnh, chuyển động máy (fixed / dynamic), nhịp dựng và ngôn ngữ kể chuyện học từ các đạo diễn nổi tiếng. Dùng khi người dùng gửi kịch bản, treatment, beat sheet, lời MV, hoặc yêu cầu "phân cảnh", "shot list", "storyboard", "góc máy", "extend kịch bản", "chia cú máy", "kể chuyện bằng hình".
---

# Director Shotlist — biến kịch bản thành ngôn ngữ hình ảnh

Bộ nhớ chuyên môn gồm 4 file tham chiếu. Đọc theo nhu cầu, đừng đọc hết nếu không cần:

| File | Nội dung | Khi nào đọc |
|---|---|---|
| `references/01_camera_grammar.md` | Cỡ cảnh, góc máy, ống kính, chuyển động máy (fixed vs dynamic), bố cục, trục 180°, chuyển cảnh, ánh sáng | Luôn đọc khi chia cú máy |
| `references/02_directors.md` | Chữ ký hình ảnh của ~30 đạo diễn + "dùng khi nào" | Khi chọn phong cách / cần ý tưởng cho cảnh khó |
| `references/03_storytelling.md` | Cấu trúc kể chuyện, nhịp, suspense, setup/payoff, motif, MV & phim cho trẻ em | Khi phân tích kịch bản, xây arc |
| `references/04_output_format.md` | Mẫu shot list, mẫu prompt keyframe/video AI, ví dụ hoàn chỉnh | Khi xuất kết quả |

## Nguyên tắc vàng: BÁM SÁT KỊCH BẢN

1. **Kịch bản là luật.** Không đổi cốt truyện, không thêm nhân vật, không đổi thứ tự sự kiện, không đổi lời thoại. Mọi thứ thêm vào chỉ là *cách quay* để kể đúng điều kịch bản đã viết.
2. **Phân biệt rõ cái có sẵn và cái thêm.** Hành động/chi tiết do mình đề xuất thêm (insert, cutaway, reaction, establishing) phải đánh dấu `[đề xuất]` để người dùng duyệt.
3. **Mỗi cú máy phải trả lời được: "Cú này kể điều gì mà cú khác không kể được?"** Không có câu trả lời → bỏ.
4. **Góc máy = quan điểm.** Trước khi chọn góc, xác định: cảnh này là của ai (POV nhân vật nào), khán giả nên biết nhiều hơn / bằng / ít hơn nhân vật?
5. **Chuyển động phải có động cơ (motivated).** Máy di chuyển vì: nhân vật di chuyển, cảm xúc thay đổi, thông tin mới được hé lộ, hoặc nhịp nhạc. Không động cơ → để máy đứng yên (locked-off).
6. **Tương phản tạo nghĩa.** Xen kẽ fixed ↔ dynamic, rộng ↔ chặt, tĩnh ↔ ồn. Một chuỗi toàn dynamic sẽ mất sức; cú dynamic chỉ mạnh khi đứng sau cú tĩnh.
7. **Tôn trọng luật dự án.** Nếu repo có file luật (vd `KMM_HANDOFF_*.md`: không chữ/số, quái không chạm trẻ, Sài Gòn 2026…) thì mọi shot phải tuân thủ. Đối chiếu trước khi xuất.
8. **Nói thật về chỗ chưa chắc.** Kịch bản mơ hồ → nêu 2–3 phương án và đề xuất 1, không tự quyết chuyện quan trọng.

## Quy trình 6 bước khi nhận kịch bản

**Bước 1 — Đọc & tóm tắt (để người dùng xác nhận mình hiểu đúng)**
- Logline 1 câu, chủ đề (theme), nhân vật chính và mong muốn/nỗi sợ của họ.
- Tổng thời lượng, định dạng (MV / phim ngắn / TVC / animation), tỉ lệ khung, nhạc (BPM, cấu trúc verse/chorus nếu có).

**Bước 2 — Bóc beat (beat breakdown)**
- Chia kịch bản thành các *beat* (đơn vị thay đổi: một hành động, một phát hiện, một quyết định, một cảm xúc mới).
- Với mỗi beat ghi: *giá trị cảm xúc đầu → cuối* (vd an toàn → bất an). Beat không đổi giá trị là beat yếu → đề xuất gộp/rút.
- Xác định: inciting incident, midpoint, climax, resolution (xem `03_storytelling.md`).

**Bước 3 — Chọn "ngữ pháp hình ảnh" tổng (visual strategy)**
- Chọn 1–3 đạo diễn làm "giọng" chính, có lý do (vd: "Kore-eda cho đời thường của trẻ em + Spielberg cho khoảnh khắc nguy hiểm + Miyazaki cho phần fantasy").
- Đặt *quy tắc hình ảnh* cho cả phim và thay đổi theo arc. Ví dụ:
  - Phần an toàn: máy ngang tầm mắt trẻ, fixed / chậm, ống kính trung tính, bố cục cân.
  - Phần nguy hiểm: máy rời tầm mắt, tele nén không gian hoặc góc rộng méo, handheld nhẹ, khung lệch, nhiều khoảng trống tiêu cực.
  - Phần giải quyết: trở về tầm mắt, máy rút ra rộng, nhân vật không còn đứng một mình trong khung.
- Motif hình ảnh lặp lại (màu, vật, khung cửa, ánh sáng) để setup → payoff.

**Bước 4 — Chia cú máy (shot breakdown)**
Mỗi beat → 1 hoặc nhiều shot. Cho mỗi shot xác định:
- Cỡ cảnh (EWS/WS/MS/MCU/CU/ECU/Insert)
- Góc (eye-level / high / low / overhead / Dutch / POV / OTS)
- Ống kính cảm giác (wide 18–24 / normal 35–50 / tele 85–135+)
- Loại máy: **FIXED** (locked-off, tripod) hoặc **DYNAMIC** (dolly, track, crane, handheld, steadicam, whip, orbit, drone, push-in/pull-out, zoom, rack focus)
- Thời lượng ước tính (giây) + điểm cắt (cut on action / match cut / smash cut / dissolve…)
- Ý đồ kể chuyện (1 câu: shot này kể gì)
- Âm thanh / nhạc liên kết (beat nhạc, SFX, im lặng)

**Bước 5 — Kiểm tra (checklist trước khi xuất)**
- [ ] Mọi beat trong kịch bản đều có shot; không có shot nào kể chuyện ngoài kịch bản mà không gắn `[đề xuất]`.
- [ ] Trục 180° và hướng màn hình (screen direction) nhất quán; chỗ vượt trục có chủ đích và có lý do.
- [ ] Tỉ lệ fixed/dynamic hợp nhịp; cú mạnh nhất đặt ở climax.
- [ ] Có establishing cho mỗi bối cảnh mới (hoặc cố tình bỏ để gây mất phương hướng).
- [ ] Có reaction shot ở những khoảnh khắc cảm xúc chính.
- [ ] Tổng thời lượng khớp (MV: khớp số giây của bài).
- [ ] Không vi phạm luật dự án.

**Bước 6 — Xuất kết quả** theo mẫu trong `04_output_format.md`:
1. Tóm tắt + visual strategy (ngắn)
2. Bảng shot list
3. (Nếu cần) prompt keyframe tiếng Anh cho từng shot
4. Câu hỏi mở / điểm cần người dùng duyệt

## Phong cách trả lời
- Trả lời tiếng Việt; thuật ngữ máy quay giữ tiếng Anh (dolly in, OTS, rack focus…) vì đó là ngôn ngữ chung trên set.
- Prompt cho AI image/video viết tiếng Anh.
- Ngắn gọn ở phần giải thích, chi tiết ở bảng shot list.
- Kịch bản dài → làm từng sequence, hỏi duyệt rồi đi tiếp, thay vì đổ một lần 200 shot.
