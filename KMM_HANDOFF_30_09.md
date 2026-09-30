# HANDOFF — MV "KHÔNG MỘT MÌNH" (KMM) · 30/09/2026

Dán file này vào chat đầu tiên của LLM mới và nói: "Đọc handoff này rồi tiếp tục gen keyframe KMM theo đúng quy tắc."

## 0. Dự án
- MV hoạt hình 3D 3'30" · 72 khung · "KHÔNG MỘT MÌNH", chiến dịch an toàn trẻ em trên mạng (dụ dỗ / bắt cóc online). Nhà tài trợ: UNICEF, UNODC, Bộ Công an.
- Người phụ trách: Hwi, Production Director, Purple Studio / FLEX Films.
- Việc của LLM: gen keyframe 16:9 từng cảnh bằng Higgsfield MCP, dùng ref nhân vật (character sheet) + plate background đã duyệt.

## 1. Quy tắc làm việc (Hwi đã dặn)
- Mỗi yêu cầu 1 ảnh. Chỉ gen nhiều khi Hwi nói rõ "3 option" (dùng generate_image_batch, 3 phương án khác nhau về góc máy/địa điểm).
- Chỉ 1K. Model `gpt_image_2`, `aspect_ratio` 16:9, `quality: medium` phải đặt tường minh (không đặt thì Higgsfield tự dùng low).
- Luôn gắn `folder_id` của project "MV KMM" (mục 5).
- Trả lời tiếng Việt, prompt tiếng Anh.
- Nếu yêu cầu không hợp lý / kém hiệu quả → phản biện và đưa giải pháp.
- Sau khi gen: jobs_wait → show_generation_by_ids → gửi link + vài dòng: ảnh làm gì, điểm cần soi (chữ/số lọt vào, mặt Mai, bóng có chạm trẻ không). LLM không xem được ảnh → luôn nói "chưa kiểm tra nội dung".
- Sửa ảnh: dùng job_id ảnh trước làm ref (role image) + "Keep Image 1 exactly … change only …".
- Khi tin nhắn mới của Hwi đến giữa lúc đang gen, xử lý cả hai, không bỏ sót yêu cầu.
- Thông tin không chắc thì nói là chưa chắc. Không khẳng định điều chưa kiểm tra.

## 2. Luật cứng của dự án
- Sài Gòn hiện đại 2026, sạch; không nông thôn/Hội An.
- Nhà Mai: nhà cấp bốn trong hẻm, khá giả, tầng trệt.
- Không chữ/số ở bất cứ đâu (biển hiệu, bao bì, đồng hồ, lịch, đèn tín hiệu, bảng LED, màn hình điện thoại). Đồng hồ = mặt trống + vạch chia + kim.
- Quái = bóng khói viền mờ, mắt hổ phách nhỏ phát sáng, không răng, KHÔNG BAO GIỜ chạm vào trẻ.
- Đồ vật đời thường làm vũ khí. Vết thương chỉ là băng cá nhân/vết xước.
- Mai không bao giờ mặc hoodie.
- Sàn matte, không gạch ô caro (trừ sàn lớp học chấp nhận).
- Trẻ em 6–6.5 đầu, người lớn 7–7.5 đầu; không chibi; "ít AI" nhất có thể; camera đọc được 2.5D.
- Style: stylized 3D render, thể khối bo tròn mềm, nét chì than mảnh lỏng tay, shading painterly, matte, grain nhẹ. Mai định nghĩa style → "EXACTLY the same art style as Image 1".

## 3. Nhân vật
Ref hiện tại là CHARACTER SHEET (Hwi đã update lại toàn bộ thiết kế). Ảnh ref thắng chữ: mô tả bên dưới là bản cũ, có thể đã đổi. Khi gen, thêm câu:
"Image N is a character reference sheet. Use it only for design, and draw ONE figure in the scene, not the sheet layout or turnaround poses."

Mô tả lock cũ (chỉ để tham khảo):
- 01_Mai: tóc đen ngang vai, mái bằng, kẹp tic-tac vàng bên phải. Đồng phục: sơ mi trắng cổ bẻ navy, khăn quàng đỏ, váy xếp ly navy, tất trắng, giày trắng, ba lô xanh da trời nhạt + móc sao vàng. Đồ ở nhà: áo thun vàng bơ trơn, short jean xanh nhạt, dép lê hồng; không khăn/ba lô. Không hoodie.
- 02_BanDanToc: da ngăm, tóc dài tết 2 bím, ba lô denim.
- 03_BanKinh: kính tròn đen, tóc buộc thấp, ba lô hồng + móc gấu.
- 04_BanMap: bạn trai mũm mĩm, đầu đinh, cầm bánh mì, short navy.
- 05_Bo: muối tiêu, kính mảnh, áo thun trắng, quần xám xanh, dép quai hậu nâu.
- 06_Me: búi thấp, áo kem, tạp dề be, quần ống rộng xanh rêu.
- 07_CoGiao: áo dài hồng, quần trắng, thước gỗ.
- 08_CoLaoCong: đồng phục cam, nón lá, chổi tre.
- 14_Cho: chó Phú Quốc, lông đỏ, tai dựng, đuôi cong.
- 17_Soi: sói bóng đêm, cao gầy bằng khói đen, tai nhọn dựng, mõm dài, vai dày, đuôi xù, mắt hổ phách nhỏ, không răng, bán trong suốt để bố mẹ "không thấy". Đây là ref sói đã chốt.
- Dân phòng: xanh olive, không chữ/patch, dùi cui (thay CSGT).

