# KMM: HANDOFF 2026-10-04 (phiên style A + chuyển cảnh A→B)

Repo `cvnhwi/kmm`. **Branch làm việc của phiên này: `claude/busy-hawking-7f4dok`.** Branch này đã gồm toàn bộ `claude/gracious-archimedes-cao5q7` (fast-forward, không ghi đè gì) cộng các commit mới của phiên này. Không tạo PR.

Thứ tự đọc khi mở box chat mới:
1. File này.
2. `KMM_RULES_SUMMARY.md`: rule style B, đầu file có ghi chú phân biệt hai style.
3. `HANDOFF_GUIDE.md`: ID media và thông số Higgsfield.
4. `STYLE_GUIDE_A.md` và `STYLE_A_SAMPLE_PROMPT.md`: style A.
5. `option_A2B_scene_hem_transition.md`: cảnh chuyển A→B, đủ v1-v4.

---

## 1. Hai style (user chốt 2026-10-03)
| | STYLE A (đời thực) | STYLE B (fantasy) |
|---|---|---|
| Video master | DAILY.mp4 `2535cacf-3f55-4f47-9e56-38bec54122e6`. Bản gốc HEVC 10-bit 1080p; vẫn gen được. | Fantasy.mp4 `24430dd0-a7ec-4d5c-a555-46abfb7600a1` |
| Mai | **01_Mai `fae9baae-3a83-4f65-bfe8-ee32fcc94a78`**. Đã soi ảnh: áo thuỷ thủ trắng cổ navy, khăn đỏ, váy xếp ly navy, bob nâu có mái, kẹp vàng bên phải, balo xanh nhạt, móc khoá sao vàng. | Mai fantasy `0d56fcb2-47cc-4271-b785-c73f4ab9a17b` |
| Look | 2D/3D lai mềm, vẽ tay (màu nước, gouache), cel-shade mềm, má hồng, ánh sáng ẤM dịu, tương phản thấp | 3D stylized cao cấp, vật liệu bóng, cyan-teal lạnh, haze, tương phản cao |
| Prompt | Mở đầu `DAILY-LIFE MASTER REFERENCE FIRST`. Gọi media bằng `<<<video_1>>>` / `<<<image_1>>>`. Các khối viết HOA không ngoặc: SPINE, REFERENCES, CHARACTERS, SPACE & BLOCKING, Shot N, RACCORD, CAMERA LAW, ACTING, LIGHTING & GRADE, STYLE, CONSTRAINTS, AVOID. Thêm AUDIO (chỉ tiếng động, không nhạc). | Khối `[ngoặc vuông]` theo skill `kmm-fantasy-video-prompt` |
| Tỉ lệ | Mai khoảng 13 tuổi, cao 6.5-7 đầu | 6-6.5 đầu |

Luật chung cho cả hai style:
- Không chữ, số hay logo.
- Real-time 24fps, không slow motion.
- Mỗi shot đúng một chuyển động máy; giữ trục 180°.
- Biểu cảm tiết chế.
- Chỉ tiếng động, KHÔNG nhạc.
- Gen vào folder MV KMM `11749213-086c-4a29-a963-b5a064eb4af7`.
- Thông số: `seedance_2_5`, `omni_reference`, draft, 480p, 16:9, `generate_audio: true`, `declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612`.

## 2. Cảnh đang làm: chuyển A→B ở hẻm (8s)
Nội dung: Mai (style A) đi một mình giữa hẻm, hai tay thả xuôi, điện thoại cầm lỏng ở tay PHẢI, không bấm máy, mặt hơi chán nản, trời đã là đêm. Sau đó chuyển sang style B.

Media đính kèm mọi bản:
- Video: DAILY `2535cacf…` và Fantasy `24430dd0…`.
- Ảnh: 01_Mai `fae9baae…`, Mai fantasy `0d56fcb2…`, hẻm `c0accc1d-53eb-4d6b-a777-acbac2133117`, điện thoại `b7eeb576-8bcf-4a98-b695-48a4e029fda1`.
- Từ v3: thêm Cổng Fantasy `22c1d2ad-9fc6-4ae8-ba39-747a28272bb0`.

| Bản | Nội dung | Job | Trạng thái |
|---|---|---|---|
| v1 op1/2/3 | Mai bấm điện thoại, chiều âm u. Op1 orbit 270°, op2 đẩy vào màn hình, op3 bóng mây quét | `feb8e84f…` / `9923a6ff…` / `2c86ffb6…` | COMPLETED (user không dùng) |
| v2 op1/2/3 | Tay thả, chán nản, đêm. Op1 orbit, op2 điện thoại tự sáng, op3 đèn tắt lần lượt | `9c1e6bf7…` / `497d1aa7…` / `3af0d101…` | COMPLETED |
| v3 | Orbit 200°, rễ cây mọc thành Cổng Fantasy trước mặt Mai | `878bec9d-496e-42c7-95a3-b6afe32dff4e` | COMPLETED. **User: "không rõ style A trước khi chuyển"** |
| v4 op1 | Orbit sửa lỗi style A, rễ → cổng | `63cb55e7-be58-40d9-895e-c0f44d5aa553` | Đã gửi gen, **chưa kiểm tra** |
| v4 op2 (mới) | Vũng nước: hình phản chiếu đã là B; Mai dẫm vào, gợn sóng lan ra biến A thành B; rễ → cổng | `4197748d-ec37-42c3-b41c-4ab904e13e7c` | Đã gửi gen, **chưa kiểm tra** |
| v4 op3 (mới) | Cổng rễ mọc xa phía trước, sóng B lan ngược về phía máy với mép rõ, quét qua Mai | `9b356ba6-5280-4a02-963a-72203975c88e` | Đã gửi gen, **chưa kiểm tra** |

