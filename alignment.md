# Đối chiếu nguồn và phụ đề

- Gói nguồn có đúng 16 PNG và 16 annotation, đánh số scene-01 đến scene-16; không có tệp SRT hay toàn văn CẢNH/HÌNH.
- Mỗi annotation chứa storyBasis, sceneDurationMs=9000 và một phần tử toàn cảnh. Lời kể trong scenes.json giữ nguyên storyBasis; không coi đó là toàn văn bản cũ.
- subtitles.srt là bản dựng nháp mới: 16 mục, mỗi mục ứng với một cảnh, tổng 144 giây. Không phải bản 106 mục/8 phút từng được nhắc trong lịch sử trao đổi.
- sources/original_srt_excerpt.srt giữ lại 4 mục đầu (0–20,5 giây) nhìn thấy trong ngữ cảnh trao đổi. Mục 1 trùng lời kể rút gọn scene-01 khi bỏ xuống dòng. Mục 2–4 bổ sung tình trạng sức khỏe của bà và nỗi lo của bọn trẻ, nhưng không hiện diện trong storyBasis của scene-01; không tự chèn hoặc chia thành cảnh mới.
- Cảnh vị khách xuất hiện là scene-02. Lịch sử trao đổi cho thấy mục SRT 5 bắt đầu 20,5 giây với “Một buổi tối”, nhưng mục này không đầy đủ nên không dùng để xác định điểm kết thúc hay sửa timeline.
- Chưa có dữ liệu để xác nhận liên kết 106 mục SRT với 16 cảnh. subtitle_cue_ids chỉ tham chiếu subtitles.srt mới trong gói này.
- Mô tả hình được biên soạn từ việc xem 16 ảnh hiện có; prompt mới dùng chung phong cách và quy tắc nhân vật. Không tuyên bố đây là nguyên văn prompt/HÌNH đã gửi.
- Ảnh nguồn có hình minh họa nhỏ giữa nền kem rộng và nét vẽ thiên về tranh. Ảnh được giữ nguyên; prompt vector là chỉ dẫn cho lần tạo ảnh sau, không phải khẳng định ảnh đã đúng phong cách.

## Khi có SRT và storyboard đầy đủ

1. Giữ nguyên mã scene-01…scene-16; thay narration bằng lời kể đầy đủ đã xác nhận.
2. Đối chiếu từng câu, gán các mục SRT thực tế vào subtitle_cue_ids; không giả định một mục bằng một cảnh.
3. Lấy start_ms/end_ms từ mục đầu/cuối của mỗi cảnh, kiểm tra cả thứ tự lẫn nội dung.
4. Thay mô tả/prompt bằng bản gốc nếu cần; cập nhật provenance và trạng thái nguồn.
5. Xuất lại storyboard.md và subtitles.srt, chạy công cụ kiểm tra.
