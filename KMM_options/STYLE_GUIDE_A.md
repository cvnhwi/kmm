# STYLE A: DAILY-LIFE (đời thực, hand-painted). Cập nhật 2026-10-03

> Style B = toàn bộ rule fantasy hiện có (`STYLE_GUIDE_B.md`, skill `kmm-fantasy-video-prompt`).
> Style A = cảnh ĐỜI THỰC, dùng **01_Mai** (KHÔNG phải Mai fantasy). Không nhầm với "style A" cũ đã xoá.
> Prompt mẫu gốc của user: `STYLE_A_SAMPLE_PROMPT.md` (giữ nguyên văn).

## 1. Media (CHƯA CHỐT ID, hỏi/xác nhận trước khi gen)
| Slot | Vai | ID |
|---|---|---|
| video_1 | Video master DAILY-LIFE (style, mood, animation feel) | ❓ chưa có |
| image_1 | Mai = 01_Mai | ❓ có thể là `fae9baae-3a83-4f65-bfe8-ee32fcc94a78` (Mai đời thực), chờ user xác nhận |
| image_2.. | Plate bối cảnh (vd hẻm `c0accc1d-…`) | theo cảnh |
| image_n | Sinh vật (vd sói `b5f7908e-…`) | theo cảnh |
Cú pháp tham chiếu trong prompt: `<<<video_1>>>`, `<<<image_1>>>`… (khác style B dùng "Video 1 / Image 1").

## 2. Cấu trúc prompt (thứ tự khối, chữ IN HOA, không dùng ngoặc vuông)
1. Dòng đầu: `DAILY-LIFE MASTER REFERENCE FIRST: <<<video_1>>> is the master reference for the style, mood and characters of this whole clip. Match its render look, hand-painted finish, materials, colour palette, lighting mood, atmosphere, character design, proportions and animation feel on every frame; do not copy its exact shots, camera or story — <ngoại lệ mood của cảnh> and follows LIGHTING & GRADE.`
2. Dòng thông số: `<N>-second clip, 16:9, locked at 24 fps, <K> shots joined by hard cuts, real-time speed, natural 24 fps animation timing, no slow motion, no speed ramp, no frame interpolation.`
3. **SPINE**: câu chuyện 1 đoạn + cảm xúc chủ đạo (vd "Dread, danger…").
4. **REFERENCES**: vai từng media; plate = "layout… locked exactly from this plate, re-lit as…" + dress set cho ĐÚNG chất Việt Nam (liệt kê đạo cụ); "design only: draw ONE figure of each, never the sheet layout".
5. **CHARACTERS**: mô tả nhân vật verbatim theo ảnh + Expression của cảnh.
6. **SPACE & BLOCKING**: một nơi, một thời điểm; tường trái/phải; hướng di chuyển; vị trí camera, trục 180°; nguồn sáng thực.
7. **Shot N (t-t s)**: CỠ CẢNH + GÓC + **lens bằng độ FOV (vd 30°)** + **ĐÚNG MỘT camera move** (hoặc PERFECTLY LOCKED-OFF) → bố cục (rule of thirds, tiền cảnh cách lens bao nhiêu cm) → hành động → điều gì KHÔNG có trong shot → `Hard cut.` (shot cuối: `Stable end frame.`)
8. **RACCORD**: ánh sáng, khí quyển, trang phục, đạo cụ, hướng màn hình, ai có mặt ở shot nào.
9. **CAMERA LAW**: luật cỡ cảnh/góc/move cho cả clip; liệt kê lại từng shot.
10. **ACTING**: mắt → đầu → thân, anticipation, follow-through; cường độ cảm xúc.
11. **LIGHTING & GRADE**
12. **STYLE**
13. **CONSTRAINTS**: tóm luật đếm được (số nhân vật, số shot/cut, 1 move/shot, không chữ…).
14. **AVOID**: liệt kê dài, gồm cả lỗi đảo ngược của từng shot (vd "the wolf charging in Shot 4").

## 3. Luật riêng style A (rút từ prompt mẫu)
- **Look:** hand-painted trên nền hybrid 3D/2D: watercolour wash, gouache dry-brush, cel-shade mềm, nét sepia-charcoal thưa (không đen tuyền). Paper grain thấp, đều, **không bao giờ trên da mặt**; hatching chì màu chỉ ở vải, tóc, lông thú, sương, nền. Nền phẳng hơn nhân vật. Nét đều, không line boil, không shimmer.
- **Mai (01_Mai):** nữ sinh VN ~13 tuổi, **6.5-7 đầu** (khác style B 6-6.5); bob nâu sẫm mái thẳng, kẹp oval vàng bên PHẢI; mắt nâu to, da sáng má hồng; áo thuỷ thủ trắng cổ/viền navy, khăn đỏ thắt giữa, váy xếp ly navy lưng cao; balo xanh nhạt miếng da nâu hình thoi, móc khoá sao vàng bên phải. Không hoodie, không chibi.
- **Biểu cảm:** tiết chế 1/3-1/2, không há miệng hét, không nước mắt chảy.
- **Rim light ấm vàng-hổ phách** (golden-amber, halation nhẹ), không hồng-trắng/trắng lạnh, không đổi màu da; fill nhẹ + catchlight nhỏ trên mặt. Bóng teal-indigo đọc được, không đen kịt.
- **Ánh sáng chỉ từ nguồn thực** (đèn đường…); chớp chậm, không đều, không strobe nhanh; không khung đen hoàn toàn.
- **Camera:** mỗi shot đúng MỘT move (dolly in / rack focus kết thúc dolly / locked-off), không rung, không whip, không zoom snap, không méo góc rộng. Không hai shot trùng CẢ cỡ cảnh lẫn góc; mỗi shot một lens khác. Dutch chỉ ở shot được chỉ định.
- **Mẫu này cấm wide/establishing**, mọi shot từ trên gấu váy trở lên, không thấy chân/giày (rule của cảnh hẻm; cảnh khác tuỳ yêu cầu).
- **Khí quyển** (sương…) có mặt và chuyển động liên tục ở MỌI shot, cùng mật độ, không che nhân vật, vẽ kiểu watercolour không phải fog card CG.
- **Ẩn/hiện có kiểm soát:** ghi rõ shot nào sinh vật VẮNG MẶT, shot nào ĐỨNG YÊN, shot nào mới HÀNH ĐỘNG; lặp lại ở RACCORD, CONSTRAINTS, AVOID.
- Luật chung với B vẫn giữ: không chữ/số/logo/biển số; real-time 24fps; trục 180°; acting Disney; đám đông không đồng loạt; không gen trùng, folder MV KMM; SFX only NO music (chưa có trong mẫu → mặc định thêm khối AUDIO trước AVOID, xem mục 4).

## 4. Điểm lệch so với style B (đã flag, chờ user chốt)
1. **Sói style A** có "subtle dark-grey muscle and fur definition", nét viền sketch, mắt vàng-gold hạt hạnh nhân, "jaw just open" → khác luật B (đen phẳng như bóng, không khối, không răng). Mặc định: theo mẫu A cho cảnh A, nhưng thêm "no visible teeth/fangs" và giữ "never touches Mai".
2. **Mắt không con ngươi** chưa ghi trong mẫu → mặc định vẫn thêm vào cho mọi sinh vật bóng tối.
3. **Không có khối âm thanh** → mặc định thêm `AUDIO: diegetic SFX only… NO music, NO score, NO melody.`
4. **Tỉ lệ Mai** 6.5-7 đầu (A) vs 6-6.5 (B): theo mẫu cho style A.