Nhân vật mới (chưa có mô tả, vai trò chưa rõ, đọc từ ảnh ref hoặc hỏi Hwi): 09_AnNinh, 10_CongAn, 15_TaiXe, 16_Bo_Fantasy, 18_Qua, 19_Nhen, 20_NguoiXau, 21_Me_Fantasy.

## 4. Higgsfield
- Workspace: `7d16e180-91e1-4bfc-a35e-8eed97d27b03` (private, gói creator). Workspace cũ `69f3f1fb-…` (ultra) KHÔNG còn nối: toàn bộ media_id và job_id cũ không dùng được.
- Project "MV KMM" (tạo mới 30/09): project_id = folder_id = `fef878e4-1957-439e-8b50-00a4ee8454c6`.
- Nạp tool: ToolSearch `select:mcp__Higgsfield__generate_image,mcp__Higgsfield__generate_image_batch,mcp__Higgsfield__jobs_wait,mcp__Higgsfield__show_generation_by_ids`.
- Upload thêm: `media_upload_widget`, gọi riêng 1 turn. Sandbox chặn upload.higgsfield.ai và *.cloudfront.net nên không tự upload/tải được.
- show_generation_by_ids với nhiều job (~22) có thể vượt giới hạn → đưa link thủ công.
- Đổi account Higgsfield thì mất hết media_id, phải tạo project mới + upload lại.

### 4a. Media ID nhân vật
| File | media_id |
|---|---|
| 01_Mai | b42c82ad-d58e-4fb3-bcf3-4d89dac09517 |
| 02_BanDanToc | 2755d89a-65c3-4a4f-9e34-669fe8968dbe |
| 03_BanKinh | fc1b53f9-386c-4326-aa1b-30089996aa18 |
| 04_BanMap | fd700683-cd2f-4766-8cee-59abc9b5dedb |
| 05_Bo | 819b9312-d35c-4c92-b5e5-f975f17b9e67 |
| 06_Me | d318bcb9-4768-43e3-95f0-14463b434891 |
| 07_CoGiao | 082374dd-e37b-4a81-b351-9ee0584847f1 |
| 08_CoLaoCong | 651ece17-dea7-4131-aa81-5642f5a0121a |
| 09_AnNinh | 1c452617-8da2-4aca-9192-7093dede0ba3 |
| 10_CongAn | 81cdd17a-1039-44b3-93f9-5724cdbd5e16 |
| 14_Cho | 8388a0fd-6e94-4433-97e3-ed4b92b45af8 |
| 15_TaiXe | 6f2ff8e2-08c5-47ad-9b71-25fa28d62738 |
| 16_Bo_Fantasy | f9500265-b7a9-485e-8720-ef2f16f0503c |
| 17_Soi | f48ff106-d9d6-4233-a770-d36f768a1f64 |
| 18_Qua | 6a271d30-4602-4348-8042-8728526956c5 |
| 19_Nhen | cdcbdc48-05d0-4875-b2c4-eb77a56cb96b |
| 20_NguoiXau | ae661756-c27e-4837-85cb-7bb91da7f6fd |
| 21_Me_Fantasy | 0d42f68e-37cb-44c1-8930-29d212572dbc |

