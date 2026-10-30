# Hãy cứ khóc đi, con tim bé nhỏ, nhưng đừng gục ngã

Dự án storyboard whiteboard tiếng Việt, dựa trên câu chuyện của Glenn Ringtved theo thông tin người dùng cung cấp. Chuẩn hóa ngày 30/10/2026.

**Trạng thái: khôi phục một phần nguồn.** Dự án có 16 cảnh được xác nhận bằng 16 ảnh và 16 annotation trong gói nguồn. Lời kể là bản rút gọn nguyên văn từ `storyBasis`; chưa khôi phục toàn văn storyboard CẢNH/HÌNH và bản SRT cũ. Không thêm cảnh ngoài dữ liệu nguồn.

## Tệp và thư mục

| Đường dẫn | Nội dung |
| --- | --- |
| `scenes.json` | Dữ liệu chuẩn UTF-8: mã cảnh, thứ tự, lời kể, mô tả hình, prompt, ảnh, thời gian và nguồn |
| `storyboard.md` | Bản đọc theo cấu trúc CẢNH / HÌNH, có ảnh xem trước |
| `subtitles.srt` | **Phụ đề dựng nháp mới**, 16 mục, tổng 2 phút 24 giây |
| `alignment.md` | Kết quả đối chiếu, phần thiếu và cách cập nhật khi có nguồn đầy đủ |
| `assets/images/` | 16 PNG nguồn được giữ nguyên |
| `sources/annotations/` | 16 annotation nguồn được giữ nguyên |
| `sources/original_srt_excerpt.srt` | Chỉ 4 mục đầu SRT cũ nhìn thấy trong ngữ cảnh; không phải bản đầy đủ |
| `tools/validate.py` | Kiểm tra JSON, mã/thứ tự cảnh, tệp ảnh và sự khớp phụ đề dựng nháp |

## Lời kể, hình ảnh và thời gian

Mỗi cảnh giữ mã `scene-01` đến `scene-16`. `narration` giữ nguyên lời kể rút gọn trong annotation. `image_description` là mô tả mới từ việc xem ảnh có sẵn; `image_prompt` được chuẩn hóa mới với phong cách **minimalist 2D vector storybook**, khung 16:9, không chữ trong hình và quy tắc nhất quán nhân vật. Các trường `provenance` ghi rõ nguồn này; không coi prompt mới là bản gốc đã gửi.

Ảnh có sẵn được bảo toàn, không tái tạo. Chúng có nét vẽ thiên về tranh và phần lề nền kem rộng; chưa tương ứng hoàn toàn với prompt vector mới.

`subtitles.srt` nối tiếp 16 khoảng 9 giây lấy từ `sceneDurationMs` của annotation. Đây là thời gian dựng nháp, **không phải SRT 8 phút/106 mục đã được đề cập trước đây**, và chưa căn theo bản thu âm. `subtitle_cue_ids` chỉ tham chiếu các mục của SRT mới trong dự án. Xem `alignment.md` trước khi dựng video cuối.

## Kiểm tra trên máy

Cần Python 3, không cần cài thư viện bổ sung. Từ thư mục dự án, chạy:

```bash
python tools/validate.py
```

## Đưa lên GitHub bằng trình duyệt

1. Giải nén gói tải xuống trên máy tính.
2. Mở repository đích mà bạn có quyền ghi. Nếu repository đã có các tệp cùng tên, kiểm tra trước khi thay thế.
3. Chọn **Add file → Upload files**; kéo toàn bộ nội dung bên trong thư mục `haycukhocdi-storyboard` vào trang, gồm cả các thư mục con. Không chỉ tải tệp ZIP nếu muốn đọc storyboard và dữ liệu trực tiếp trên GitHub.
4. Nhập nội dung commit, ví dụ `Add normalized 16-scene storyboard`, rồi chọn **Commit changes**.
5. Mở lại `scenes.json`, `storyboard.md`, `subtitles.srt` và `README.md`; kiểm tra đủ 16 cảnh và các ảnh hiển thị.

## Đưa lên repository mới bằng Git

Tạo một repository trống, thay `REPOSITORY_URL` bằng URL repository đó. Chạy trong thư mục dự án:

```bash
git init -b main
git add .
git commit -m "Add normalized 16-scene storyboard"
git remote add origin REPOSITORY_URL
git push -u origin main
```

Nếu repository đã có lịch sử, clone repository về rồi chép các tệp vào thư mục mong muốn, kiểm tra `git diff`, commit và push theo nhánh đang sử dụng. Không chạy quy trình khởi tạo trên để thay lịch sử đã có.

## Ghi nhận nguồn

Gói đầu vào: `haycukhocdi_whiteboard_pack.zip`; mã SHA-256 lưu trong `scenes.json`. Không mặc định lần gửi nội dung trước đã tạo commit trên GitHub. Việc đóng gói này không cấp quyền sử dụng đối với tác phẩm gốc.