**User bảo "dừng lại" sau khi v4 đã gửi.** Lịch tự kiểm tra đã bị huỷ. Bước tiếp theo: `jobs_wait` 3 job v4, gửi link cho user, đổi Status sang COMPLETED. Chỉ làm khi user yêu cầu.

### Chẩn đoán lỗi v3 (đã tự trích khung hình để xem)
- Đoạn đầu v3 tối, render 3D/anime bóng, gần như giống hệt style B.
- DAILY.mp4 thật sự là cảnh chạng vạng ấm, mềm, vẽ tay. Đêm tối cộng grade lạnh đã xoá hết chất này.
- **Cách sửa đã áp dụng ở v4:**
  - Style A là "đầu đêm vừa tối": trời còn xanh tím, đèn đường và cửa hàng màu đào-hổ phách chiếu sáng rõ, nền vẽ tay.
  - Phải chuyển rõ từ ẤM MỀM VẼ TAY sang LẠNH BÓNG 3D.
  - Đoạn A kéo dài 3.5-4.8s, mở bằng MCU thấy rõ mặt 01_Mai.
  - Avoid thêm "style A render 3D bóng, nửa đầu tối/lạnh".
- **Nếu v4 vẫn chưa rõ style A**, có hai hướng:
  - (a) Dùng bản DAILY đã chuyển H.264 720p `f8a3a6cb-4238-4e77-bac2-26092729d416`. File đã upload nhưng **chưa `media_confirm`** vì user chặn bước đó. Nếu dùng, gọi `media_confirm` type video trước.
  - (b) Tách thành 2 clip (một clip A thuần, một clip B thuần) rồi nối bằng dựng.

## 3. Kỹ thuật đã tìm ra trong phiên
- **Xem được nội dung video/ảnh:**
  1. Lấy URL cloudfront của media ref trong output `show_generation_by_ids`. URL dạng `https://d2ol7oe51mr4n9.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/<media_id>.mp4` hoặc `<media_id>_resize.jpg`. Kết quả gen nằm ở `d8j0ntlcm91z4.cloudfront.net/...`.
  2. Dùng `sandbox_exec` (Higgsfield) chạy `curl` + `ffmpeg` tile 4 khung nhỏ (scale 224, `-q:v 20`). Giữ base64 dưới khoảng 8k ký tự, nếu dài hơn output bị cắt.
  3. Ghi base64 ra file trong scratchpad, decode, rồi dùng `Read` để xem ảnh.
  - Máy local KHÔNG tải được CDN (proxy chặn 403).
- `show_medias` vẫn lỗi schema. `show_generation_by_ids` trả output quá lớn (bị lưu ra file), dùng `jq` để lấy link.
- Upload file do mình tạo: gọi `media_upload` → PUT trong sandbox kèm header `If-None-Match: *` → `media_confirm`.

## 4. Việc còn mở
- Xem 3 job v4, cho user chọn.
- User chưa duyệt 1080p bản nào.
- Có thể cập nhật `STYLE_GUIDE_A.md`: style A = ánh sáng ấm, sáng rõ, vẽ tay (bài học từ v3).
- Còn ID account cũ (⚠️) chưa upload lại: Hầm `b97b3e97…`, StandardB `c5746038…`.

## 5. Prompt mở đầu cho box chat mới (copy dán)
```
Tiếp tục dự án MV KMM. Repo cvnhwi/kmm, branch claude/busy-hawking-7f4dok. Đọc KMM_options/HANDOFF_2026-10-04_STYLE_A_B.md trước, rồi KMM_RULES_SUMMARY.md, HANDOFF_GUIDE.md, STYLE_GUIDE_A.md, STYLE_A_SAMPLE_PROMPT.md, option_A2B_scene_hem_transition.md. Trả lời tiếng Việt, prompt tiếng Anh. Style A = DAILY.mp4 2535cacf-3f55-4f47-9e56-38bec54122e6 + 01_Mai fae9baae-3a83-4f65-bfe8-ee32fcc94a78; Style B = Fantasy.mp4 24430dd0-a7ec-4d5c-a555-46abfb7600a1 + Mai fantasy 0d56fcb2-47cc-4271-b785-c73f4ab9a17b. Mọi gen vào folder MV KMM 11749213-086c-4a29-a963-b5a064eb4af7. Việc đầu tiên: kiểm tra 3 job v4 (63cb55e7..., 4197748d..., 9b356ba6...).
```