### 4b. Media ID plate
| File | media_id |
|---|---|
| B02_Hem1_Day | 875ca1de-fe82-40c9-aaa3-1fae77e08461 |
| B02_Hem2_Day | 4f3d0ed0-f249-4da7-a72f-49e3c7849065 |
| B02_Hem3_Day | 8f5fe6b4-b2c1-4d80-b836-684bb85fbbed |
| B03_PhongMai1_Sunset | 71a09bcb-813d-4888-a25b-1bd5b602a00f |
| B04_NgaTu1_Day | ae680526-07ce-498d-9b3d-33e21298afc6 |
| B04_NgaTu2_Day | 375c3734-fe5a-4165-ac7c-81b1f6b605f5 |
| B05_Bus1_Day | 7b04666b-2fe0-41d7-b72d-5d39d89e9a4c |
| B06_ViaHe1_Day | fd1ba4f2-bdab-485e-9ae1-1837984e0b82 |
| B06_ViaHe2_Day | dd262c5c-9dfc-4cbb-9173-6c50d0280131 |
| B06_ViaHe3_Day | fc8f164d-8fb4-495e-8054-dc9e88e152f1 |
| B07_Station1_Noon | 49855481-6b7a-47e4-af30-b8a70d8acb19 |
| B07_Station2_Noon | 72ef884d-14be-473f-9de1-90dc12c9334a |
| B07_Station3_Noon | b672cf25-8b72-48c2-b4bd-ec328a2ad749 |
| B09_Truong1_Day | 03fbb6cc-dd7b-4c53-9f20-dfc7a17fcfdc |
| B10_PhongMai1_Night | 95a5e880-d642-48c2-9fd5-e930f2f3ea17 |
| B10_PhongMai1_Night2 | b97542df-5a4d-44be-9b59-c8c578ef2d1f |
| B11_Bep | a1f35aa7-b708-4696-99fb-85d025faebf8 |
| B12_Class | 3b2fcd92-040d-4efe-9654-525dda7dec90 |
| B13_HangQuan | b0399a7f-5c5e-4dad-add9-9d006f02e9fd |
| B13_HangQuan2 | 567e2b93-2041-40ab-a01b-755945f8a59a |
| B14_Boss | f1ae9d0a-c22c-4de8-92f0-a051fb01937c |
| BG01_DW1_1 (DarkWeb) | 080fd547-7e6d-4ea3-b44e-dc70202c0751 |
| BG01_DW2_2 (DarkWeb) | 664864d0-9f56-48c3-8a59-578f56417527 |
| BG01_DW3_1 (DarkWeb) | c37dafcb-50fc-4f03-b079-014023c6d127 |

Chưa có plate: B09_Truong3_Day, B08_Class1/3, phòng khách, phòng tắm, hành lang nhà Mai, hành lang trường. Cảnh cần các nơi này thì tự dựng bằng prompt hoặc xin Hwi upload thêm.
Ghi chú: B13 trong tài liệu cũ là "hành lang", file mới tên B13_HangQuan (hiểu là hàng quán). B14_Boss chưa rõ dùng cho cảnh nào.

## 5. Mẫu prompt
Cảnh có Mai + plate:

```
Image 1 is Mai (character reference sheet, use only for design, draw ONE figure), Image 2 is the [plate name] background plate. Create a 16:9 keyframe with EXACTLY the same art style as Image 1: stylized 3D render, soft rounded volumes, thin loose charcoal sketch lines, painterly shading, matte surfaces, subtle grain, not chibi. Same [location] as Image 2 (modern Saigon 2026 nha cap bon, matte floor), [time of day / lighting]. Camera: [angle]. [Mai action, expression]. She wears [school uniform | casual home outfit: plain butter-yellow tee, light-blue denim shorts, pink slides, yellow tic-tac clip, no hoodie]. [Other characters/props]. No text, no numbers, no logos, no writing anywhere, no shadow monsters, no other people.
```

Params: model `gpt_image_2`, aspect_ratio `16:9`, resolution `1k`, quality `medium`, folder_id, medias `[{value, role:"image"}]`.

Sửa ảnh: "Image 1 is the current keyframe … Keep Image 1 exactly: same room, same camera, same style … Change only: …" (ref = job_id ảnh trước; thêm media nhân vật nếu cần giữ thiết kế).

Bóng quái: "night-shadow [dog/wolf], dark smoke silhouette with soft wispy smoke edges, small glowing amber eyes, no teeth, far from the child and never touching her, semi-transparent so the adults do not notice it."

Composition theo hình bố cục của Hwi (hộp màu): đọc vị trí/kích thước/thứ tự che từng khối màu và mô tả bằng lời. Hình bố cục chưa upload nên chỉ theo mô tả; upload nếu muốn chính xác hơn.

## 6. Ảnh đã gen ở account CŨ (không dùng làm ref được)
Các cảnh đã làm ở account cũ (phòng Mai đêm, bố mẹ qua khe cửa, sói trước cửa, hành lang trường, hẻm sáng có bạn, 3 option buổi sáng...) có job_id gắn với workspace `69f3f1fb-…`. Ở workspace mới không dùng được, muốn dùng phải gen lại. Ảnh chưa ở account mới: chưa có ảnh nào.

## 7. Việc còn tồn đọng
- Hwi chưa phản hồi duyệt các cảnh phòng Mai đêm, phòng khách bố mẹ, hẻm có bạn, 3 option buổi sáng.
- Câu hỏi mở: giữ nét chì than hay flat hand-painted; khách chấp nhận nhân vật dân phòng/CSGT không; Sài Gòn vs UBND Hà Nội; thiết kế chiến sĩ, nông dân, hacker, hình thái bảo vệ bus, chị gái 16 tuổi.
- Xác nhận vai trò các nhân vật mới (09, 10, 15, 16, 18–21) và plate B14_Boss.
- Giao keyframe vào Desktop\KMM\Keyframes_29_09 (trước đó kẹt quyền tải Chrome).
